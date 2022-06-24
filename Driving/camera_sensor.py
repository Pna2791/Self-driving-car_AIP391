import cv2
from threading import Thread
from queue import Queue
import time


class Camera:
    def __init__(self, device, resolution, fps):
        def camera_threading():
            print('Camera starting')
            camera = cv2.VideoCapture(device, cv2.CAP_DSHOW)
            camera.set(cv2.CAP_PROP_FPS, fps)
            camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
            camera.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
            print('Camera recording')
            while self.running:
                ret, frame = camera.read()
                self.images.put(frame)
                time.sleep(0.01)

        self.running = True
        self.images = Queue()
        self.cam_reading = Thread(target=camera_threading)
        self.cam_reading.start()

    def read(self):
        data = self.images.get(block=True)
        return data

    def available(self):
        return not self.images.empty()

    def size(self):
        return self.images.qsize()

    def close(self):
        self.running = False
