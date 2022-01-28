from tkinter import *
from time import strftime
from PIL import ImageTk, Image
from motion import movement
from facedetect import facedetect
from cam import cam
from both import both

def time():
    string = strftime('%H:%M:%S %p')
    t.config(text = string)
    t.after(1000, time)

window=Tk()

path5 = "/Users/computername/Desktop/Security-Python/images/log.png"
img5 = ImageTk.PhotoImage(Image.open(path5).resize((140,130)))
im5 = Label(window, image = img5)
im5.place(x=0,y=0)

lbl=Label(window, text="Security System", fg='brown', font=("Helvetica", 45,'bold'))
lbl.place(x=420, y=10)

t = Label(window, fg='black',font = ('calibri', 20, 'bold'))
t.place(x=1050, y=5)
time()

path = "/Users/computername/Desktop/Security-Python/images/SD 2.png"
img = ImageTk.PhotoImage(Image.open(path))
im = Label(window, image = img)
im.place(x=490,y=65)

lbl1=Label(window,text=" It is a camera security system that detects the motion of body and has features like face detection which automatically\ncaptures the scene along with timestamp, images and recordings.\nYou can choose from the following options available.", fg='black', font=("Arial", 17))
lbl1.place(x=160, y=200)

path1 = "/Users/computername/Desktop/Security-Python/images/cam.jpg"
img1 = ImageTk.PhotoImage(Image.open(path1).resize((200,180)))
btn1=Button(window, text="Camera" ,image=img1,command=cam)
btn1.place(x=200, y=290)

path2 = "/Users/computername/Desktop/Security-Python/images/mo.jpg"
img2 = ImageTk.PhotoImage(Image.open(path2).resize((200,180)))
btn2=Button(window, text="Motion", image=img2,command=movement)
btn2.place(x=500, y=290)

path3 = "/Users/computername/Desktop/Security-Python/images/det.png"
img3 = ImageTk.PhotoImage(Image.open(path3).resize((200,180)))
btn3=Button(window, text="Face Detection", image=img3,command=facedetect)
btn3.place(x=800, y=290)

path4 = "/Users/computername/Desktop/Security-Python/images/botg.jpg"
img4 = ImageTk.PhotoImage(Image.open(path4).resize((200,180)))
btn4=Button(window, text="Record", image=img4,command=both)
btn4.place(x=500, y=500)

t1 = Label(window,fg='brown',text='Camera Feed' ,font = ('calibri', 15,"italic"))
t1.place(x=195, y=280)

t2 = Label(window,fg='brown',text='Motion Detector' ,font = ('calibri', 15,"italic"))
t2.place(x=495, y=280)

t3 = Label(window,fg='brown',text='Face Detection' ,font = ('calibri', 15,"italic"))
t3.place(x=795, y=280)

t4 = Label(window,fg='brown',text='Auto-Record' ,font = ('calibri', 15,"italic"))
t4.place(x=500, y=490)

t4 = Label(window,fg='brown',text='🖥 After selecting the option press the escape button to close the camera window.',font = ('calibri', 11,"bold"))
t4.place(x=372, y=687)

window.title('Camera Security System')
window.geometry("1200x720")
window.minsize(1200,720)
window.maxsize(1200,720)
window.mainloop()
