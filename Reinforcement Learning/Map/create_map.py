import cv2
import numpy as np

width, height = 1000, 600

lane_size = 100
start_point = (height/2, 100)

img = np.zeros((height, width), dtype=np.uint8)

# Draw line
img = cv2.line(img, (0, int((height+lane_size)/2)), (width, int((height+lane_size)/2)), 255, 2)
img = cv2.line(img, (0, int((height-lane_size)/2)), (width, int((height-lane_size)/2)), 255, 2)
img = cv2.line(img, (50, 0), (50, height), 255, 2)


cv2.imshow('map', img)
cv2.imwrite('Map_1.png', img)
print(img.shape)
cv2.waitKey()
cv2.destroyAllWindows()
