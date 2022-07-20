import cv2
import glob

# params setting

read_from_video_or_images = "images"     # neither "video" or "images"
counting_start = 0
original_video_path = "data/original_video/traffic sign 2.mp4"
original_images_path = "D:\Desktop\AIP391\Lane detection\data/traffic signs data\90xxxx/"
save_images_path = "D:\Desktop\AIP391\Lane detection\data/traffic signs data\cleaned data/"

def naming(frame, index: int):
    cv2.imshow("frame",frame)
    while True:
        label = cv2.waitKey(0)
        print(chr(label))
        if label >= 49 and label <= 51:         # key set validation {1, 2, 3}
            cv2.imwrite(save_images_path+f"{str(index).zfill(5)}.png", frame)
            cv2.waitKey(100)  
            break
        if label == 120: 
            cv2.waitKey(100)                        # ignore bad frame : key_x
            break

def naming_from_images():
    image_paths = glob.glob(original_images_path+"*.png")
    cnt = counting_start
    for path in image_paths:
        cnt += 1
        frame = cv2.imread(path)
        # frame = cv2.flip(frame, 1)        # flip image
        naming(frame=frame, index=cnt)

def naming_from_videos():
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
        naming(frame=frame, index=cnt)
    cap.release()

if __name__=="__main__":
    if read_from_video_or_images=="video":
        naming_from_videos()
    elif read_from_video_or_images=="images":
        naming_from_images()
    