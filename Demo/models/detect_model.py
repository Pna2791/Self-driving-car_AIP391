from time import time as millis
import numpy as np
import torch
import cv2
from utils.augmentations import letterbox
from models.common import DetectMultiBackend
from utils.general import (check_img_size, non_max_suppression)
import keras


class YOLO:
    class_label = ['Bien giam toc--yeild-', 'Den do', 'Den giao thong', 'Den vang', 'Di Thang', 'Duong cam', 'Stop', 'canh bao queo phai', 'canh bao queo trai', 'den xanh', 'duoc queo phai', 'duong uu tien', 'end limit 30km-h', 'end limit 40km-h', 'end limit 50km-h', 'end limit 60km-h', 'end limit 70km-h', 'end limit 80km-h', 'gioi han toc do 10km-h', 'gioi han toc do 120km-h', 'gioi han toc do 20km-h', 'gioi han toc do 30km-h', 'gioi han toc do 40km-h', 'gioi han toc do 50km-h', 'gioi han toc do 60km-h', 'gioi han toc do 70km-h', 'gioi han toc do 80km-h', 'gioi han toc do 90km-h', 'limit 5km-h', 'min limit 20km-h', 'min limit 40km-h', 'min limit 60km-h', 'queo trai', 'slow']

    def __init__(self,
                 input_resolution=(640, 360),
                 output_resolution=(25, 25),
                 imgsz=(640, 640),
                 weights='yolov5s_300_64_416x416px.pt',  # model.pt path(s)

                 augment=False,  # augmented inference
                 conf_thres=0.25,  # confidence threshold
                 iou_thres=0.45,  # NMS IOU threshold
                 max_det=1000,  # maximum detections per image

                 classes=None, # filter by class: --class 0, or --class 0 2 3
                 agnostic_nms=False,  # class-agnostic NMS

                 half=False,  # use FP16 half-precision inference
                 dnn=False,  # use OpenCV DNN for ONNX inference
                 ):
        self.input_shape = input_resolution
        self.output_shape = output_resolution
        self.area_min = output_resolution[0]*output_resolution[1]

        self.augment = augment
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.classes = classes
        self.agnostic_nms = agnostic_nms
        self.max_det = max_det

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = DetectMultiBackend(weights, device=self.device, dnn=dnn, fp16=half)
        self.stride, names, self.pt = self.model.stride, self.model.names, self.model.pt
        imgsz = check_img_size(imgsz, s=self.stride)  # check image size

        self.model.warmup(imgsz=(1 if self.pt else 1, 3, *imgsz))
        self.img_size = imgsz
        self.scale_ratio = (input_resolution[0]/imgsz[0], input_resolution[0]/imgsz[0])
        # self.scale_ratio = (input_resolution[0]/imgsz[0], input_resolution[1]/384)
        # self.scale_ratio = (3, 3)
        print(imgsz, self.scale_ratio)

    def resize(self, img0):
        img = letterbox(img0, self.img_size, stride=self.stride, auto=self.pt)[0]
        img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        img = np.ascontiguousarray(img)
        return img

    def predict(self, img):
        im = self.resize(img)

        im = torch.from_numpy(im).to(self.device)
        im = im.half() if self.model.fp16 else im.float()  # uint8 to fp16/32
        im /= 255  # 0 - 255 to 0.0 - 1.0
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim

        # print(im.shape)
        # 384*640
        predictions = self.model(im, augment=self.augment)
        predictions = non_max_suppression(predictions, self.conf_thres, self.iou_thres, self.classes, self.agnostic_nms, max_det=self.max_det)[0]

        boxes = []
        for pred in predictions:
            x1 = int(pred[0]*self.scale_ratio[0])
            y1 = int(pred[1]*self.scale_ratio[1])
            x2 = int(pred[2]*self.scale_ratio[0])
            y2 = int(pred[3]*self.scale_ratio[1])
            boxes.append([x1, y1, x2, y2, round(float(pred[4]), 2)])

        return boxes

    def crop_images(self, img, boxes, top=0):
        red = (0, 0, 255)
        width, height = self.input_shape
        imgs = []
        # frame = img
        padding = 0.05
        valid_boxes = []
        for box in boxes:
            d_height    = box[3] - box[1]
            d_width     = box[2] - box[0]

            x1 = int(box[0] - padding*d_width)
            x2 = int(box[2] + padding*d_width)
            y1 = int(box[1] - padding*d_height)
            y2 = int(box[3] + padding*d_height)

            if x1 < 0:      x1 = 0
            if x2 > width:  x2 = width
            if y1 < 0:      y1 = 0
            if y2 > height: y2 = height

            box_area = (x1-x2)*(y1-y2)
            # frame = cv2.rectangle(img, (x1, y1), (x2, y2), red, thickness=3)
            # frame = cv2.putText(frame, str(box[4]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, red, 2, cv2.LINE_AA,)
            if box_area >= self.area_min:
                crop_img = img[y1:y2, x1:x2]
                crop_img = cv2.resize(crop_img, self.output_shape)
                imgs.append(crop_img)
                valid_boxes.append([(x1, y1+top), (x2, y2+top)])

        return valid_boxes, np.array(imgs)


class CNN:
    # class_names = ['cam di nguoc chieu', 'yellow light', 'duong cam', 'green light', 'limit 100', 'limit 20', 'limit 40', 'limit 50', 'limit 60', 'limit 70', 'limit 80', 'unlimit 70', 'min 20', 'min 40', 'min 60', 're trai', 'red light', 'slow', 'stop', 'unlimit 40', 'unlimit 50', 'unlimit 60']
    class_names = ['cam di nguoc chieu', 'duong cam', 'slow', 'stop', 'red light', 'yellow light', 'green light', 'limit 20', 'limit 40', 'limit 50', 'limit 60', # 10
                   'limit 70', 'limit 80', 'limit 90', 'limit 100', 'min 20', 'min 40', 'min 60', 'min 80', 'turn left', 'turn right', 'unlimit 40', 'unlimit 50',        # 21
                   'unlimit 60', 'unlimit 70', 'unlimit all']

    def __init__(self,
                 input_shape=(25, 25),
                 conf_thres=0.5,
                 scale=False,
                 weights='weights/model-31x31.h5'
                 ):
        self.conf_thres = conf_thres
        self.model = keras.models.load_model(weights)

    def predict(self, imgs):
        predictions = self.model.predict(imgs)
        indexes = np.argmax(predictions, axis=1)

        thres = []
        names = []
        for ind, pred in zip(indexes, predictions):
            th = pred[ind]
            if th >= self.conf_thres:
                thres.append(round(pred[ind], 2))
                names.append(self.class_names[ind])

        return thres, indexes

