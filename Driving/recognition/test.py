import keras
import numpy as np
import cv2
from time import time as second



net = keras.models.load_model('model-31x31.h5')
net.summary()

img = cv2.imread('stop.png')
img = cv2.resize(img, (32, 32))
img = img/255.

t_start = second()
data_frame = np.array([img])
pred = net.predict(data_frame)[0]
print(len(pred))
print(np.argmax(pred))
print(second() - t_start)
