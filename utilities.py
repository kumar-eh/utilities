from tkinter import *
from tkinter.messagebox import *
from PIL import Image
import time
import winsound
import mysql.connector
from tkinter import messagebox
from datetime import datetime

global c1
global c2
global c3
global c4
global c5
global c6
global secs_counter
global mins_counter
global hours_counter
secs_counter = 0
mins_counter = 0
hours_counter = 0

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "root"
)
my_cur = mydb.cursor()
my_cur.execute("Create database if not exists utility")
my_cur.execute("use utility")
my_cur.execute("Create table if not exists todo(note char(255))")
my_cur.execute("Create table if not exists alarm(hr integer(11) , min integer(11))")
mydb.commit()
####################################################################################################################################################################################
def alarm():
    def back11():
        alarm_frame.destroy()
    userText = False
    def userText1(event):
        alarm_entry_hr.delete(0 , END)
        usercheck = TRUE
    def userText2(event):
        alarm_entry_min.delete(0 , END)
        usercheck = TRUE
    def add_alarm(hr , min , alarm_frame):
        def alar():                
            freq = 1000
            dur = 500
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            my_cur.execute("Select * from alarm")
            a1 = my_cur.fetchall()
            for i in a1:
                if(i[0] == datetime.now().hour and i[1] == datetime.now().minute):
                    hr1 = str(i[0])
                    min1 = str(i[1])
                    for j in range(0, 4):    
                        winsound.Beep(freq, dur)
                        my_cur.execute("Delete from alarm where hr = %s and min = %s " %(hr1 , min1))
                        mydb.commit()
                        alarm_frame.destroy()
                        
            time.sleep(1)
            alar()
        try:
            hr = int(hr)
            min = int(min)
            if(hr>24 or hr<0 or min>60 or min<0):
                messagebox.showwarning("Alert" , "Enter a valid time")
                return
            my_cur.execute("Insert into alarm (hr , min) values ('%s' ,'%s')" %(hr , min))
            mydb.commit()
            alar()

        except ValueError:
            messagebox.showwarning("ALert" , "Dont leave a field blank")
            
    alarm_frame = Frame(c, bg = "cyan")
    alarm_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

    eg_label = Label(alarm_frame , text = "Enter in 24 hr format eg.(23hr 20min)")
    eg_label.pack()

    alarm_entry_hr = Entry(alarm_frame)
    alarm_entry_hr.insert(0 , "Enter hr here")
    alarm_entry_hr.bind("<Button>", userText1)
    alarm_entry_hr.place(rely = 0.2 , relx = 0.42)

    alarm_entry_min = Entry(alarm_frame)
    alarm_entry_min.insert(0 , "Enter min here")
    alarm_entry_min.bind("<Button>", userText2)
    alarm_entry_min.place(relx = 0.42 , rely = 0.3)

    submit_butt = Button(alarm_frame , text = "Add alarm" ,command = lambda: add_alarm(alarm_entry_hr.get() , alarm_entry_min.get() , alarm_frame) )
    submit_butt.place(relx = 0.45, rely = 0.4)

    back = Button(alarm_frame , text = "< Back" , command = lambda : back11())
    back.place(relx = 0 , rely = 0)
####################################################################################################################################################################################
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
            time.sleep(1)
        else:
            winsound.Beep(freq, dur)
    
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
####################################################################################################################################################################################
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

    stopwatch_frame = Frame(c, bg = "cyan")
    stopwatch_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

    start_button = Button(stopwatch_frame ,text = "Start Stopwatch" , command = lambda: stopwa())
    start_button.place(relx = 0.444 , rely = 0.6)

    back = Button(stopwatch_frame , text = "< Back" , command = lambda : back2())
    back.place(relx = 0 , rely = 0)
