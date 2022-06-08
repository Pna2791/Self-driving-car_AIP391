import cv2
import numpy as np
from Driving_Environment import Driving
import time


driving_env = Driving()

t_start = time.time()
for i in range(10):
    driving_env.run(1)
    print(i)
    cv2.waitKey(100)

driving_env.run(2)
for i in range(50):
    driving_env.run(0)
    print(i)
    cv2.waitKey(100)
print(time.time() - t_start)
cv2.waitKey()
cv2.destroyAllWindows()
