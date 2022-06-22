from evaluating_model import *
from hought_transform import *
from sklearn.metrics import classification_report
import glob
import cv2

if __name__=="__main__":
    results = eval_model(test_dataset_path="data/test.csv")

    # frames_path = "D:/Desktop/AIP391/Lane detection/Frames/"
    # image_path = "D:/Desktop/AIP391/Lane detection/Frames/036840.png"
    # filenames = glob.glob(frames_path+"*.png")
    # # for i in range(570, 590):
    # #     img = cv2.imread(filenames[i])
    # #     process_image(img)
    # img = cv2.imread(image_path)
    # process_image(img)