from time import time as millis
import numpy as np
import torch
from utils.augmentations import letterbox
from models.common import DetectMultiBackend
from utils.general import (check_img_size, non_max_suppression)


class YOLO:
    class_label = ['Bien giam toc--yeild-', 'Den do', 'Den giao thong', 'Den vang', 'Di Thang', 'Duong cam', 'Stop', 'canh bao queo phai', 'canh bao queo trai', 'den xanh', 'duoc queo phai', 'duong uu tien', 'end limit 30km-h', 'end limit 40km-h', 'end limit 50km-h', 'end limit 60km-h', 'end limit 70km-h', 'end limit 80km-h', 'gioi han toc do 10km-h', 'gioi han toc do 120km-h', 'gioi han toc do 20km-h', 'gioi han toc do 30km-h', 'gioi han toc do 40km-h', 'gioi han toc do 50km-h', 'gioi han toc do 60km-h', 'gioi han toc do 70km-h', 'gioi han toc do 80km-h', 'gioi han toc do 90km-h', 'limit 5km-h', 'min limit 20km-h', 'min limit 40km-h', 'min limit 60km-h', 'queo trai', 'slow']

    def __init__(self,
                 imgsz=(416, 416),
                 weights='yolov5s_300_64_416x416px.pt',  # model.pt path(s)
                 data='data/coco128.yaml',  # dataset.yaml path

                 augment=False,  # augmented inference
                 conf_thres=0.25,  # confidence threshold
                 iou_thres=0.45,  # NMS IOU threshold
                 max_det=1000,  # maximum detections per image

                 classes=None, # filter by class: --class 0, or --class 0 2 3
                 agnostic_nms=False,  # class-agnostic NMS

                 half=False,  # use FP16 half-precision inference
                 dnn=False,  # use OpenCV DNN for ONNX inference
                 ):
        self.augment = augment
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.classes = classes
        self.agnostic_nms = agnostic_nms
        self.max_det = max_det

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = DetectMultiBackend(weights, device=self.device, dnn=dnn, data=data, fp16=half)
        self.stride, names, self.pt = self.model.stride, self.model.names, self.model.pt
        imgsz = check_img_size(imgsz, s=self.stride)  # check image size

        self.model.warmup(imgsz=(1 if self.pt else 1, 3, *imgsz))
        self.img_size = imgsz


    def resize(self, img0):
        img = letterbox(img0, self.img_size, stride=self.stride, auto=self.pt)[0]
        img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        img = np.ascontiguousarray(img)
        return img

    def predict(self, img):
        t_start = millis()

        im = self.resize(img)
        im = torch.from_numpy(im).to(self.device)
        im = im.half() if self.model.fp16 else im.float()  # uint8 to fp16/32
        im /= 255  # 0 - 255 to 0.0 - 1.0
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim

        # 384*640
        predictions = self.model(im, augment=self.augment)
        predictions = non_max_suppression(predictions, self.conf_thres, self.iou_thres, self.classes, self.agnostic_nms, max_det=self.max_det)[0]

        # yield len(predictions)
        yield predictions

        # result = []
        # for pred in predictions:
        #     # x1 = pred[0] - pred[2]/2
        #     # x2 = pred[0] + pred[2]/2
        #     # y1 = pred[1] - pred[3]/2
        #     # y2 = pred[1] + pred[3]/2
        #     # result.append([x1, y1, x2, y2])
        #     result.append([pred[0], pred[1], pred[2], pred[3]])
        #
        # yield result
        yield millis() - t_start

