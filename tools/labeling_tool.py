import cv2
import glob

# params setting
read_from_video_or_images = "images"
train_or_test = "train"
shape_frame = (640, 360)
original_video_path = "data/original_video/video 2.mp4"
start_point_couting = 18179

original_images_path = "data/raw_frames/"
labeling_saving_path = "data/"




#----------------------------------------------------------------------------------------------

def labeling(frame, index: int, shape : tuple[int, int]):
    image = cv2.resize(frame, shape)
    cv2.line(image, (0,shape[1]), (shape[0]//2,0), color=(255, 0, 0), thickness= 2)
    cv2.line(image, (shape[0], shape[1]), (shape[0]//2,0), color=(255, 0, 0), thickness= 2)
    cv2.line(image, (0,shape[1]), (shape[0]//4,0), color=(0 , 255, 255), thickness= 1)
    cv2.line(image, (shape[0], shape[1]), (shape[0]//4,0), color=(0 , 255, 255), thickness= 1)
    cv2.line(image, (0,shape[1]), (shape[0]*3//4,0), color=(0 , 255, 255), thickness= 1)
    cv2.line(image, (shape[0], shape[1]), (shape[0]*3//4,0), color=(0 , 255, 255), thickness= 1)
    cv2.imshow("frame",image)
    while True:
        label = cv2.waitKey(0)
        if label >= 49 and label <= 51:         # key set validation {1, 2, 3}
            frame = cv2.resize(frame, shape)
            cv2.imwrite(labeling_saving_path+f"{train_or_test}/{label-48}/{str(index).zfill(6)}.png", frame)
            break
        if label == 120:                         # ignore bad frame : key_x
            break

def labeling_from_video(counting_start : int):
    cap = cv2.VideoCapture(original_video_path)
    print(cap.get(cv2.CAP_PROP_FPS))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cnt = counting_start
    while True:
        ret, frame = cap.read()
        if not ret: 
            break
        cnt += 1
        labeling(frame=frame, index=cnt, shape=shape_frame)
    cap.release()

def labeling_from_images(counting_start : int):
    image_paths = glob.glob("data/raw_frames/*.png")
    cnt = counting_start
    for path in image_paths:
        cnt += 1
        frame = cv2.imread(path)
        # frame = cv2.flip(frame, 1)        # flip image
        labeling(frame=frame, index=cnt, shape=shape_frame)

if __name__=="__main__":
    if read_from_video_or_images=="video":
        labeling_from_video(start_point_couting)
    if read_from_video_or_images=="images":
        labeling_from_images(start_point_couting)   