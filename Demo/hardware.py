import numpy as np
import bluetooth
import time
import cv2
from threading import Thread
from queue import Queue


class Car_BLE:
    available = False

    def __init__(self, name, port=1, address=None):
        if address is None:
            for add in bluetooth.discover_devices():
                if name == bluetooth.lookup_name(add):
                    address = add
                    break
        if address is not None:
            print('Found', address)
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((address, port))
            self.available = True
            print('Connected')
        else:
            print('Cannot found')

    def send(self, msg):
        if self.available:
            self.sock.send(msg + '\n')
        else:
            print('BLE not available')

    def close(self):
        self.pause()
        if self.available:
            self.sock.close()
            self.available = False
        else:
            print('BLE not available')

    def action(self, act):
        if act == 0:
            self.sock.send('A-2\n')
        elif act == 1:
            self.sock.send('A0\n')
        elif act == 2:
            self.sock.send('A2\n')

    def speed(self, spd):
        spd = int(spd*7.5)
        if self.available:
            self.sock.send('S' + str(spd) + '\n')
            time.sleep(0.1)
        else:
            print('BLE not available')

    def delta(self, dlt):
        if self.available:
            self.sock.send('S' + str(dlt) + '\n')
            time.sleep(0.1)
        else:
            print('BLE not available')

    def pause(self):
        if self.available:
            self.sock.send('P\n')
        else:
            print('BLE not available')


class Camera:
    def __init__(self, ID=0, fps=10, resolution=(640, 360), input_shape=(48, 27)):
        self.resolution = resolution
        self.input_shape = input_shape
        print('Camera starting...')
        self.camera = cv2.VideoCapture(ID)

        self.camera.set(cv2.CAP_PROP_FPS, fps)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
        print('Camera running')

    def read(self):
        ret, frame = self.camera.read()
        mini = cv2.resize(frame, self.input_shape)
        mini = np.array([mini])
        return frame, mini

    def close(self):
        self.camera.release()

    def draw_grid(self, img):
        blue = (255, 0, 0)
        red = (0, 0, 255)
        thickness = 1
        width, height = self.resolution
        img = cv2.line(img, (int(width / 2), 0), (int(width / 2), height), blue, thickness)                             # center
        img = cv2.line(img, (0, int(height * 0.2)), (width, int(height * 0.2)), red, thickness)      # speed bounder
        img = cv2.line(img, (int(width * 0.3), int(height / 2)), (int(width * 0.7), int(height / 2)), blue, thickness)
        img = cv2.line(img, (int(width * 0.3), int(height / 3)), (int(width * 0.7), int(height / 3)), blue, thickness)
        img = cv2.line(img, (0, int(height * 2 / 3)), (width, int(height * 2 / 3)), blue, thickness)

        img = cv2.line(img, (int(width * 0.5), 0), (int(width * 0.2), height), blue, thickness)
        img = cv2.line(img, (int(width * 0.5), 0), (int(width * 0.8), height), blue, thickness)

        img = cv2.line(img, (int(width * 0.5), int(height * 0)), (int(width * 0.1), height), blue, thickness)
        img = cv2.line(img, (int(width * 0.5), int(height * 0)), (int(width * 0.9), height), blue, thickness)
        return img
