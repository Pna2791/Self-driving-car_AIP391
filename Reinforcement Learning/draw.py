import cv2
import numpy as np


def draw_center(background, img, position):
    bg_sum = background.sum()
    img_sum = img.sum()

    # pos: X, Y
    height, width = img.shape[:2]
    top = position[1] - int(height/2)
    left = position[0] - int(width/2)

    # cv2.imshow('Background', background)
    output = np.array(background)
    output[top:top+height, left:left+width] += img

    n_white = output.sum()
    yield output
    yield img_sum+bg_sum != n_white


def draw_rotation(background, img, position, angel):
    pass


def rotaion(img, angle):
    height, width = img.shape[:2]
    center = (width/2, height/2)
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=angle, scale=1)
    rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))
    return rotated_image
