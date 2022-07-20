import cv2
import numpy as np
import glob
import pandas as pd
from sklearn.model_selection import train_test_split
import csv

# params setting
data_reading_path = "D:\Desktop\AIP391\Lane detection\data/traffic signs data/50x50 bboxs/"
resize_step = False
num_of_classes = 26
shape_resized = (50, 50)
train_or_test = "train"


#----------------------------------------------------------------------------------------------

def creating_csv(filename: str, x_set, y_set, shape : tuple[int, int]):
    #creating header
    header = ['label']
    for i in range(3*shape_resized[0]*shape_resized[1]): header.append(f"px{i}")
    data = pd.DataFrame(columns= header)
    for i in range(len(x_set)):
        print(i)
        row = [y_set[i]]
        image = cv2.imread(x_set[i])
        if resize_step:
            image = cv2.resize(image, shape)
        # image = np.asfarray(image)
        image = np.reshape(image, (-1))
        for value in image:
            row.append(value)    
        data.loc[i] = row

    data.to_csv(data_reading_path+filename+".csv", index=False,)

if __name__ == "__main__":
    X, y = [], []
    for i in range(num_of_classes):
        x_arr = glob.glob(data_reading_path+f"{train_or_test}/{str(i)}/*.png")
        y_arr = np.ones(len(x_arr))*i
        X = np.append(X, x_arr)
        y = np.append(y, y_arr)

    print(f"total image: {len(X)}")
    if train_or_test=="train":
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
        creating_csv("train", X_train, y_train, shape=shape_resized)
        creating_csv("validation", X_val, y_val, shape=shape_resized)
    if train_or_test=="test":
        creating_csv("test", X, y, shape=shape_resized)
    
