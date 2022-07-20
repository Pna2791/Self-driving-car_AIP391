import enum
from turtle import RawTurtle
import numpy as np
import cv2
import torch

from models.common import DetectMultiBackend
from utils.augmentations import letterbox
from utils.general import (cv2, non_max_suppression)
from utils.torch_utils import select_device

@torch.no_grad()
class YOLO:
    def __init__(self, weights='yolov5s.pt',  # model.pt path(s)
                 imgsz=(640, 640),  # inference size (height, width)
                 conf_thres=0.25,  # confidence threshold
                 max_det=1000,  # maximum detections per image
                 device='',  # cuda device, i.e. 0 or 0,1,2,3 or cpu
                 ):
        self.weights = weights
        self.imgsz = imgsz
        self.conf_thres = conf_thres
        self.max_det = max_det
        self.device = select_device(device)

        self.model = DetectMultiBackend(weights)
        self.stride, self.names, self.pt = self.model.stride, self.model.names ,self.model.pt

        # self.model.warmup(imgsz=(1 if self.pt else 1, 3, *imgsz))  # warmup

    def predict(self, image):
        img = letterbox(image, self.imgsz, stride=self.stride)[0]
        # Convert
        img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        img = np.ascontiguousarray(img)

        im = img
        im = torch.from_numpy(im).to(self.device)
        im = im.half() if self.model.fp16 else im.float()  # uint8 to fp16/32
        im /= 255  # 0 - 255 to 0.0 - 1.0
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim
        
        pred = self.model(im)
        pred = non_max_suppression(pred, self.conf_thres, max_det=self.max_det)

        signs, windows = [], []
        for box in pred[0]:
            windows.append([int(box[0]), int(box[1]), int(box[2]), int(box[3])])
            signs.append(int(box[5]))
        return pred, signs, windows


model_path = "models/yolov5s_300_64_416x416px.pt"

if __name__ == "__main__":
    im = cv2.imread('D:\Desktop\AIP391\Lane detection\data/test/00341.png')
    yolov5 = YOLO(weights=model_path, imgsz=[416, 416], conf_thres=0.1)
    pred, sg, wds = yolov5.predict(im)

    ratio = max(im.shape)/416
    for i, box in enumerate(wds):
        for j in range(len(box)):
            box[j] = int(box[j]*ratio)
        cv2.rectangle(im, pt1=(box[2], box[3]), pt2=(box[0], box[1]), color=(255,0,0), thickness=2)

    cv2.imshow('image', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()