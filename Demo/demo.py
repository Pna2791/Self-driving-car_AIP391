import time

from models.detect_model import YOLO, CNN

import keras
from hardware import Camera, Car_BLE
from time import time as second
import numpy as np
import cv2


flag_send = False
ind = 0

speed, speed_min = (60, 40)
speed_max = [80]
flag_stop = False
flag_min = 40
flag_max = 60
flag_unmax = 60


input_shape = (48, 27)
camera_resolution   = (1280, 720)
camera_fps          = 10
preview_size = (960, 540)
top = int(camera_resolution[1] * 0.2)

camera  = Camera(ID=0, resolution=camera_resolution, fps=camera_fps, input_shape=input_shape)
model   = YOLO(imgsz=(640, 640), weights='weights/sign_detection_end.pt', conf_thres=0.6,
               input_resolution=camera_resolution, output_resolution=(50, 50), )
cnn     = CNN(weights='weights/signs-50x50-v2.h5', input_shape=(50, 50), conf_thres=0.5)
driver = keras.models.load_model('weights/model-gen-2.h5')

class_names = ['cam di nguoc chieu', 'duong cam', 'slow', 'stop', 'red light', 'yellow light', 'green light', 'limit 20', 'limit 40', 'limit 50', 'limit 60', # 10
               'limit 70', 'limit 80', 'limit 90', 'limit 100', 'min 20', 'min 40', 'min 60', 'min 80', 'turn left', 'turn right', 'unlimit 40', 'unlimit 50',        # 21
               'unlimit 60', 'unlimit 70', 'unlimit all']
limit_speed = [20, 40, 50, 60, 70, 80, 90, 100]
min_speed   = [20, 40, 60, 80]
unlinmit    = [40, 50, 60, 70, 100]


if flag_send:
    address = '00:19:10:09:3B:C7'
    car = Car_BLE('HC-06', address=address)
    car.speed(speed)
    time.sleep(1)
    car.delta(0.6)


def save_video(img, ind):
    path = 'data/demo/' + '{:0>5d}'.format(ind) + '.png'
    cv2.imwrite(path, img)


red = (0, 0, 255)
blue = (255, 0, 0)


def draw_infor(frame):
    frame = cv2.putText(frame, str(speed_min), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, blue, 2, cv2.LINE_AA,)
    frame = cv2.putText(frame, str(speed_max[-1]), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, blue, 2, cv2.LINE_AA,)
    frame = cv2.putText(frame, str(speed), (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, blue, 2, cv2.LINE_AA,)
    return frame


def stop():
    global ind
    if flag_send:
        car.pause()
    t_out = second() + 1
    while t_out > second():
        frame, imgs = camera.read()
        boxes = model.predict(frame[top:])
        boxes, imgs = model.crop_images(frame[top:], boxes, top)

        frame = camera.draw_grid(frame)
        if len(imgs) > 0:
            thres, indexes = cnn.predict(imgs)
            for box, th, index in zip(boxes, thres, indexes):
                if index == 3:
                    t_out = second() + 1

                frame = cv2.rectangle(frame, box[0], box[1], red, thickness=3)
                frame = cv2.putText(frame, str(th) + ' ' + class_names[index], box[0], cv2.FONT_HERSHEY_SIMPLEX, 1, red, 2, cv2.LINE_AA,)

        frame = cv2.putText(frame, 'STOP', (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, red, 3, cv2.LINE_AA,)
        save_video(frame, ind)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        ind += 1


def run():
    global ind, flag_stop, flag_max, flag_min, flag_unmax, speed_min, speed_max, speed
    while True:
        t_start = second()
        frame, imgs = camera.read()

        data = driver.predict(imgs)
        data = np.argmax(data)
        if flag_send:
            car.action(data)
        # print(data)

        boxes = model.predict(frame[top:])
        boxes, imgs = model.crop_images(frame[top:], boxes, top)

        frame = camera.draw_grid(frame)
        if len(imgs) > 0:
            thres, indexes = cnn.predict(imgs)
            for box, th, index in zip(boxes, thres, indexes):
                frame = cv2.rectangle(frame, box[0], box[1], red, thickness=3)
                frame = cv2.putText(frame, str(th) + ' ' + class_names[index], box[0], cv2.FONT_HERSHEY_SIMPLEX, 1, red, 2, cv2.LINE_AA,)

                if index == 3:
                    flag_stop = True

                if 7 <= index <= 14:    # limit speed
                    val = limit_speed[index-7]
                    if flag_max == val:
                        if speed_max[-1] != val:
                            speed_max.append(val)
                            speed = int( (val + speed_min) / 2)
                            if flag_send:
                                car.speed(speed)
                    else:
                        flag_max = val

                if 15 <= index <= 18:       # speed min
                    val = min_speed[index-15]
                    if flag_min == val:
                        if speed_min != val:
                            speed_min = val
                            speed = int( (val + speed_max[-1]) / 2)
                            if flag_send:
                                car.speed(speed)
                    else:
                        flag_min = val

                if 21 <= index <= 25:
                    val = unlinmit[index-21]
                    if flag_unmax == val:
                        if speed_max[-1] == val:
                            speed_max.pop()
                            speed = int( (speed_max[-1] + speed_min) / 2)
                            if flag_send:
                                car.speed(speed)
                    else:
                        flag_unmax = val

        frame = draw_infor(frame)
        save_video(frame, ind)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        ind += 1
        if flag_stop:
            stop()
            flag_stop = False
        print(second() - t_start)

    if flag_send:
        car.close()
    camera.close()
    cv2.destroyAllWindows()
    print('index:', ind)

run()
