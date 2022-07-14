from detect_model import YOLO
import cv2


def draw_box(img, boxes):
    red = (0, 0, 255)
    for box in boxes:
        start_point = (int(box[0]), int(box[1]*0.9375))
        end_point = (int(box[2]), int(box[3]*0.9375))
        # start_point = (int(width*box[0]), int(width*box[1]))
        # end_point = (int(width*box[2]), int(width*box[3]))
        img = cv2.rectangle(img, start_point, end_point, red, thickness=1)
    return img


# img = cv2.imread('traffic_sign/02845.png')
img = cv2.imread('data/l4/00000.png')
model = YOLO(imgsz=(640, 640), weights='best.pt')


pred, dura = model.predict(img)
print(dura, pred)

frame = draw_box(img, pred)
cv2.imshow('frame', frame)

cv2.waitKey()
cv2.destroyAllWindows()