####################################################################################################################################################################################
def convertor():
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    def back4():
        con_frame.destroy()
        
    def bmi():
        def back5():
            bmi_frame.destroy()
            
        def calc_bmi(wt , ht , bmi_label):
            bmi_label.delete(0, 'end')
            ht = int(ht)
            ht*=ht
            bmi= (int(wt)/int(ht))*10000
            bmi_label.insert(1, str(bmi))
            
        bmi_frame = Frame(c, bg = "cyan")
        bmi_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

        wt_entry = Entry(bmi_frame)
        wt_entry.place(relx = 0.45 , rely = 0.2)

        wt_label = Label(bmi_frame , text = "Enter weight in kg")
        wt_label.place(relx = 0.3 , rely = 0.2)

        ht_entry = Entry(bmi_frame)
        ht_entry.place(relx = 0.45 , rely = 0.3)

        ht_label = Label(bmi_frame , text = "Enter height in cm")
        ht_label.place(relx = 0.3 , rely = 0.3)
        
        bmi_label1 = Label(bmi_frame , text = "Your BMI")
        bmi_label1.place(relx = 0.3 , rely = 0.5)
        
        bmi_label = Entry(bmi_frame)
        bmi_label.place(relx = 0.45 , rely = 0.5)
        
        back = Button(bmi_frame , text = "< Back" , command = lambda : back5())
        back.place(relx = 0 , rely = 0)
        
        submit_butt = Button(bmi_frame , text = "Submit" ,command = lambda: calc_bmi(wt_entry.get(), ht_entry.get(), bmi_label) )
        submit_butt.place(relx = 0.4 , rely = 0.4)

    def dis():
        def back6():
            dis_frame.destroy()
        def calc_dis(op , per , dis_label):
            op = float(op)
            per = float(per)
            discount = op*(per/100)
            dis_label.delete(0 , 'end')
            dis_label.insert(1 , str(discount))

        dis_frame = Frame(c, bg = "cyan")
        dis_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

        op = Entry(dis_frame)
        op.place(relx = 0.45 , rely = 0.2)

        op_label = Label(dis_frame , text = "Enter original price")
        op_label.place(relx = 0.3 , rely = 0.2)

        percenta = Entry(dis_frame)
        percenta.place(relx = 0.45 , rely = 0.3)

        per_label = Label(dis_frame , text = "Enter discount %")
        per_label.place(relx = 0.3 , rely = 0.3)

        dis_label1 = Label(dis_frame , text = "Amount discounted")
        dis_label1.place(relx = 0.3 , rely = 0.5)
        
        dis_label = Entry(dis_frame)
        dis_label.place(relx = 0.45 , rely = 0.5)
        
        back = Button(dis_frame , text = "< Back" , command = lambda : back6())
        back.place(relx = 0 , rely = 0)

        submit_butt = Button(dis_frame , text = "Submit" ,command = lambda: calc_dis(op.get(), percenta.get(), dis_label))
        submit_butt.place(relx = 0.4 , rely = 0.4)        

    def length():
        def back7():
            len_frame.destroy()
            
        def calc_len(cm , m_entry , feet_entry , mm_entry):
            cm = float(cm)
            feet = cm*0.328
            m = cm*0.01
            mm = cm*10
            m_entry.delete(0 , 'end')
            feet_entry.delete(0 , 'end')
            mm_entry.delete(0 , 'end')
            m_entry.insert(1 , m)
            feet_entry.insert(1 , feet)
            mm_entry.insert(1 , mm)
            

        len_frame = Frame(c, bg = "cyan")
        len_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

        cm_entry = Entry(len_frame)
        cm_entry.place(relx = 0.45 , rely = 0.2)

        cm_label = Label(len_frame , text = "Enter length in cm")
        cm_label.place(relx = 0.3 , rely = 0.2)

        mm_label = Label(len_frame , text = "Length in mm")
        mm_label.place(relx = 0.3 , rely = 0.4)
        mm_entry = Entry(len_frame)
        mm_entry.place(relx = 0.45 , rely = 0.4)

        m_label = Label(len_frame , text = "Length in m")
        m_label.place(relx = 0.3 , rely = 0.5)
        m_entry = Entry(len_frame)
        m_entry.place(relx = 0.45 , rely = 0.5)

        feet_label = Label(len_frame , text = "Length in feet")
        feet_label.place(relx = 0.3 , rely = 0.6)
        feet_entry = Entry(len_frame)
        feet_entry.place(relx = 0.45 , rely = 0.6)
        
        submit_butt = Button(len_frame , text = "Submit" ,command = lambda: calc_len(cm_entry.get() , m_entry , feet_entry , mm_entry))
        submit_butt.place(relx = 0.4 , rely = 0.3)

        back = Button(len_frame , text = "< Back" , command = lambda : back7())
        back.place(relx = 0 , rely = 0)

        
    def timecon():
        def back8():
            time_frame.destroy()

        def calc_time(s , min_entry , hr_entry):
            min_entry.delete(0 , 'end')
            hr_entry.delete(0 , 'end')
            s = float(s)
            min = s / 60
            hr = min/60
            min_entry.insert(1 , min)
            hr_entry.insert(1 , hr)

        time_frame = Frame(c, bg = "cyan")
        time_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

        time_entry = Entry(time_frame)
        time_entry.place(relx = 0.45 , rely = 0.2)
        s_label = Label(time_frame , text = "Enter time in seconds")
        s_label.place(relx = 0.3 , rely = 0.2)

        min_label = Label(time_frame , text = "Time in minutes")
        min_label.place(relx = 0.3 , rely = 0.4)
        min_entry = Entry(time_frame)
        min_entry.place(relx = 0.45 , rely = 0.4)

        hr_label = Label(time_frame , text = "Time in hours")
        hr_label.place(relx = 0.3 , rely = 0.5)
        hr_entry = Entry(time_frame)
        hr_entry.place(relx = 0.45 , rely = 0.5)

        submit_butt = Button(time_frame , text = "Submit" ,command = lambda: calc_time(time_entry.get() , min_entry , hr_entry))
        submit_butt.place(relx = 0.4 , rely = 0.3)

        back = Button(time_frame , text = "< Back" , command = lambda : back8())
        back.place(relx = 0 , rely = 0)

    def temp():
        def back9():
            temp_frame.destroy()

        def calc_temp(fah , c_entry):
            fah = float(fah)
            cel = (fah-32)*(5/9)
            c_entry.delete(0 , 'end')
            c_entry.insert(1 , cel)
            

        temp_frame = Frame(c, bg = "cyan")
        temp_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

        fah_entry = Entry(temp_frame)
        fah_entry.place(relx = 0.45 , rely = 0.2)
        fah_label = Label(temp_frame , text = "Temp in Fahrenheit")
        fah_label.place(relx = 0.3 , rely = 0.2)

        c_label = Label(temp_frame , text = "Temp in celcius")
        c_label.place(relx = 0.3 , rely = 0.4)
        c_entry = Entry(temp_frame)
        c_entry.place(relx = 0.45 , rely = 0.4)

        submit_butt = Button(temp_frame , text = "Submit" ,command = lambda: calc_temp(fah_entry.get() , c_entry))
        submit_butt.place(relx = 0.4 , rely = 0.3)

        back = Button(temp_frame , text = "< Back" , command = lambda : back9())
        back.place(relx = 0 , rely = 0)

        
    def mass():
        def back10():
            mass_frame.destroy()
        def calc_mass(g , mg_entry , kg_entry):
            g = float(g)
            mg = g*1000
            kg = g/1000
            mg_entry.delete(0 , 'end')
            kg_entry.delete(0 , 'end')
            mg_entry.insert(1 , mg)
            kg_entry.insert(1 , kg)
            
        mass_frame = Frame(c, bg = "cyan")
        mass_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

        g_entry = Entry(mass_frame)
        g_entry.place(relx = 0.45 , rely = 0.2)
        g_label = Label(mass_frame , text = "Enter weight in g")
        g_label.place(relx = 0.3 , rely = 0.2)

        mg_label = Label(mass_frame , text = "Weight in mg")
        mg_label.place(relx = 0.3 , rely = 0.4)
        mg_entry = Entry(mass_frame)
        mg_entry.place(relx = 0.45 , rely = 0.4)

        kg_label = Label(mass_frame , text = "Weight in kg")
        kg_label.place(relx = 0.3 , rely = 0.5)
        kg_entry = Entry(mass_frame)
        kg_entry.place(relx = 0.45 , rely = 0.5)

        submit_butt = Button(mass_frame , text = "Submit" ,command = lambda: calc_mass(g_entry.get() , mg_entry , kg_entry))
        submit_butt.place(relx = 0.4 , rely = 0.3)

        back = Button(mass_frame , text = "< Back" , command = lambda : back10())
        back.place(relx = 0 , rely = 0)
    con_frame = Frame(c, bg = "cyan")
    con_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

    c1= PhotoImage(file="bmi_logo.png")
    conlabel1=Label(con_frame, image=c1)
    conlabel1.place(relx = 0.12 , rely = 0.11)
    cb1 = Button(con_frame, text = "BMI" , command = lambda: bmi())
    cb1.place(relx = 0.155 , rely = 0.35)

    c2= PhotoImage(file="dis_logo.png")
    conlabel2=Label(con_frame, image=c2)
    conlabel2.place(relx = 0.44 , rely = 0.11)
    cb2 = Button(con_frame, text = "Discount" , command = lambda: dis())
    cb2.place(relx = 0.445, rely = 0.35)

    c3= PhotoImage(file="length_logo.png")
    conlabel3=Label(con_frame, image=c3)
    conlabel3.place(relx = 0.7  ,rely = 0.11)
    cb3=Button(con_frame, text = "Length" , command = lambda: length())
    cb3.place(relx = 0.737 , rely = 0.35)

    c4= PhotoImage(file="temp_logo.png")
    conlabel4=Label(con_frame, image=c4)
    conlabel4.place(relx = 0.1435 , rely = 0.5)
    cb4=Button(con_frame, text = "Temperature" , command = lambda: temp())
    cb4.place(relx = 0.13 , rely = 0.74)

    c5= PhotoImage(file="time_logo.png")
    conlabel5=Label(con_frame, image=c5)
    conlabel5.place(relx = 0.42 , rely = 0.5)
    cb5=Button(con_frame, text = "Time", command = lambda: timecon())
    cb5.place(relx = 0.454 , rely = 0.74)

    c6= PhotoImage(file="mass_logo.png")
    conlabel6=Label(con_frame, image=c6)
    conlabel6.place(relx = 0.712 , rely = 0.5)
    cb6=Button(con_frame, text = "Mass", command = lambda: mass())
    cb6.place(relx = 0.739 , rely = 0.74)

    back = Button(con_frame , text = "< Back" , command = lambda : back4())
    back.place(relx = 0 , rely = 0)
