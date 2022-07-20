import keras
import numpy as np
from tools.BLE import Car_BLE
import time
import cv2

from yolo_model import YOLO

input_shape = (48, 27)

height, width, fps = 360, 640, 10
preview_size = (width, height)

address = '00:19:10:09:3B:C7'
# car = Car_BLE('HC-06', address=address)
time.sleep(1)
# car.speed(400)
time.sleep(1)
# car.delta(200)
# time.sleep(1)
# car.delta(200)

net = keras.models.load_model('models/model-gen-2.h5')
yolov5 = YOLO(weights='models/yolov5s_300_64_416x416px.pt', imgsz=[416, 416], conf_thres=0.1)

print('Camera starting...')
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

camera.set(cv2.CAP_PROP_FPS, fps)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
print('Camera running')


def save_video(img, ind, act: str):
    path = 'D:\Desktop\AIP391\Lane detection\data\sign classification/raw/0' + '{:0>5d}'.format(ind) + f'.png'
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
frame_index = 850
while True:
    try:
        ret, frame = camera.read()
        img = cv2.resize(frame, input_shape)

        act = net.predict(np.array([img]))
        ts, signs, wds = yolov5.predict(img)
        act = np.argmax(act)
        # car.action(act)

        print(f'{act} -- {round(1 / (time.time() - t_start))} fps -- signs = {signs}')
        t_start = time.time()

        save_video(frame, frame_index, act)
        frame_index += 1
        ratio = max(frame.shape)/416
        for i, box in enumerate(wds):
            for j in range(len(box)):
                box[j] = int(box[j]*ratio)
            cv2.rectangle(frame, pt1=(box[2], box[3]), pt2=(box[0], box[1]), color=(255,0,0), thickness=2)
        # frame = draw_grid(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except:
        break


camera.release()
cv2.destroyAllWindows()

# car.pause()
# car.close()