from detect_model import YOLO
# import keras
# import numpy as np
# import time
import cv2


input_shape = (64, 36)
height, width, fps_set = 360, 640, 10
preview_size = (width, height)


print('Camera starting...')
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

camera.set(cv2.CAP_PROP_FPS, fps_set)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
print('Camera running')

model = YOLO(imgsz=(640, 640), weights='best.pt')


def save_video(img, ind):
    path = 'data/l4/' + '{:0>5d}'.format(ind) + '.png'
    cv2.imwrite(path, img)


def draw_box(img, boxes):
    red = (0, 0, 255)
    for box in boxes:
        start_point = (int(box[0]), int(box[1]*0.9375))
        end_point = (int(box[2]), int(box[3]*0.9375))
        # start_point = (int(width*box[0]), int(width*box[1]))
        # end_point = (int(width*box[2]), int(width*box[3]))
        img = cv2.rectangle(img, start_point, end_point, red, thickness=1)
    return img


def crop_images(img, boxes, img_size):
    imgs = []
    for box in boxes:
        d_height    = box[3] - box[1]
        d_width     = box[2] - box[0]

        x1 = int(box[0] - 0.1*d_width)
        x2 = int(box[2] + 0.1*d_width)
        y1 = int(box[1] - 0.1*d_height)
        y2 = int(box[3] + 0.1*d_height)

        if x1 < 0:      x1 = 0
        if x2 > width:  x2 = width
        if y1 < 0:      y1 = 0
        if y2 > height: y2 = height

        crop_img = img[y1:y2, x1:x2]
        crop_img = cv2.resize(crop_img, img_size)

        imgs.append(crop_img)

    return imgs


def draw_grid(img):
    blue = (255, 0, 0)
    img = cv2.line(img, (int(width / 2), 0), (int(width / 2), height), blue, 1)
    img = cv2.line(img, (int(width * 0.3), int(height / 2)), (int(width * 0.7), int(height / 2)), blue, 1)
    img = cv2.line(img, (int(width * 0.3), int(height / 3)), (int(width * 0.7), int(height / 3)), blue, 1)
    img = cv2.line(img, (0, int(height * 2 / 3)), (width, int(height * 2 / 3)), blue, 1)

    img = cv2.line(img, (int(width * 0.5), 0), (int(width * 0.2), height), blue, 1)
    img = cv2.line(img, (int(width * 0.5), 0), (int(width * 0.8), height), blue, 1)

    img = cv2.line(img, (int(width * 0.5), int(height * 0)), (int(width * 0.1), height), blue, 1)
    img = cv2.line(img, (int(width * 0.5), int(height * 0)), (int(width * 0.9), height), blue, 1)
    return img


ind = 0
while True:
    ret, frame = camera.read()
    pred, dura = model.predict(frame)
    print(dura, pred)

    # save_video(frame, ind)
    # frame = draw_grid(frame)
    frame = draw_box(frame, pred)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ind += 1


camera.release()
cv2.destroyAllWindows()