####################################################################################################################################################################################
def notes():
    userText = False
    
    def back3():
        notes_frame.destroy()
        
    def disp():
        todo_list.delete(0,'end')
        my_cur.execute("Select * from todo")
        result = my_cur.fetchall()
        for i in result:
            todo_list.insert(0, i)
    
    def savenote(e):
        my_cur.execute("insert into todo(note) values ('%s')" % e)
        mydb.commit()
        disp()


    def del_note(todo_list):
        try:
            values = todo_list.curselection() #**
            index = values[0]   #** 
            val = todo_list.get(index)
            val = val[0]
            my_cur.execute("Delete from todo where note = ('%s')"  %val)
            mydb.commit()
            disp()

        except IndexError:
            print(showwarning("ALert" , "Please select a note first"))
    
    def userText(event):
       todo_entry.delete(0 , END)
       usercheck = TRUE

    notes_frame = Frame(c, bg = "cyan")
    notes_frame.place(relx = 0, rely = 0.1 , relwidth = 1, relheight = 0.9)

    todo_entry = Entry(notes_frame)
    todo_entry.insert(0 , "What to do?")
    todo_entry.bind('<Button>' , userText)
    todo_entry.place(relx = 0.35, rely = 0.1)
 
    todo_label = Label(notes_frame , text = "To-Do List" , width = 77)
    todo_label.place(relx = 0.13 , rely = 0.25)
    
    todo_list = Listbox(notes_frame , width = 90 , height = 15)
    todo_list.place(relx = 0.13 , rely = 0.3)
    
    submit_button = Button(notes_frame ,text = "Submit",  command = lambda: savenote(todo_entry.get()))
    submit_button.place(relx = 0.52 , rely = 0.09)
    disp()

    del_button = Button(notes_frame , text = "Work done delete it" , command = lambda: del_note(todo_list))
    del_button.place(relx = 0.8 , rely = 0.5)

    back = Button(notes_frame , text = "< Back" , command = lambda : back3())
    back.place(relx = 0 , rely = 0)
####################################################################################################################################################################################
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
####################################################################################################################################################################################

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
l6=Button(frame_body, text = "TO-DO", command = lambda: notes())
l6.place(relx = 0.624 , rely = 0.74)
    

root.resizable(0,0)
root.mainloop()





