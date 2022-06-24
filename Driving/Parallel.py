import keras
import numpy as np
from recoding import Recorder
from camera_sensor import Camera
import time
import cv2


input_shape = (64, 36)
height, width, fps_set = 360, 640, 10
preview_size = (width, height)


def save_video(recoder, img, ind):
    path = 'dataset/l3/' + '{:0>4d}'.format(ind) + '.png'
    recoder.write(path, img)


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


if __name__ == '__main__':
    net = keras.models.load_model('model/model-v2.h5')

    camera = Camera(1, preview_size, fps_set)
    recoder = Recorder()


    t_start = time.time()
    frame_index = 0
    count = 0
    fps = 0
    time_fps = time.time()+1
    while True:
        if camera.available():
            count += 1
            frame = camera.read()
            img = cv2.resize(frame, input_shape)

            act = net.predict(np.array([img]))
            act = np.argmax(act)

            if time_fps < time.time():
                fps = count
                count = 0
                time_fps = time.time() + 1

            print(act, fps, 'fps')
            t_start = time.time()

            save_video(recoder, frame, frame_index)
            frame_index += 1
            cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    camera.close()
    cv2.destroyAllWindows()
    recoder.stop()
