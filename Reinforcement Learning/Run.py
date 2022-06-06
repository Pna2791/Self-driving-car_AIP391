import cv2
import numpy as np
from Driving_Environment import Driving
import time

driving_env = Driving()
for i in range(20):
    driving_env.action(1)
    print(i)
    cv2.waitKey(100)

driving_env.action(2)
for i in range(20):
    driving_env.action(0)
    print(i)
    cv2.waitKey(100)

cv2.waitKey()
cv2.destroyAllWindows()
