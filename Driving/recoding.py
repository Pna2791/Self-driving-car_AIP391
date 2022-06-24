import cv2
from queue import Queue
from threading import Thread
import time


class Recorder:
    def __init__(self):

        def writing_thread():
            print('Recording start')
            while self.running:
                if not self.imgs.empty():
                    img = self.imgs.get()
                    name = self.names.get()
                    cv2.imwrite(name, img)
                time.sleep(0.01)
            print('Recording stop')

        self.running = True
        self.imgs = Queue()
        self.names = Queue()
        self.thread = Thread(target=writing_thread)
        self.thread.start()

    def write(self, name, img):
        self.imgs.put(img)
        self.names.put(name)

    def stop(self):
        self.running = False
