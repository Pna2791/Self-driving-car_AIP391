import cv2
# from tkinter import * 

original_video_path = "D:\Desktop\AIP391\Lane detection/video 1.mp4"
labeling_saving_path = "D:/Desktop/AIP391/Lane detection/data/"


def labeling(frame, index: int):
    image = cv2.resize(frame, (1080, 608))
    cv2.line(image, (0,608), (540,0), color=(255, 0, 0), thickness= 2)
    cv2.line(image, (1080, 608), (540,0), color=(255, 0, 0), thickness= 2)
    cv2.line(image, (0,608), (280,0), color=(0 , 255, 255), thickness= 1)
    cv2.line(image, (1080, 608), (280,0), color=(0 , 255, 255), thickness= 1)
    cv2.line(image, (0,608), (820,0), color=(0 , 255, 255), thickness= 1)
    cv2.line(image, (1080, 608), (820,0), color=(0 , 255, 255), thickness= 1)
    cv2.imshow("frame",image)
    while True:
        label = cv2.waitKey(0)
        if not (label < 49 and label > 51):
            frame = cv2.resize(frame, (720, 405))
            cv2.imwrite(labeling_saving_path+f"{label-48}-test/{str(index).zfill(5)}.png", frame)
            break

if __name__=="__main__":
    cap = cv2.VideoCapture(original_video_path)
    print(cap.get(cv2.CAP_PROP_FPS))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    cnt = 0
    while True:
        ret, frame = cap.read()
        if not ret: 
            break
        cap.read()
        cap.read()
        cnt += 3
        labeling(frame=frame, index=cnt)

    cap.release()