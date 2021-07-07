from tkinter import *
from tkinter.messagebox import *
from PIL import Image


def alarm():
    print("ok")



root = Tk()
root.title("Utilities")
c = Canvas(root, width = "850" , height = "500")
c.pack()

frame_head = Frame(c)
frame_head.place(relx = 0, rely = 0 , relwidth =1 , relheight = 0.1)

p1= PhotoImage(file="Utilities_logo1.png")
bglabel1=Label(frame_head, image=p1)
bglabel1.place(relx = 0.35 , rely = 0.05)

label_for_title = Label(frame_head, text = "Utilities")
label_for_title.place(relx = 0.4 , rely = 0 , relwidth = 0.1 , relheight = 1)
##########################################################################################

frame_body = Frame(c, bg = "cyan")
frame_body.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

frame_for_alarm = Button(frame_body ,height = 10 , width = 30 , command = lambda: alarm())
frame_for_alarm.place(relx = 0.02 , relwidth = 0.3 , relheight = 0.4 , rely = 0.04)
p2= PhotoImage(file="alarm_logo1.png")
bglabel2=Label(frame_for_alarm, image=p2)
bglabel2.pack()
l2=Label(frame_for_alarm, text = "ALARM")
l2.place(relx = 0.405 , rely = 0.6)

frame_for_timer = Button(frame_body ,height = 10 , width = 30)
frame_for_timer.place(relx = 0.35 , relwidth = 0.3 , relheight = 0.4 , rely = 0.04)
p3= PhotoImage(file="Timer_logo.png")
bglabel3=Label(frame_for_timer, image=p3)
bglabel3.pack()
l3=Label(frame_for_timer, text = "TIMER")
l3.place(relx = 0.42 , rely = 0.6)

frame_for_stopwatch = Button(frame_body ,height = 10 , width = 30)
frame_for_stopwatch.place(relx = 0.67 , relwidth = 0.3 , relheight = 0.4 , rely = 0.04)
p4= PhotoImage(file="stopwatch_logo.png")
bglabel4=Label(frame_for_stopwatch, image=p4)
bglabel4.pack()
l4=Label(frame_for_stopwatch, text = "STOPWATCH")
l4.place(relx = 0.35 , rely = 0.6)

frame_for_convertor = Button(frame_body ,height = 10 , width = 30)
frame_for_convertor.place(relx = 0.17 , relwidth = 0.3 , relheight = 0.4 , rely = 0.5)
p5= PhotoImage(file="convertor_logo.png")
bglabel5=Label(frame_for_convertor, image=p5)
bglabel5.pack()
l5=Label(frame_for_convertor, text = "CONVERTOR")
l5.place(relx = 0.35 , rely = 0.6)

frame_for_notes = Button(frame_body ,height = 10 , width = 30)
frame_for_notes.place(relx = 0.55 , relwidth = 0.3 , relheight = 0.4 , rely = 0.5)
p6= PhotoImage(file="notes_logo.png")
bglabel6=Label(frame_for_notes, image=p6)
bglabel6.pack()
l6=Label(frame_for_notes, text = "NOTES")
l6.place(relx = 0.41 , rely = 0.6)


root.resizable(0,0)
root.mainloop()

