import keras
import numpy as np
from BLE import Car_BLE
import time
import cv2

input_shape = (64, 36)

height, width, fps_set = 360, 640, 30
preview_size = (width, height)

address = '00:19:10:09:3B:C7'
# car = Car_BLE('HC-06', address=address)
# car.speed(200)
# car.delta(100)

net = keras.models.load_model('model/model-v2.h5')

print('Camera starting...')
camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)

camera.set(cv2.CAP_PROP_FPS, fps_set)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
print('Camera running')


def save_video(img, ind):
    path = 'dataset/l4/' + '{:0>4d}'.format(ind) + '.png'
    cv2.imwrite(path, img)


def draw_grid(img):
    blue = (255, 0, 0)
    img = cv2.line(img, (int(width / 2), 0), (int(width / 2), height), blue, 1)
    img = cv2.line(img, (int(width * 0.3), int(height / 2)), (int(width * 0.7), int(height / 2)), blue, 1)
    img = cv2.line(img, (int(width * 0.3), int(height / 3)), (int(width * 0.7), int(height / 3)), blue, 1)
    img = cv2.line(img, (0, int(height * 2 / 3)), (width, int(height * 2 / 3)), blue, 1)

    img = cv2.line(img, (int(width * 0.5), 0), (int(width * 0.2), height), blue, 1)
    img = cv2.line(img, (int(width * 0.5), 0), (int(width * 0.8), height), blue, 1)

    img = cv2.line(img, (int(width * 0.5), int(height * 0)), (int(width * 0.1), height), blue, 1)
    img = cv2.line(img, (int(width * 0.5), int(height * 0)), (int(width * 0.9), height), blue, 1)
    return img


t_start = time.time()
frame_index = 0
count = 0
fps = 0
time_fps = time.time()+1
while True:
    try:

        ret, frame = camera.read()
        img = cv2.resize(frame, input_shape)

        act = net.predict(np.array([img]))
        act = np.argmax(act)
        # car.action(act)
        count += 1
        if time_fps < time.time():
            fps = count
            count = 0
            time_fps = time.time() + 1

        print(act, fps, 'fps')
        t_start = time.time()

        save_video(frame, frame_index)
        frame_index += 1
        cv2.imshow('frame', frame)

        save_video(frame, frame_index)
        frame_index += 1
        frame = draw_grid(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except:
        break


camera.release()
cv2.destroyAllWindows()

# car.pause()
# car.close()
