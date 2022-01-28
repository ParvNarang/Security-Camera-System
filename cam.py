import cv2
import time

def cam():
    cap = cv2.VideoCapture(0)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    if not (cap.isOpened()):
        print("Could not open video device:")

    while True:
        ret, img = cap.read()
        if ret == False:
            break

        cv2.imshow('Camera Feed', img)

        key = cv2.waitKey(5)

        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
