import cv2
import time

def movement():
    cap = cv2.VideoCapture(0)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    f = time.ctime()

    #out = cv2.VideoWriter(str(f)+'.avi', cv2.VideoWriter_fourcc(
     #   'M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
    while True:
        _, frame1 = cap.read()
        _, frame2 = cap.read()

        diff = cv2.absdiff(frame2, frame1)
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        diff = cv2.blur(diff, (5, 5))
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        contr, _ = cv2.findContours(
            thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contr) > 28:
            ft = time.ctime()
            #max_cnt = max(contr, key=cv2.contourArea)
            #x,y,w,h = cv2.boundingRect(max_cnt)
            #cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)
            #cv2.putText(frame1, "MOTION DETECTED", (10, 80),
                        #cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
            cv2.putText(frame1, str(ft), (50,50), 2, 1, (0,255,0), 2, cv2.LINE_AA)


            #out.write(frame1)
            #for i in range(3):
             #   cv2.imwrite('opencv'+str(ft)+'.png', frame1)

        else:
            cv2.putText(frame1, "NO-MOTION", (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

        cv2.imshow("Motion Detection Frame", frame1)

        if cv2.waitKey(1) == 27:

            break

    cap.release()
    cv2.destroyAllWindows()
