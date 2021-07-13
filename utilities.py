from tkinter import *
from tkinter.messagebox import *
from PIL import Image
import time
import winsound
global secs_counter
global mins_counter
global hours_counter
secs_counter = 0
mins_counter = 0
hours_counter = 0
def alarm():
    print("alarm")

def timer():
    userText = False
    def userText(event):
        number_entry.delete(0 , END)
        usercheck = TRUE
    
    def back1():
        timer_frame.destroy()
        
    def timer1(timer):
        timer = int(timer)
        timer*=60
        freq = 1000
        dur = 4000
        for i in range(1,timer):
            print(i)
            time.sleep(1)
        else:
            winsound.Beep(freq, dur)
    
    print("timer")
    timer_frame = Frame(c, bg = "cyan")
    timer_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

    number_entry = Entry(timer_frame)
    number_entry.insert(0 , "Number of minutes")
    number_entry.bind("<Button>", userText)
    number_entry.place(relx = 0.32 , rely = 0.4)

    timer_start = Button(timer_frame ,text = "Start timer"  ,command = lambda : timer1(number_entry.get()))
    timer_start.place(relx = 0.48 , rely = 0.395)

    back = Button(timer_frame , text = "< Back" , command = lambda : back1())
    back.place(relx = 0 , rely = 0)
    
def stopwatch():
    global secs_counter
    global mins_counter
    global hours_counter

    def stopstop():
        global secs_counter
        global mins_counter
        global hours_counter
        secs_counter = 0
        mins_counter = 0
        hours_counter = 0
        
    def back2():
        global secs_counter
        global mins_counter
        global hours_counter
        stopwatch_frame.destroy()
        secs_counter = 0
        mins_counter = 0
        hours_counter = 0
        
    def stopwa(): 
        def counter(label1 , label2 , label3):
            def count():
                 global secs_counter
                 global mins_counter
                 global hours_counter
                 if(True):
                     if(secs_counter>58):
                         secs_counter = 1
                         label1.config(text=str(secs_counter))
                         label1.after(1000, count)
                         if(mins_counter>58):
                             mins_counter=0
                             hours_counter+=1
                             label2.config(text=str(mins_counter))
                             label3.config(text = str(hours_counter))
                         else:
                             mins_counter+=1
                             label2.config(text=str(mins_counter))
                     else:
                         secs_counter+=1
                         label1.config(text=str(secs_counter))
                         label1.after(1000, count)
            count()
        seconds_label = Label(stopwatch_frame , text = "0")
        seconds_label.place(relx = 0.65 , rely = 0.3 , relwidth = 0.1  , relheight = 0.1)
        seco = Label(stopwatch_frame , text = "secs")
        seco.place(relx = 0.76 , rely = 0.356)

        minutes_label = Label(stopwatch_frame , text = "0")
        minutes_label.place(relx = 0.45 , rely = 0.3 , relwidth = 0.1  , relheight = 0.1)
        min = Label(stopwatch_frame , text = "mins")
        min.place(relx = 0.56 , rely = 0.356)
        
        hours_label = Label(stopwatch_frame , text = "0")
        hours_label.place(relx = 0.25 , rely = 0.3 , relwidth = 0.1  , relheight = 0.1)
        hr = Label(stopwatch_frame , text = "hrs")
        hr.place(relx = 0.36 , rely = 0.356)

        restart_button = Button(stopwatch_frame ,text = "Restart Stopwatch" , command = lambda: stopstop())
        restart_button.place(relx = 0.444 , rely = 0.6)

        counter(seconds_label , minutes_label , hours_label)


    print("stopwatch")
    stopwatch_frame = Frame(c, bg = "cyan")
    stopwatch_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

    start_button = Button(stopwatch_frame ,text = "Start Stopwatch" , command = lambda: stopwa())
    start_button.place(relx = 0.444 , rely = 0.6)

    back = Button(stopwatch_frame , text = "< Back" , command = lambda : back2())
    back.place(relx = 0 , rely = 0)

def convertor():
    print("convertor")

def notes():
    print("notes")

root = Tk()
root.title("Utilities")
c = Canvas(root, width = "850" , height = "500")
c.pack()

frame_head = Frame(c)
frame_head.place(relx = 0, rely = 0 , relwidth =1 , relheight = 0.1)

p1= PhotoImage(file="Utilities_logo1.png")
bglabel1=Label(frame_head, image=p1)
bglabel1.place(relx = 0.35 , rely = 0.05)

label_for_title = Label(frame_head, text = "Utilities" )
label_for_title.place(relx = 0.41 , rely = 0.16 , relwidth = 0.1 , relheight = 0.7)
##########################################################################################

frame_body = Frame(c, bg = "cyan")
frame_body.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

p2= PhotoImage(file="alarm_logo1.png")
bglabel2=Label(frame_body, image=p2)
bglabel2.place(relx = 0.12 , rely = 0.11)
l2 = Button(frame_body, text = "ALARM" , command = lambda: alarm())
l2.place(relx = 0.14 , rely = 0.35)

p3= PhotoImage(file="Timer_logo.png")
bglabel3=Label(frame_body, image=p3)
bglabel3.place(relx = 0.42 , rely = 0.11)
l3=Button(frame_body, text = "TIMER" , command = lambda: timer())
l3.place(relx = 0.443, rely = 0.35)

p4= PhotoImage(file="stopwatch_logo.png")
bglabel4=Label(frame_body, image=p4)
bglabel4.place(relx = 0.7  ,rely = 0.11)
l4=Button(frame_body, text = "STOPWATCH" , command = lambda: stopwatch())
l4.place(relx = 0.7134 , rely = 0.35)

p5= PhotoImage(file="convertor_logo.png")
bglabel5=Label(frame_body, image=p5)
bglabel5.place(relx = 0.257 , rely = 0.5)
l5=Button(frame_body, text = "CONVERTOR" , command = lambda: convertor())
l5.place(relx = 0.273 , rely = 0.74)

p6= PhotoImage(file="notes_logo.png")
bglabel6=Label(frame_body, image=p6)
bglabel6.place(relx = 0.6 , rely = 0.5)
l6=Button(frame_body, text = "NOTES", command = lambda: notes())
l6.place(relx = 0.624 , rely = 0.74)
    

root.resizable(0,0)
root.mainloop()





