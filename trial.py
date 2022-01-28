from motion import movement
from facedetect import facedetect
from cam import cam
from both import both
import time

u = input("enter = ")
#current_time = time.strftime("%H:%M:%S", )
while True:
    f = time.ctime()
    print(f)
    if u == "a":
        a = int(f[11:13])
        if a > 18 or a > 8:
            movement()
            break
        else:
            print("not")
            break
    if u == "b":
        a = int(f[11:13])
        if a > 18 or a > 8:
            facedetect()
            break
        else:
            print("not")
            break
    if u == "c":
        cam()
        break
    if u == "x":
        both()
        break
    if u == "e":
        movement()
        facedetect()
        break
    if u == "d":
        break
