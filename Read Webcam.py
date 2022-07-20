# import the opencv library
import cv2
import time
# define a video capture object
print("Finding")
vid = cv2.VideoCapture(2)
vid.set(cv2.CAP_PROP_FPS, 10)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # set new dimensionns to cam object (not cap)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
print("Reading")

while True:

    # Capture the video frame
    # by frame
    t_start = time.time()
    ret, frame = vid.read()
    # frame = cv2.resize(frame, (1280, 720))
    # Display the resulting frame
    print(frame.shape)
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    print(time.time() - t_start)


# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
