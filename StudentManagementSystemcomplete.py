############################################# for inside add student
def addstudent():
    def submitadd():
        print('Added')
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='grey')
    addroot.resizable(False,False)

    #######################################add syudement labels
    idlabel = Label(addroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    idlabel.place(x=10,y=10)    

    namelabel = Label(addroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    namelabel.place(x=10,y=70)    

    mobilelabel = Label(addroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    mobilelabel.place(x=10,y=130)    

    emaillabel = Label(addroot,text='Enter Email :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    emaillabel.place(x=10,y=190)    

    addresslabel = Label(addroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    addresslabel.place(x=10,y=250)    

    genderlabel = Label(addroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    genderlabel.place(x=10,y=310)    

    doblabel = Label(addroot,text='Enter DOB :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    doblabel.place(x=10,y=370)    

    ############################################## add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=70)

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=130)

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=190)

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=250)

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=310)




    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=370)

    submitbtn = Button(addroot,text='submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='red',activeforeground='gold2',
    bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)



    addroot.mainloop()

def searchstudent():
    def search():
            print('search')
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x470+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='grey')
    searchroot.resizable(False,False)

    #######################################add syudement labels
    idlabel = Label(searchroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    idlabel.place(x=10,y=10)    

    namelabel = Label(searchroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    namelabel.place(x=10,y=70)    

    mobilelabel = Label(searchroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    mobilelabel.place(x=10,y=130)    

    emaillabel = Label(searchroot,text='Enter Email :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    emaillabel.place(x=10,y=190)    

    addresslabel = Label(searchroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    addresslabel.place(x=10,y=250)    

    genderlabel = Label(searchroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    genderlabel.place(x=10,y=310)    

    doblabel = Label(searchroot,text='Enter DOB :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    doblabel.place(x=10,y=370) 
    
    datelabel = Label(searchroot,text='Enter :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    datelabel.place(x=10,y=370) 

    


    

    ############################################## add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=10)

    mobileentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=70)

    emailentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=130)

    addressentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=190)

    genderentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=250)

    dobentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=310)

    dateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=370)
    
    submitbtn = Button(searchroot,text='search',font=('roman',15,'bold'),width=20,bd=5,activebackground='red',activeforeground='gold2',
    bg='red',command=search)
    submitbtn.place(x=150,y=420)

    



    searchroot.mainloop()

    

def deletestudent():
    print('student deleted')

def updatestudent():
    print('student updated')


def updatestudent():
    def update():
            print('update')
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x470+220+200')
    updateroot.title('Student Management System')
    updateroot.config(bg='grey')
    updateroot.resizable(False,False)

    #######################################add syudement labels
    idlabel = Label(updateroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    idlabel.place(x=10,y=10)    

    namelabel = Label(updateroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    namelabel.place(x=10,y=70)    

    mobilelabel = Label(updateroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    mobilelabel.place(x=10,y=130)    

    emaillabel = Label(updateroot,text='Enter Email :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    emaillabel.place(x=10,y=190)    

    addresslabel = Label(updateroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    addresslabel.place(x=10,y=250)    

    genderlabel = Label(updateroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    genderlabel.place(x=10,y=310)    

    doblabel = Label(updateroot,text='Enter DOB :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    doblabel.place(x=10,y=370) 
    
    datelabel = Label(updateroot,text='Enter Date :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    datelabel.place(x=10,y=370) 

    timelabel = Label(updateroot,text='Enter Time :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12)
    timelabel.place(x=10,y=370) 

    


    


    

    ############################################## add student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=10)

    mobileentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=70)

    emailentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=130)

    addressentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=190)

    genderentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=250)

    dobentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=310)

    dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=370)
    
    timeentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=370)
    
    submitbtn = Button(updateroot,text='search',font=('roman',15,'bold'),width=20,bd=5,activebackground='red',activeforeground='gold2',
    bg='red',command=update)
    submitbtn.place(x=150,y=420)

    



    updateroot.mainloop()

    

def showstudent():
    print('student show')

def exportstudent():
    print('student export')

def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    print(res)



#########################################connection nto database
def Connectdb():
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='grey')

############################################################# labels
    hostlabel = Label(dbroot,text="Enter host :",bg='gold',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter user :",bg='gold',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter password :",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,anchor='w')
    passwordlabel.place(x=10,y=130)



####################################### connectiondb entry
    hostval = StringVar()
    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userval = StringVar()
    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5)
    passwordentry.place(x=250,y=130)


    ############################# submit button
    submitbutton = Button(dbroot,text='submit',font=('roman',15,'bold'),width=20,activebackground='red'
    ,activeforeground='gold2',bd=5,command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()

def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200, tick)
###############################3 INTRO SLIDER
import random
colors = ['red','grey','blue','pink']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(20,IntroLabelColorTick)


def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count =0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200,IntroLabelTick)
####################################################

from tkinter import *
from tkinter import Toplevel, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import sqlite3
import random
import time
root = Tk()
root.title('Student Management System')
root.config(bg='grey')
root.geometry('1175x700+200+50')
############### frames

DataEntryFrame = Frame(root, bg='white',relief=SOLID,borderwidth=6)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

############################################### dataentry inside the frame and intro
frontlabel = Label(DataEntryFrame,text='---------------welcome------------',width=30,font=('arial',22,'italic','bold'))
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1 .Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
activeforeground='white',command=addstudent)

addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2 .Search Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
activeforeground='white',command=searchstudent)

searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3 .Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief= RIDGE,
activeforeground='white',command=deletestudent)

deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4 .Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief= RIDGE,
activeforeground='white',command=updatestudent)

updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5 . Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief= RIDGE,
activeforeground='white',command=showstudent)

showallbtn.pack(side=TOP,expand=True)

exportdatabtn = Button(DataEntryFrame,text='6 .Export Data',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief= RIDGE,
activeforeground='white',command=exportstudent)

exportdatabtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7 .Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief= RIDGE,
activeforeground='white',command=exit)

exitbtn.pack(side=TOP,expand=True)



ShowDataFrame = Frame(root,bg='white',relief=SOLID,borderwidth=6)
ShowDataFrame.place(x=550,y=80,width=620,height=600)
######################################################################show data frames
style = ttk.Style()
style.configure('Treeview.Heading', font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)


studnettable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time')
,yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studnettable.xview)
scroll_y.config(command=studnettable.yview)

studnettable.heading('Id',text='Id')
studnettable.heading('Name',text='Name')
studnettable.heading('Mobile No',text='Mobile No')
studnettable.heading('Email',text='Email')
studnettable.heading('Address',text='Address')
studnettable.heading('Gender',text='Gender')
studnettable.heading('D.O.B',text='D.O.B')
studnettable.heading('Added Date',text='Added Dssate')
studnettable.heading('Added Time',text='Added time')
studnettable['show']= 'headings'
studnettable.column('Id',width=100)
studnettable.column('Name',width=200)
studnettable.column('Mobile No',width=200)
studnettable.column('Email',width=300)
studnettable.column('Address',width=200)
studnettable.column('Gender',width=100)
studnettable.column('D.O.B',width=150)
studnettable.column('Added Date',width=150)
studnettable.column('Added Time',width=150)

studnettable.pack(fill=BOTH,expand=1)



########################################## slider

ss = 'Welcome To Student Management System'
count = 0
text = ''
##########################
SliderLabel = Label(root, text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=5,width=35,bg='cyan')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()
############################################################ clock
clock = Label(root,font=('times',14,' bold'),relief=RIDGE,borderwidth=5,bg='lawn green')
clock.place(x=0,y=0)
tick()
################################################# connect to database
connectbutton = Button(root,text='Connect To Database',width=23,
activebackground='red',activeforeground='white',font=('chiller',15,'italic bold'),relief=RIDGE,borderwidth=5,bg='cyan',bd=6,command=Connectdb)
connectbutton.place(x=930,y=0)




root.mainloop()

