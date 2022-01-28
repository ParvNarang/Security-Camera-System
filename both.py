import cv2
import time

face_cascade = cv2.CascadeClassifier(
    "frontal_face.xml")

def both():
    cap = cv2.VideoCapture(0)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    f = time.ctime()
    out = cv2.VideoWriter(str(f)+'.avi', cv2.VideoWriter_fourcc(
        'M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
    out2 = cv2.VideoWriter('motion'+str(f)+'.avi', cv2.VideoWriter_fourcc(
        'M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
    

    while True:
        _, frame1 = cap.read()
        _, frame2 = cap.read()
        ret, img = cap.read()
        if ret == False:
            break

        diff = cv2.absdiff(frame2, frame1)
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        diff = cv2.blur(diff, (5, 5))
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        contr, _ = cv2.findContours(
            thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.21, 4)
        if len(contr) > 28:
            ft = time.ctime()
            #max_cnt = max(contr, key=cv2.contourArea)
            #x,y,w,h = cv2.boundingRect(max_cnt)
            #cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)
            #cv2.putText(frame1, "MOTION DETECTED", (10, 80),
                        #cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
            cv2.putText(frame1, str(ft), (50, 50), 2,
                        1, (0, 255, 0), 2, cv2.LINE_AA)
            out2.write(frame1)
            for i in range(3):
                cv2.imwrite('opencv'+str(ft)+'.png', frame1)
        else:
            cv2.putText(frame1, "NO-MOTION", (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

        for(x, y, w, h) in faces:
            ft = time.ctime()
            cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 15)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 15)
            cv2.putText(img, str(ft), (50, 50), 2, 1,
                        (0, 255, 0), 2, cv2.LINE_AA)
            out.write(img)
            for i in range(3):
                cv2.imwrite('opencv'+str(ft)+'.png', img)

            # out.write(frame1)
            # for i in range(3):
            #   cv2.imwrite('opencv'+str(ft)+'.png', frame1)


        cv2.imshow("Motion Detection", frame1)
        cv2.imshow('img', img)
        #cv2.imshow('hh', gray)

        key = cv2.waitKey(5)

        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
