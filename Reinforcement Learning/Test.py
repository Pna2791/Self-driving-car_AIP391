import cv2
import numpy as np
import time

img = cv2.imread('car.png')
angle = 45



height, width = img.shape[:2]
center = (width/2, height/2)
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=angle, scale=1)
rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))

for i in range(255):
    rotated_image[:, :] = i
    cv2.imshow('image', rotated_image)
    print(i)
    cv2.waitKey(30)
# print(rotated_image)


cv2.waitKey()
cv2.destroyAllWindows()
