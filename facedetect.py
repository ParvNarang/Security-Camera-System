import cv2
import time

face_cascade = cv2.CascadeClassifier(
    "frontal_face.xml")


def facedetect():
    cap = cv2.VideoCapture(0)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    f = time.ctime()

    #out = cv2.VideoWriter(str(f)+'.avi', cv2.VideoWriter_fourcc(
     #   'M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

    if not (cap.isOpened()):
        print("Could not open video device:")

    while True:
        ret, img = cap.read()
        if ret == False:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.21, 4)

        for(x, y, w, h) in faces:
            ft = time.ctime()
            cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 15)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 15)
            cv2.putText(img, str(ft), (50,50), 2, 1, (0,255,0), 2, cv2.LINE_AA)
            #out.write(img)
            #for i in range(3):
             #   cv2.imwrite('opencv'+str(ft)+'.png', img)

        cv2.imshow('Coloured', img)
        cv2.imshow('GrayScale',gray)

        key = cv2.waitKey(5)

        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
