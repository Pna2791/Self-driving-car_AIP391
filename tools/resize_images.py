import cv2
import numpy as np
import glob

# params setting
shape = (48, 27)
images_folder = "E:\Coding\Python\Learning\AIP391\data/train/3"
saving_folder = "E:\Coding\Python\Learning\AIP391\data/resized_train/2"
cnt = 0

# =============================================

if __name__ == "__main__":
    X, y = [], []
    paths = glob.glob(f"{images_folder}/*.png")
    for i, path in enumerate(paths):
        img = cv2.imread(path)
        img = cv2.resize(img, shape)
        cv2.imwrite(f"{saving_folder}/{str(cnt).zfill(5)}.png", img)
        cnt+=1
