import mysql.connector
import smtplib
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import ttkwidgets.autocomplete
from PIL import ImageTk
import mysql.connector
# from ttkwidgets.autocomplete import AutocompleteEntry
from tkinter import *
import random
import re

#SHOWS LOGIN OR SIGNUP
class register:
    def __init__(self, root):
        self.root = root
        self.root.title("PROCTOR")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="#072227")
        self.root.attributes('-fullscreen', True)
        title = tk.Label(text="PROCTORSHIP DATABASE", font=("Times new roman", 40, "bold"), bg="#35858B", fg="#0f4c54", bd=10,
                         relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        self.login_frame = tk.Frame(self.root,bg="#072227")
        self.login_frame.place(relx=.5, rely=.5,anchor="center")

        self.frame = tk.Frame(self.root, bg="#072227")
        self.frame.place(x=1300, y=85)
        # LOGIN
        btn = tk.Button(self.login_frame, text="LOGIN", command=self.load_new, width=20, height=3,
                        font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227")
        btn.grid(row=0, column=0, padx=30, pady=40)

        # SIGNUP
        btn = tk.Button(self.login_frame, text="SIGNUP", command=self.load_new1, width=20, height=3,
                        font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227")
        btn.grid(row=0, column=5, padx=20, pady=20)

        #close
        btn = tk.Button(self.frame, text="CLOSE", command=self.load_new2, width=20, height=2,
                        font=("Roboto", 12, "bold"), relief=GROOVE, bg="#B8405E", fg="#072227")
        btn.grid(row=0, column=0, padx=20, pady=20)




    def load_new(self):
        self.frame.destroy()
        self.login_frame.destroy()
        self.another = login(self.root)

    def load_new1(self):
        self.frame.destroy()
        self.login_frame.destroy()
        self.another = register_teacher(self.root)

    def load_new2(self):
        self.root.destroy()

#ALLOWS TO REGISTER TEACHER
class register_teacher:

    global otp
    otp = random.randint(1000, 9999)
    otp = str(otp)
    def __init__(self, root):
        self.root = root
        self.root.title("PROCTOR")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="#072227")
        # self.root.attributes('-fullscreen', True)
        title = tk.Label(text="PROCTORSHIP DATABASE", font=("Times new roman", 40, "bold"), bg="#35858B", fg="#0f4c54", bd=10,
                         relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        self.uname = tk.StringVar()
        self.name = tk.StringVar()
        self.phone = tk.StringVar()
        self.paswd = tk.StringVar()
        self.paswd1 = tk.StringVar()
        self.emailid = tk.StringVar()
        self.otp = tk.StringVar()
        # Images
        self.logo = ImageTk.PhotoImage(file="C:/Users/Tejas/PycharmProjects/DBMSPROJECT/images/logo.png")

        self.login_frame = tk.Frame(self.root, bg="#072227")
        self.login_frame.place(relx=0.5, rely=0.55, anchor="center")

        self.frame = tk.Frame(self.root, bg="#072227")
        self.frame.place(x=1000, y=115)



        logolbl = tk.Label(self.login_frame, image=self.logo, bg="#072227")
        logolbl.grid(row=0, column=0,padx=(40,0),pady=(10,20))


        #Username
        usrlbl = tk.Label(self.login_frame, text="USERNAME",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        usrlbl.grid(row=1, column=0,padx=(80,20),pady=(0,15))
        usr_entry = tk.Entry(self.login_frame, bd=3, bg="#072227",width=45, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE, textvariable=self.uname,
                             font=("comic sans", 15))
        usr_entry.grid(row=1, column=1,pady=(0,15))

        # name
        name = tk.Label(self.login_frame, text="NAME",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        name.grid(row=2, column=0 ,padx=(15,20),pady=(0,15))
        name_en = tk.Entry(self.login_frame, bd=3, bg="#072227", fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", width=45,relief=GROOVE, textvariable=self.name,
                             font=("comic sans", 15))
        name_en.grid(row=2, column=1,pady=(0,15))

        # phone
        usrlbl = tk.Label(self.login_frame, text="PHONE",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        usrlbl.grid(row=3, column=0, padx=(35,20),pady=(0,15) )
        usr_entry = tk.Entry(self.login_frame, bd=3, bg="#072227", fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF",width=45, relief=GROOVE, textvariable=self.phone,
                             font=("comic sans", 15))
        usr_entry.grid(row=3, column=1,pady=(0,15))

        #Password
        pwdlbl = tk.Label(self.login_frame, text="PASSWORD",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        pwdlbl.grid(row=4, column=0, padx=(85,20),pady=(0,15) )
        pwd_entry = tk.Entry(self.login_frame, bd=3, bg="#072227", fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF",width=45, relief=GROOVE, textvariable=self.paswd,
                             font=("comic sans", 15), show="*")
        pwd_entry.grid(row=4, column=1,pady=(0,15) )

        #Confirm Password
        pwd1lbl = tk.Label(self.login_frame, text="CONFIRM PASSWORD",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        pwd1lbl.grid(row=5, column=0, padx=(205,20),pady=(0,15))
        pwd1_entry = tk.Entry(self.login_frame, bd=3,width=45, bg="#072227", fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE, textvariable=self.paswd1,
                             font=("comic sans", 15), show="*")
        pwd1_entry.grid(row=5, column=1,pady=(0,15))

        # Email

        emlbl = tk.Label(self.login_frame, text="EMAIL",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        emlbl.grid(row=6, column=0, padx=(15,20),pady=(0,15))
        em_entry = tk.Entry(self.login_frame, bd=3,width=45, bg="#072227", fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE, textvariable=self.emailid,
                             font=("comic sans", 15))
        em_entry.grid(row=6, column=1,pady=(0,15))


        #OTP
        otplbl = tk.Label(self.login_frame, text="OTP",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        otplbl.grid(row=7, column=0, padx=(0,20),pady=(0,15))
        otp_entry = tk.Entry(self.login_frame, bd=3,width=45, bg="#072227", fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE, textvariable=self.otp,
                             font=("comic sans", 15))
        otp_entry.grid(row=7, column=1,pady=(0,15))

        def send():
            try:
                s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
                s.starttls()
                s.login("tejasvirat72@gmail.com", "Tejasr@125")

                print(otp)
                s.sendmail("tejasvirat72@gmail.com", em_entry.get(), otp)
                messagebox.showinfo("Send OTP via Email", f"OTP sent to {em_entry.get()}")
                s.quit()


            except:
                messagebox.showinfo("Send OTP via Email",
                                    "Please enter the valid email address OR check an internet connection")


        #Verify
        send_button = tk.Button(self.login_frame, width=20, bg="#4FBDBA", height=1, text="VERIFY EMAIL",
                             font=("times new roman", 12, "bold"), fg="#072227", command=send)
        send_button.grid(row=6, column=2,pady=(0,15),padx=(20,30))








        btn = tk.Button(self.login_frame, width=20, bg="#4FBDBA", height=2, text="REGISTER",
                             font=("times new roman", 12, "bold"), fg="#072227", command=self.register)
        btn.grid(row=8, columnspan=2, padx=20,pady=(20,10))

        # GO BACK
        self.btn = tk.Button(self.frame, width=20, bg="#4FBDBA", height=2, text="GO BACK",
                             font=("times new roman", 12, "bold"), fg="#072227", command=self.back1)
        self.btn.grid(row=6, columnspan=5, padx=20, pady=(0, 10))

    def back1(self):
        self.frame.destroy()
        self.login_frame.destroy()
        self.another = register(self.root)





    def register(self):
        print(otp)
        print(self.paswd.get())
        print(self.paswd1.get())
        if(self.paswd.get()==self.paswd1.get()):

            if (otp == self.otp.get()):
                messagebox.showinfo("Successful", "OTP Verified")
                mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
                cursor = mydb.cursor()
                cursor.execute("SELECT * FROM teacher")
                result = cursor.fetchall()
                print(result)
                for i in result:
                    if self.uname.get() == i[0]:
                        messagebox.showerror("Error", f"{self.uname.get()} : Already Exists")
                        break
                    elif self.emailid.get() == i[4]:
                        messagebox.showerror("Error", f"{self.emailid.get()} : Already Exists")
                        break

                    else:
                        messagebox.showinfo("Successful", "Registered Successfully")
                        insert_query = "INSERT INTO teacher(T_id,T_name,pwd,phone,email) VALUES(%s,%s,%s,%s,%s)"

                        record = (self.uname.get(), self.name.get(), self.paswd.get(), self.phone.get(), self.emailid.get())
                        cursor.execute(insert_query, record)
                        mydb.commit()
                        print("Record added Successfully")
                        self.frame.destroy()
                        self.login_frame.destroy()
                        self.another=register(self.root)


            else:
                messagebox.showerror("Error", "Wrong OTP")

#ALLOWS TO LOGIN AS STUDENT OR TEACHER
class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="#072227")
        # self.root.attributes('-fullscreen', True)
        title = tk.Label(text="LOGIN", font=("Times new roman", 40, "bold"), bg="#35858B", fg="#0f4c54", bd=10,
                         relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        self.login_frame = tk.Frame(self.root,bg="#072227")
        self.login_frame.place(relx=.5, rely=.5,anchor="center")

        self.frame = tk.Frame(self.root, bg="#072227")
        self.frame.place(x=1075, y=100)




        #Student
        btn = tk.Button(self.login_frame, text="STUDENT", command=self.load_new, width=20, height=3,
                        font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227")
        btn.grid(row=0, column=0, padx=30, pady=40)

        # Teacher
        btn = tk.Button(self.login_frame, text="TEACHER", command=self.load_new1, width=20,height=3,font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA",fg="#072227")
        btn.grid(row=0, column=5, padx=20, pady=20)

        # GO BACK
        self.btn = tk.Button(self.frame, width=20, bg="#4FBDBA", height=2, text="GO BACK",
                             font=("Roboto", 12, "bold"), fg="#072227", command=self.back1)
        self.btn.grid(row=6, columnspan=2, padx=20, pady=(0, 10))

    def back1(self):
        self.frame.destroy()
        self.login_frame.destroy()
        self.another = register(self.root)

    def load_new(self):
        self.frame.destroy()
        self.login_frame.destroy()
        self.another = Login_System_Student(self.root)

    def load_new1(self):
        self.frame.destroy()
        self.login_frame.destroy()
        self.another = Login_System_Teacher(self.root)

#LOGIN PAGE STUDENT
class Login_System_Student:
    def __init__(self, root):
        self.root = root

        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="#072227")
        # self.root.attributes('-fullscreen', True)
        self.uname = tk.StringVar()
        self.paswd = tk.StringVar()
        # Images
        self.logo = ImageTk.PhotoImage(file="C:/Users/Tejas/PycharmProjects/DBMSPROJECT/images/logo.png")
        title = tk.Label(text="PROCTOR DATABASE", font=("Times new roman", 40, "bold"), bg="#35858B", fg="#0f4c54", bd=10,
                         relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        self.login_frame = tk.Frame(self.root, bg="#072227",bd=2,highlightbackground="#AEFEFF",highlightthickness=1)
        self.login_frame.place(relx=0.5,rely=0.55,anchor="center")

        self.frame = tk.Frame(self.root, bg="#072227")
        self.frame.place(x=1075,y=100)

        #Image
        logolbl = tk.Label(self.login_frame, image=self.logo, bd=0,bg="#072227")
        logolbl.grid(row=0, columnspan=2, padx=50,pady=20)

        # Username
        usrlbl = tk.Label(self.login_frame, text="USERNAME",
                          font=("Roboto", 18), bg="#072227",fg="WHITE")
        usrlbl.grid(row=1, column=1, padx=20, pady=(10,0))
        usr_entry = tk.Entry(self.login_frame,  bd=3,insertbackground="#AEFEFF", bg="#072227",fg="#AEFEFF", cursor="xterm #AEFEFF", textvariable=self.uname, relief=GROOVE, font=("comic sans", 15))
        usr_entry.grid(row=2, column=1, padx=90,pady=5)

        #password
        pwdlbl = tk.Label(self.login_frame, text="PASSWORD",
                          font=("Roboto", 18), bg="#072227",fg="WHITE")
        pwdlbl.grid(row=3, column=1, padx=20)
        pwd_entry = tk.Entry(self.login_frame, bd=3,bg="#072227",fg="#AEFEFF", cursor="xterm #AEFEFF" ,insertbackground="#AEFEFF",relief=GROOVE, textvariable=self.paswd, font=("comic sans", 15),show="*")
        pwd_entry.grid(row=4, column=1, padx=90,pady=5)


        #button
        btn = tk.Button(self.login_frame, text="LOGIN", command=self.login, width=20,height=2,font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA",fg="#072227")
        btn.grid(row=5, columnspan=2, padx=20,pady=(15,40))

        # GO BACK
        self.btn = tk.Button(self.frame, width=20,bg="#4FBDBA", height=2, text="GO BACK", font=("times new roman", 12, "bold"),fg="#072227",command=self.back1)
        self.btn.grid(row=6, columnspan=2, padx=20, pady=(0,10))

    def back1(self):
        self.frame.destroy()
        self.login_frame.destroy()
        self.another = login(self.root)

    def login(self):
        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        cursor.execute("SELECT usn,pwd FROM student")
        result = cursor.fetchall()
        print(result)
        if len(self.uname.get()) != 10:
            messagebox.showerror("Name Error", "USN should be of 10 characters")
        else:
            for i in result:
                if self.uname.get() == i[0] and self.paswd.get() == i[1]:
                    messagebox.showinfo("Successful", f"welcome {self.uname.get()}")
                    self.frame.destroy()
                    self.login_frame.destroy()
                    self.another=student(self.root)
                    break
        if self.uname.get() != i[0] or self.paswd.get() != i[1]:
            messagebox.showerror("Error", "Invalid username and password")

#LOGIN PAGE TEACCHER
class Login_System_Teacher:
    def __init__(self, root):
        self.root = root

        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="#072227")
        # self.root.attributes('-fullscreen', True)
        self.uname = tk.StringVar()
        self.paswd = tk.StringVar()
        # Images
        self.logo = ImageTk.PhotoImage(file="C:/Users/Tejas/PycharmProjects/DBMSPROJECT/images/logo.png")
        title = tk.Label(text="PROCTOR DATABASE", font=("Times new roman", 40, "bold"), bg="#35858B", fg="#0f4c54",
                         bd=10,
                         relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        self.login_frame = tk.Frame(self.root, bg="#072227", bd=2, highlightbackground="#AEFEFF", highlightthickness=1)
        self.login_frame.place(relx=0.5, rely=0.55, anchor="center")

        self.frame = tk.Frame(self.root, bg="#072227")
        self.frame.place(x=1075, y=100)

        # Image
        logolbl = tk.Label(self.login_frame, image=self.logo, bd=0, bg="#072227")
        logolbl.grid(row=0, columnspan=2, padx=50, pady=20)

        # Username
        usrlbl = tk.Label(self.login_frame, text="USERNAME",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        usrlbl.grid(row=1, column=1, padx=20, pady=(10, 0))
        usr_entry = tk.Entry(self.login_frame, bd=3, insertbackground="#AEFEFF", bg="#072227", fg="#AEFEFF",
                             cursor="xterm #AEFEFF", textvariable=self.uname, relief=GROOVE, font=("comic sans", 15))
        usr_entry.grid(row=2, column=1, padx=90, pady=5)

        # password
        pwdlbl = tk.Label(self.login_frame, text="PASSWORD",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        pwdlbl.grid(row=3, column=1, padx=20)
        pwd_entry = tk.Entry(self.login_frame, bd=3, bg="#072227", fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE, textvariable=self.paswd,
                             font=("comic sans", 15), show="*")
        pwd_entry.grid(row=4, column=1, padx=90, pady=5)

        # button
        btn = tk.Button(self.login_frame, text="LOGIN", command=self.login, width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227")
        btn.grid(row=5, columnspan=2, padx=20, pady=(15, 40))

        # GO BACK
        self.btn = tk.Button(self.frame, width=20, bg="#4FBDBA", height=2, text="GO BACK",
                             font=("times new roman", 12, "bold"), fg="#072227", command=self.back1)
        self.btn.grid(row=6, columnspan=2, padx=20, pady=(0, 10))

    def back1(self):
        self.frame.destroy()
        self.login_frame.destroy()
        self.another = login(self.root)

    def login(self):
        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        cursor.execute("SELECT T_id,pwd FROM teacher")
        result = cursor.fetchall()
        print(result)
        for i in result:
            if self.uname.get() == i[0] and self.paswd.get() == i[1]:
                messagebox.showinfo("Successful", f"welcome {self.uname.get()}")
                self.frame.destroy()
                self.login_frame.destroy()
                self.another = teacher(self.root)
                break
        if self.uname.get() != i[0] or self.paswd.get() != i[1]:
            messagebox.showerror("Error", "Invalid username and password")

#STUDENT FRONT PAGE
class student:
    def __init__(self, root):
        self.root = root
        self.root.title("student")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="#072227")
        # self.root.attributes('-fullscreen', True)
        #frame
        self.student_frame=tk.Frame(self.root, bg="#072227")
        self.student_frame.place(relx=0.5,rely=0.5,anchor="center")

        self.frame = tk.Frame(self.root, bg="#072227")
        self.frame.place(x=1075, y=115)


        #Fill proctor book
        btn=tk.Button(self.student_frame,  text="FILL PROCTOR BOOK",width=20, height=3,
                        font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",command=self.new)
        btn.grid(row=0,column=0,padx=20,pady=(20,0))

        # RAISE ISSUES
        btn = tk.Button(self.student_frame, text="RAISE ISSUES", width=20, height=3,
                        font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",command=self.new1)
        btn.grid(row=1, column=0, padx=20, pady=10)


        # GO BACK
        self.btn = tk.Button(self.frame,text="LOGOUT",
                             width=20, height=2,
                             font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", command=self.back1)
        self.btn.grid(row=2, columnspan=2, padx=20, pady=(0,20))

    def back1(self):
        self.frame.destroy()
        self.student_frame.destroy()
        self.another = Login_System_Student(self.root)



    def new(self):
        self.frame.destroy()
        self.student_frame.destroy()
        self.another=fill_proctor(self.root)

    def new1(self):
        self.frame.destroy()
        self.student_frame.destroy()
        self.another = raiseissue(self.root)

#1ST OPTION OF STUDENT
class fill_proctor:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.configure(background="#072227")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        # self.root.attributes('-fullscreen', True)
        # self.root.attributes('-fullscreen', True)
        self.name = tk.StringVar()
        self.usn = tk.StringVar()
        self.dob = tk.StringVar()
        self.yoa = tk.StringVar()
        self.email = tk.StringVar()
        self.fname = tk.StringVar()
        self.mname = tk.StringVar()
        self.pcn = tk.StringVar()
        self.pemail = tk.StringVar()
        self.peradd = tk.StringVar()
        self.studcn = tk.StringVar()
        self.ten = tk.StringVar()
        self.twel = tk.StringVar()
        self.bgrp = tk.StringVar()
        self.pwd = tk.StringVar()

        # self.frame=tk.Frame(self.root, bg="#072227")
        # self.frame.place(relx=.5, rely=.55,anchor="center")
        self.frame1 = tk.Frame(self.root, bg="#072227")
        self.frame1.place(x=1275, y=95)


        self.frame2 = tk.Frame(self.root, bg="#072227")
        self.frame2.place(x=0, y=200)
        self.frame3 = tk.Frame(self.root, bg="#072227")
        self.frame3.place(x=675, y=200)
        self.frame4 = tk.Frame(self.root, bg="#072227")
        self.frame4.place(x=0, y=750)



        #name
        name = tk.Label(self.frame2, text="STUDENT'S NAME:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        name.grid(row=6, column=0,sticky='w',pady=(20,0))
        name_en = tk.Entry(self.frame2,  textvariable=self.name, bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        name_en.grid(row=6, column=1,sticky='w',pady=(20,0))

        #usn
        usn = tk.Label(self.frame2, text="STUDENT'S USN:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        usn.grid(row=7, column=0,sticky='w',pady=(20,0))
        usn_en = tk.Entry(self.frame2,textvariable=self.usn, bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        usn_en.grid(row=7, column=1,sticky='w',pady=(20,0))

        #dob
        dob = tk.Label(self.frame2, text="STUDENT'S DOB:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        dob.grid(row=8, column=0,sticky='w',pady=(20,0))
        dob_en = tk.Entry(self.frame2, textvariable=self.dob, bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        dob_en.grid(row=8, column=1,sticky='w',pady=(20,0))

        #year_of_admission
        yoa = tk.Label(self.frame2, text="YEAR OF ADMISSION:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        yoa.grid(row=9, column=0,sticky='w',pady=(20,0))
        yoa_en = tk.Entry(self.frame2,  textvariable=self.yoa, bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        yoa_en.grid(row=9, column=1,sticky='w',pady=(20,0))

        #email
        email = tk.Label(self.frame2, text="STUDENT'S E-MAIL:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        email.grid(row=10, column=0,sticky='w',pady=(20,0))
        email_en = tk.Entry(self.frame2, textvariable=self.email,bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        email_en.grid(row=10, column=1,sticky='w',pady=(20,0))

        #fathername
        fname = tk.Label(self.frame2, text="FATHER'S NAME:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        fname.grid(row=11, column=0,sticky='w',pady=(20,0))
        fname_en = tk.Entry(self.frame2, textvariable=self.fname,bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        fname_en.grid(row=11, column=1,sticky='w',pady=(20,0))

        #mother name
        mname = tk.Label(self.frame2, text="MOTHER'S NAME:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        mname.grid(row=12, column=0,sticky='w',pady=(20,0))
        usr_entry = tk.Entry(self.frame2,  textvariable=self.mname, bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        usr_entry.grid(row=12, column=1,sticky='w',pady=(20,0))

        #parentscontact
        pcn = tk.Label(self.frame2, text="PARENT'S CONTACT NUMBER:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        pcn.grid(row=13, column=0,sticky='w',pady=(20,0))
        pcn_en = tk.Entry(self.frame2,  textvariable=self.pcn, bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        pcn_en.grid(row=13, column=1,sticky='w',pady=(20,0))

        #parentsemail
        pemail = tk.Label(self.frame3, text="PARENT'S E-MAIL:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        pemail.grid(row=6, column=0,sticky='w',pady=(20,0))
        pemail_en = tk.Entry(self.frame3, textvariable=self.pemail,bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        pemail_en.grid(row=6, column=1,sticky='w',pady=(20,0))

        #permaddress
        padd = tk.Label(self.frame3, text="PERMANENT ADDRESS:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        padd.grid(row=7, column=0,sticky='w',pady=(20,0))
        padd_en= tk.Entry(self.frame3, textvariable=self.peradd,bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        padd_en.grid(row=7, column=1,sticky='w',pady=(20,0))

        #students contact
        scn = tk.Label(self.frame3, text="STUDENT'S CONTACT NUMBER:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        scn.grid(row=8, column=0,sticky='w',pady=(20,0))
        scn_en = tk.Entry(self.frame3,  textvariable=self.studcn, bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        scn_en.grid(row=8, column=1,sticky='w',pady=(20,0))

        #10thmarks
        ten = tk.Label(self.frame3, text="MARKS OBTAINED IN 10TH:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        ten.grid(row=9, column=0,sticky='w',pady=(20,0))
        ten_en = tk.Entry(self.frame3,  textvariable=self.ten,bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        ten_en.grid(row=9, column=1,sticky='w',pady=(20,0))

        #12thmarks
        twel = tk.Label(self.frame3, text="MARKS OBTAINED IN 12TH:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        twel.grid(row=10, column=0,sticky='w',pady=(20,0))
        twel_en = tk.Entry(self.frame3,  textvariable=self.twel,bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        twel_en.grid(row=10, column=1,sticky='w',pady=(20,0))

        #bloodgrp
        bgrp = tk.Label(self.frame3, text="STUDENT'S BLOOD GROUP:",
                          font=("Roboto", 18), bg="#072227", fg="WHITE")
        bgrp.grid(row=11, column=0,sticky='w',pady=(20,0))
        bgrp_en = tk.Entry(self.frame3,  textvariable=self.bgrp,bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        bgrp_en.grid(row=11, column=1,sticky='w',pady=(20,0))

        # Password
        bgrp = tk.Label(self.frame3, text="NEW PASSWORD:",
                        font=("Roboto", 18), bg="#072227", fg="WHITE")
        bgrp.grid(row=12, column=0,sticky='w',pady=(20,0))
        bgrp_en = tk.Entry(self.frame3, textvariable=self.pwd,bd=3, bg="#072227", width=25, fg="#AEFEFF", cursor="xterm #AEFEFF",
                             insertbackground="#AEFEFF", relief=GROOVE,
                             font=("comic sans", 15))
        bgrp_en.grid(row=12, column=1,sticky='w',pady=(20,0))



        # submit
        btn = tk.Button(self.frame4, text="SUBMIT", height=2, width=25,font=("times new roman", 12, "bold"),relief=GROOVE, bg="#4FBDBA", fg="#072227",command=self.submit)
        btn.grid(row=0, column=0,sticky='w', padx=100, pady=10)


        #updatemarks&atten_button
        btn = tk.Button(self.frame4,text="UPDATE MARKS/ATTENDANCE",height=2, width=45, font=("times new roman", 12, "bold"),
                        relief=GROOVE, bg="#4FBDBA", fg="#072227",command=self.sem)
        btn.grid(row=0, column=6, padx=100,sticky='nsew', pady=10)


        # GO BACK
        self.btn = tk.Button(self.frame4, height=2, width=20, font=("times new roman", 12, "bold"),
                        relief=GROOVE, bg="#4FBDBA", fg="#072227", text="GO BACK", command=self.back3)
        self.btn.grid(row=0, column=9,sticky='e', padx=100, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame1, height=2, width=20, font=("times new roman", 12, "bold"),
                             relief=GROOVE, bg="#4FBDBA", fg="#072227", text="LOGOUT",
                             command=self.back22)
        self.btn.grid(row=0, column=0, pady=10)


    def back22(self):
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.frame1.destroy()

        self.another = Login_System_Student(self.root)


    def back3(self):
        self.frame1.destroy()

        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.another = student(self.root)



    def submit(self):
        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        select="select usn from student"
        cursor.execute(select)
        result=cursor.fetchall()
        a=False
        for i in result:
            if self.usn.get() == i[0]:
                a=True
                break
        if a==True:
            record = (
            self.name.get(), self.pwd.get(), self.peradd.get(), self.studcn.get(), self.email.get(), self.bgrp.get(),
            self.ten.get(), self.twel.get(), self.fname.get(), self.mname.get(), self.pcn.get(), self.yoa.get(),
            self.pemail.get(), self.dob.get(), self.usn.get())
            for i in record:
                if len(i)== 0:
                    messagebox.showerror("Error","Enter all fields!!")
                    break
            else:
                mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
                cursor = mydb.cursor()
                insert_query = "update student set name=%s,pwd=%s,address=%s,phone=%s,email=%s,bgrp=%s,m_ten=%s,m_twel=%s,fname=%s,mname=%s,p_numb=%s,yoa=%s,pemail=%s,dob=%s where usn=%s"

                cursor.execute(insert_query, record)
                messagebox.showinfo("Successful","Student's details inserted")
                mydb.commit()
        else:
            messagebox.showerror("Error", "USN not registered!!")





    def sem(self):
        self.frame1.destroy()

        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()

        self.framenw = tk.Frame(self.root,bg="#072227")
        self.framenw.place(relx=.5, rely=.55, anchor="center")
        self.framenw1 = tk.Frame(self.root, bg="#072227")
        self.framenw1.place(x=975, y=95)
        # self.root.attributes('-fullscreen', True)

        self.clicked = tk.StringVar()
        self.clicked1 = tk.StringVar()
        self.clicked2 = tk.StringVar()
        self.clicked3 = tk.StringVar()
        self.clicked4 = tk.StringVar()
        self.sub_m = tk.StringVar()
        self.sub_at = tk.StringVar()


        # usn
        usn = tk.Label(self.framenw, text="STUDENT'S USN:",
                       font=("Roboto", 18), bg="#072227", fg="WHITE")
        usn.grid(row=0, column=0,  pady=(20, 0), padx=(20, 0))
        usn_en = tk.Entry(self.framenw,  textvariable=self.usn, bd=3, bg="#072227", width=45, fg="#AEFEFF",
                           cursor="xterm #AEFEFF",
                           insertbackground="#AEFEFF", relief=GROOVE,
                           font=("comic sans", 15))
        usn_en.grid(row=0, column=1,  pady=(20, 0), padx=(0, 20))

        #Semester dropdown
        self.sem=['1','2','3','4','5','6','7','8']
        self.clicked.set("SEMESTER")
        self.drop = tk.OptionMenu(self.framenw, self.clicked, *self.sem)
        self.drop.config(font=("times new roman", 12, "bold"),bd=0, width=20, height=2,bg="#4FBDBA", fg="#072227")
        self.drop.grid(row=1, column=0,pady=(20,0))

        #branch_id
        self.ia3 = ['CSE', 'ISE']
        self.clicked4.set("BRANCH_ID")
        self.drop = tk.OptionMenu(self.framenw, self.clicked4, *self.ia3)
        self.drop.config(font=("times new roman", 12, "bold"), width=20, bd=0, height=2, bg="#4FBDBA", fg="#072227")
        self.drop.grid(row=1, column=1, pady=(20, 0))

        self.btn = tk.Button(self.framenw, text="SELECT", font=("times new roman", 12, "bold"), width=20, height=2,bg="#4FBDBA", fg="#072227", command=self.sub_code)
        self.btn.grid(row=1, column=2,pady=(20,0))


        # GO BACK
        self.btn = tk.Button(self.framenw1,  height=2, width=20, font=("times new roman", 12, "bold"),
                        relief=GROOVE, bg="#4FBDBA", fg="#072227", text="CLOSE",
                             command=self.back11)
        self.btn.grid(row=0, column=0, padx=10, pady=10)



    def back11(self):


        self.framenw1.destroy()
        self.framenw.destroy()

        self.another = fill_proctor(self.root)




        #sub_code drop down
    def sub_code(self):
        record=(int(self.clicked.get()),self.clicked4.get())
        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        select_query="SELECT c.sub_code FROM consists c where c.sem=%s and c.b_id=%s"
        cursor.execute(select_query,record)
        result = cursor.fetchall()
        self.result=list(result)
        print(self.result)
        # print(self.result[0][0])
        # self.result = ['18MAT11', '18CHE12', '18CPS13', '18ELN14', '18ME15', '18CHEL16', '18CPL16']
        self.clicked1.set("SUB_CODE")
        self.drop = tk.OptionMenu(self.frame, self.clicked1, *self.result)
        self.drop.config(font=("times new roman", 12, "bold"), width=20,bd=0, height=2, bg="#4FBDBA", fg="#072227")
        self.drop.grid(row=2, column=0, pady=(20, 0))

        # ia drop down
        self.ia = ['IA1','IA2','IA3']
        self.clicked2.set("INTERNALS")
        self.drop = tk.OptionMenu(self.frame, self.clicked2, *self.ia)
        self.drop.config(font=("times new roman", 12, "bold"), width=20,bd=0, height=2, bg="#4FBDBA", fg="#072227")
        self.drop.grid(row=2, column=1, pady=(20, 0))

        # # branchid drop down
        # # record = (self.clicked.get(),)
        # # mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        # # cursor = mydb.cursor()
        # # select_query = "SELECT branchid FROM course where sem=%s"
        # # cursor.execute(select_query, record)
        # # result = cursor.fetchall()
        # # self.ia2 = list(result)
        # self.ia2 = ['CSE', 'ISE']
        # self.clicked3.set("BRANCH_ID")
        # self.drop = tk.OptionMenu(self.frame, self.clicked3, *self.ia2)
        # self.drop.config(font=("times new roman", 12, "bold"), width=20, bd=0, height=2, bg="#4FBDBA", fg="#072227")
        # self.drop.grid(row=1, column=2, pady=(20, 0))

        # branchname drop down



        #MARKS ENTRY
        self.subm = tk.Label(self.frame, text="MARKS", font=("Roboto", 18), bg="#072227", fg="WHITE")
        self.subm.grid(row=3, column=0,pady=(20,0))

        self.subm_en = tk.Entry(self.frame, bd=5, textvariable=self.sub_m, bg="#072227", width=45, fg="#AEFEFF",
                          cursor="xterm #AEFEFF",
                          insertbackground="#AEFEFF", relief=GROOVE,
                          font=("comic sans", 15))
        self.subm_en.grid(row=3, column=1,pady=(20,0))

        # attendance ENTRY
        self.subat = tk.Label(self.frame, text="ATTENDANCE",font=("Roboto", 18), bg="#072227", fg="WHITE")
        self.subat.grid(row=4, column=0)

        self.subat_en = tk.Entry(self.frame, bd=5, textvariable=self.sub_at, bg="#072227", width=45, fg="#AEFEFF",
                          cursor="xterm #AEFEFF",
                          insertbackground="#AEFEFF", relief=GROOVE,
                          font=("comic sans", 15))
        self.subat_en.grid(row=4, column=1)


        self.btn = tk.Button(self.frame, text="SUBMIT",  font=("times new roman", 12, "bold"), width=20, height=2,
                             bg="#4FBDBA", fg="#072227",command=self.insert)
        self.btn.grid(row=5, columnspan=2, padx=(30, 10), pady=(30, 10))



    def insert(self):
        print(self.result[0][0])
        print(self.clicked.get())
        print(self.clicked2.get())
        print(self.sub_m.get())
        print(self.sub_at.get())
        print(self.usn.get())
        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        select = "select usn from student"
        cursor.execute(select)
        result = cursor.fetchall()
        print(result)
        a=False
        for i in result:
            print(i[0])
            if self.usn.get() == i[0]:
                a=True

        if a==True:
            mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
            cursor = mydb.cursor()
            insert_query="insert into enrolls values (%s,%s,%s,%s,%s)"
            record=(self.usn.get(),self.result[0][0],self.clicked2.get(),self.sub_m.get(),self.sub_at.get())
            cursor.execute(insert_query,record)
            insert_query1 = "update student set branch_id=(%s) where usn=(%s)"
            record1 = (self.clicked4.get(),self.usn.get())
            cursor.execute(insert_query1, record1)
            messagebox.showinfo("Successful","Marks & attendance updated")
            self.newWindow.destroy()
            mydb.commit()
        else:
            messagebox.showerror("Error", "USN not registered!!")
            self.newWindow.destroy()



#2ND OPTION OF STUDENT
class raiseissue:
    def __init__(self, root):
        self.root = root
        self.root.title("proctor")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="#072227")
        # self.root.attributes('-fullscreen', True)
        self.usn=tk.StringVar()
        self.frame = tk.Frame(self.root,bg="#072227")
        self.frame.place(relx=0.5,rely=0.5,anchor="center")

        self.frame1 = tk.Frame(self.root, bg="#072227")
        self.frame1.place(x=1075, y=100)
        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        cursor.execute("SELECT usn FROM student")
        result = cursor.fetchall()
        usns=list(result)
        print(usns)
        USN_n=list()
        for i in range(0,len(usns)):
            USN_n.append(usns[i][0])
        print(USN_n)


        # usn
        usn = tk.Label(self.frame, text="STUDENT'S USN:",
                       font=("Roboto", 18), bg="#072227", fg="WHITE")
        usn.grid(row=0, column=0, padx=(20, 0), pady=(20, 0))
        usn_en = ttkwidgets.autocomplete.AutocompleteEntry(self.frame,completevalues=USN_n, textvariable=self.usn,
                           font=("comic sans", 15))
        usn_en.config( background="#072227", width=45, foreground="black",
                           cursor="xterm #AEFEFF")
        usn_en.grid(row=0, column=1, pady=(20, 0), padx=(0, 20))


        #raise issue
        btn = tk.Button(self.frame, text="RAISE AN ISSSUE",width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", command=self.raise1)
        btn.grid(row=1, columnspan=5,padx=20, pady=(15, 40))

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",text="LOGOUT",
                             command=self.back)
        self.btn.grid(row=0, column=0, padx=10, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="GO BACK",
                             command=self.back2)
        self.btn.grid(row=0, column=1, padx=10, pady=10)

    def back(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = Login_System_Student(self.root)

    def back2(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = student(self.root)

    def raise1(self):
        self.frame.destroy()
        self.frame1.destroy()
        self.frame = tk.Frame(self.root,bg="#072227")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame1 = tk.Frame(self.root, bg="#072227")
        self.frame1.place(x=1075, y=100)
        self.clicked=tk.StringVar()
        self.tc_name = tk.StringVar()
        self.issue_id = random.randint(1000, 9999)
        self.clicked_te=tk.StringVar()


        #usn label
        usn_lb = tk.Label(self.frame, text="USN : ", font=("Roboto", 18), bg="#072227", fg="WHITE")
        usn_lb.grid(row=0, column=0, pady=(20, 0))
        usn_lb=tk.Label(self.frame,text=str(self.usn.get()),font=("Roboto", 18), bg="#072227", fg="WHITE")
        usn_lb.grid(row=0,column=1 , pady=(20, 0))


        #issue id label
        usn_lb = tk.Label(self.frame, text="ISSUE-ID : ", font=("Roboto", 18), bg="#072227", fg="WHITE")
        usn_lb.grid(row=0, column=2, pady=(20, 0))
        usn_lb = tk.Label(self.frame, text=self.issue_id,font=("Roboto", 18), bg="#072227", fg="WHITE")
        usn_lb.grid(row=0, column=3, pady=(20, 0))

        # Semester dropdown
        self.sem = ['Unable to attend test1', 'Unable to attend test2', 'Unable to attend test3', 'Cannot attend next week classes', 'Feeling sick', 'Hostel food not good', 'Hostel maintenance not good', 'Cannot understand subject1']
        self.clicked.set("Issues")
        self.drop = tk.OptionMenu(self.frame, self.clicked, *self.sem)
        self.drop.config(font=("times new roman", 12, "bold"), bd=0, width=40, height=2, bg="#4FBDBA", fg="#072227")
        self.drop.grid(row=1, column=0,padx=20)
        btn = tk.Button(self.frame, text="Other Issues", width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
                        command=self.other)
        btn.grid(row=1, column=1, padx=20)



        # #teacher name
        # tc = tk.Label(self.frame, text="ENTER PROCTOR NAME:",
        #               font=("Roboto", 18), bg="#072227", fg="WHITE")
        # tc.grid(row=2, column=0, pady=(20, 0))
        # tc_en = tk.Entry(self.frame, textvariable=self.tc_name,bd=3, bg="#072227", width=45, fg="#AEFEFF",
        #                   cursor="xterm #AEFEFF",
        #                   insertbackground="#AEFEFF", relief=GROOVE,
        #                   font=("comic sans", 15))
        # tc_en.grid(row=2, column=1, pady=(20, 0))

        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        select_query = "SELECT T_name FROM teacher"
        cursor.execute(select_query)
        result = cursor.fetchall()
        self.result = list(result)
        print(self.result)
        # print(self.result[0][0])
        # self.result = ['18MAT11', '18CHE12', '18CPS13', '18ELN14', '18ME15', '18CHEL16', '18CPL16']
        self.clicked_te.set("TEACHER-NAME")
        self.drop = tk.OptionMenu(self.frame, self.clicked_te, *self.result)
        self.drop.config(font=("times new roman", 12, "bold"), width=20, bd=0, height=2, bg="#4FBDBA", fg="#072227")
        self.drop.grid(row=1, column=2,padx=20 )


        #submit button
        btn = tk.Button(self.frame, text="SUBMIT", width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", command=self.submit)
        btn.grid(row=3, columnspan=4, pady=20)

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="LOGOUT",
                             command=self.back)
        self.btn.grid(row=0, column=0, padx=10, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="GO BACK",
                             command=self.back1)
        self.btn.grid(row=0, column=1, padx=10, pady=10)

    def back(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = Login_System_Student(self.root)

    def back1(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = raiseissue(self.root)

    def other(self):
        # Description
        iss = tk.Label(self.frame, text="ENTER ISSUE:",
                       font=("Roboto", 18), bg="#072227", fg="WHITE")
        iss.grid(row=3, column=0,pady=(20, 0))
        iss_en = tk.Entry(self.frame, textvariable=self.clicked, bd=3, bg="#072227", width=45, fg="#AEFEFF",
                          cursor="xterm #AEFEFF",
                          insertbackground="#AEFEFF", relief=GROOVE,
                          font=("comic sans", 15))
        iss_en.grid(row=3, column=1,pady=(20, 0))

    def submit(self):
        print(self.clicked_te.get())
        self.t_name = str(self.clicked_te.get())
        print(self.t_name)
        regex=re.compile(r'\w+')
        mo=regex.search(self.t_name)
        self.t_name=mo.group()


        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        select_query="SELECT T_id FROM teacher where T_name=(%s)"
        record=(self.t_name,)
        cursor.execute(select_query,record)
        result12 = cursor.fetchall()
        self.result12 = list(result12)
        if self.result12 == []:
            messagebox.showerror("Error","Invalid teacher name!")

        print(result12)
        status='Pending'
        iss_add='Not yet addressed'
        if self.clicked.get() =='Issues':
            messagebox.showerror("Error","All fields are required")
        else:
            print( self.result12[0][0])
            insert_query2 = "insert into issues values(%s,%s,%s)"
            record2 = (self.usn.get(),self.issue_id, self.result12[0][0])
            insert_query = "INSERT INTO has (usn, issue_id,t_id) SELECT usn, issue_id,t_id FROM issues  WHERE issue_id = (%s) LIMIT 1"
            record = (self.issue_id,)
            in_q="update has set t_id=(%s) where issue_id=(%s)"
            rec=(self.result12[0][0],self.issue_id)

            query = "update has set descr=(%s),stat=(%s),iss_add=(%s) where issue_id=(%s)"
            record1 = (self.clicked.get(), status,iss_add,self.issue_id)
            cursor.execute(insert_query2, record2)
            cursor.execute(in_q, rec)
            # print('inserted1')
            cursor.execute(insert_query, record)
            # print('inserted2')
            cursor.execute(query,record1)
            # print('inserted3')
            messagebox.showinfo("Issue","Issue Raised")


            mydb.commit()

#TEACHER FRONT PAGE

class teacher:
    def __init__(self, root):
        self.root = root
        self.root.title("teacher")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="#072227")
        # self.root.attributes('-fullscreen', True)

        #frame
        self.teacher_frame=tk.Frame(self.root,bg="#072227")
        self.teacher_frame.place(relx=0.5,rely=0.5,anchor="center")

        self.frame = tk.Frame(self.root, bg="#072227")
        self.frame.place(x=1075, y=100)

        #add student
        btn=tk.Button(self.teacher_frame,width=20, height=3,
                        font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",text="ADD STUDENT",command=self.new)

        btn.grid(row=0,column=0,padx=20,pady=10)

        # # add course
        # btn = tk.Button(self.teacher_frame,width=20, height=3,
        #                 font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",text="ADD COURSE", command=self.new1)
        # btn.grid(row=1, column=0, padx=20, pady=10)

        # view batch/students
        btn = tk.Button(self.teacher_frame, width=20, height=3,
                        font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="VIEW STUDENT", command=self.new2)
        btn.grid(row=2, column=0, padx=20, pady=10)

        # Resolve issues
        btn = tk.Button(self.teacher_frame, width=20, height=3,
                        font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="RESOLVE ISSUES", command=self.new3)
        btn.grid(row=3, column=0, padx=20, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame, width=20, height=2,
                        font=("Roboto", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="LOGOUT", command=self.back1)
        self.btn.grid(row=22, column=2, padx=10, pady=10)

    def back1(self):
        self.frame.destroy()
        self.teacher_frame.destroy()
        self.another = Login_System_Teacher(self.root)

    def new(self):
        self.frame.destroy()
        self.teacher_frame.destroy()
        self.another = addstudent(self.root)

    def new1(self):
        self.frame.destroy()
        self.teacher_frame.destroy()
        self.another = addcourse(self.root)

    def new2(self):
        self.frame.destroy()
        self.teacher_frame.destroy()
        self.another = viewstudent(self.root)

    def new3(self):
        self.frame.destroy()
        self.teacher_frame.destroy()
        self.another = resolveissues(self.root)

#ALLOWS TO AD STUDENT(TEACHER 1ST OPTION)
class addstudent:
    def __init__(self, root):
        self.root = root
        self.root.title("teacher")
        self.root.geometry("1350x700+0+0")

        self.usn = tk.StringVar()
        self.frame = tk.Frame(self.root,bg="#072227")
        self.frame.place(relx=0.5,rely=0.5,anchor="center")

        self.frame1 = tk.Frame(self.root, bg="#072227")
        self.frame1.place(x=1075, y=100)



        #USN
        usn = tk.Label(self.frame, text="STUDENT'S USN:",
                       font=("Roboto", 18), bg="#072227", fg="WHITE")
        usn.grid(row=0, column=0, pady=(20,0),padx=(20, 0))
        usn_en = tk.Entry(self.frame, textvariable=self.usn,  bd=3, width=45, bg="#072227", fg="#AEFEFF", cursor="xterm #AEFEFF",
                            insertbackground="#AEFEFF", relief=GROOVE,
                            font=("comic sans", 15))
        usn_en.grid(row=0, column=1, pady=(20,0),padx=(0, 20))

        # display
        self.listbox = tk.Listbox(self.frame, height=10,
                                  width=45,
                                  bg="#072227",
                                  activestyle='dotbox',
                                  font="Roboto",
                                  fg="#4FBDBA")




        # add student
        btn = tk.Button(self.frame,  width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="ADD STUDENT", command=self.add)
        btn.grid(row=1, columnspan=2, padx=10, pady=10)

        #show students
        btn = tk.Button(self.frame,  width=40, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",text="SHOW STUDENT'S LOGIN INFO", command=self.show)
        btn.grid(row=2, columnspan=2, padx=10, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="LOGOUT",
                             command=self.back)
        self.btn.grid(row=0, column=0, padx=10, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame1,  width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="GO BACK",
                             command=self.back2)
        self.btn.grid(row=0, column=1, padx=10, pady=10)

    def back(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = Login_System_Teacher(self.root)

    def back2(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = teacher(self.root)



    def add(self):
        self.listbox.destroy()
        self.listbox = tk.Listbox(self.frame, height=10,
                                  width=45,
                                  bg="#072227",
                                  activestyle='dotbox',
                                  font="Roboto",
                                  fg="#4FBDBA")

        self.btn.destroy()



        # delete students
        btn = tk.Button(self.frame, width=20, height=2, bg="#4FBDBA", fg="#072227",text="DELETE", command=self.delete)
        btn.grid(row=7, columnspan=3, padx=10, pady=10)

        pwd = random.randint(10000, 99999)
        pwd = str(pwd)
        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        cursor.execute("select usn from student")
        result=cursor.fetchall()
        print(result)
        for i in result:
            # print(i[0])
            if self.usn.get() == i[0]:
                messagebox.showerror("Error","Duplicate entry")
                break
        if len(self.usn.get()) == 10:
            mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
            cursor = mydb.cursor()
            insert_query = '''INSERT INTO student (usn,pwd) VALUES (%s,%s)'''
            record = (self.usn.get(), pwd)
            cursor.execute(insert_query, record)
            select_query = "select usn from student"
            cursor.execute(select_query)
            result = cursor.fetchall()
            n = 1
            for i in result:
                self.listbox.insert(n, i)
                self.listbox.grid(row=5, columnspan=2,padx=20,pady=20)
                n = n + 1
            messagebox.showinfo("Successful","Student Added!!")
            mydb.commit()
        else:
            messagebox.showerror("Error","USN should be of 10 characters!!")




    def delete(self):
        select = self.listbox.curselection()
        print(select)
        value=self.listbox.get(select[0])
        self.listbox.delete(select[0])
        record=(value[0],)
        print(record)
        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        delete_query = "delete from student where usn = %s"
        cursor.execute(delete_query,record)
        result = cursor.fetchall()
        n = 1
        for i, j in result:
            self.listbox.insert(n, i, j)
            self.listbox.grid(row=5, columnspan=2,padx=20,pady=20)
            n = n + 1
        messagebox.showinfo("Successful","Student deleted")
        mydb.commit()



    def show(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.frame = tk.Frame(self.root,bg="#072227")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.frame1 = tk.Frame(self.root, bg="#072227")
        self.frame1.place(x=1075, y=100)

        # display
        listbox = tk.Listbox(self.frame, height=10,
                             width=45,
                             bg="#072227",
                             activestyle='dotbox',
                             font="Roboto",
                             fg="#4FBDBA")
        listbox1 = tk.Listbox(self.frame, height=10,
                             width=45,
                             bg="#072227",
                             activestyle='dotbox',
                             font="Roboto",
                             fg="#4FBDBA")


        label = tk.Label(self.frame, text=" USN",font=("Roboto", 18), bg="#072227", fg="WHITE")
        label1 = tk.Label(self.frame, text=" PASSWORD", font=("Roboto", 18), bg="#072227", fg="WHITE")
        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        select_query1 = "select usn from student"
        cursor.execute(select_query1)
        result = cursor.fetchall()
        n = 1
        for i in result:
            listbox.insert(n, i)
            label.grid(row=4, column=0, padx=(20,0), pady=(20,0))
            listbox.grid(row=5, column=0, padx=(20,0), pady=20)
            n = n + 1

        select_query2 = "select pwd from student"
        cursor.execute(select_query2)
        result1 = cursor.fetchall()
        n = 1
        for i in result1:
            listbox1.insert(n, i)
            label1.grid(row=4, column=2, padx=(0,20), pady=(20,0))
            listbox1.grid(row=5, column=2, padx=(0,20), pady=20)
            n = n + 1

        mydb.commit()
        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2, bg="#4FBDBA", fg="#072227", text="LOGOUT",
                             command=self.back)
        self.btn.grid(row=0, column=0, padx=10, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2, bg="#4FBDBA", fg="#072227", text="GO BACK",
                             command=self.back1)
        self.btn.grid(row=0, column=1, padx=10, pady=10)

    def back(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = Login_System_Teacher(self.root)

    def back1(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = addstudent(self.root)

#ALLOWS TO ADD COURSE TO TEACCHER(2ND OPTION OF TEACHER)
# class addcourse:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("teacher")
#         self.root.geometry("1350x700+0+0")
#         self.root.configure(background="#072227")
#         # self.root.attributes('-fullscreen', True)
#         self.sub_code = tk.StringVar()
#         self.sub_name = tk.StringVar()
#         self.sem = tk.StringVar()
#         self.frame = tk.Frame(self.root,bg="#072227")
#         self.frame.place(relx=0.5, rely=0.5, anchor="center")
#
#         self.frame1 = tk.Frame(self.root, bg="#072227")
#         self.frame1.place(x=1075, y=100)
#
#
#         # sub_code
#         sub_code = tk.Label(self.frame, text="SUBJECT CODE:",
#                        font=("Roboto", 18), bg="#072227", fg="WHITE")
#         sub_code.grid(row=0, column=0, pady=(20, 0), padx=(20, 0))
#         sub_code_en = tk.Entry(self.frame, textvariable=self.sub_code, bd=3, bg="#072227", width=45, fg="#AEFEFF",
#                            cursor="xterm #AEFEFF",
#                            insertbackground="#AEFEFF", relief=GROOVE,
#                            font=("comic sans", 15))
#         sub_code_en.grid(row=0, column=1, pady=(20, 0), padx=(0, 20))
#
#         # sub_name
#         sub_name = tk.Label(self.frame, text="SUBJECT NAME:",
#                        font=("Roboto", 18), bg="#072227", fg="WHITE")
#         sub_name.grid(row=1, column=0, pady=(20, 0), padx=(20, 0))
#         sub_name_en = tk.Entry(self.frame, textvariable=self.sub_name,bd=3, bg="#072227", width=45, fg="#AEFEFF",
#                            cursor="xterm #AEFEFF",
#                            insertbackground="#AEFEFF", relief=GROOVE,
#                            font=("comic sans", 15))
#         sub_name_en.grid(row=1, column=1, pady=(20, 0), padx=(0, 20))
#
#         # sem
#         sem = tk.Label(self.frame, text="SEMESTER:",
#                        font=("Roboto", 18), bg="#072227", fg="WHITE")
#         sem.grid(row=2, column=0, pady=(20, 0), padx=(20, 0))
#         sem_en = tk.Entry(self.frame,  textvariable=self.sem, bd=3, bg="#072227", width=45, fg="#AEFEFF",
#                            cursor="xterm #AEFEFF",
#                            insertbackground="#AEFEFF", relief=GROOVE,
#                            font=("comic sans", 15))
#         sem_en.grid(row=2, column=1, pady=(20, 0), padx=(0, 20))
#         # branch_id
#         self.ia3 = ['CSE', 'ISE']
#         self.clicked4.set("BRANCH_ID")
#         self.drop = tk.OptionMenu(self.frame, self.clicked4, *self.ia3)
#         self.drop.config(font=("times new roman", 12, "bold"), width=20, bd=0, height=2, bg="#4FBDBA", fg="#072227")
#         self.drop.grid(row=3, column=0, pady=(20, 0))
#
#
#
#         # display
#         self.listbox = tk.Listbox(self.frame, height=10,
#                                   width=45,
#                                   bg="#072227",
#                                   activestyle='dotbox',
#                                   font="Roboto",
#                                   fg="#4FBDBA")
#
#         # add course
#         btn = tk.Button(self.frame, width=20, height=2,
#                         font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="ADD COURSE", command=self.add)
#         btn.grid(row=3, columnspan=2, padx=10, pady=10)
#
#         # show students
#         btn = tk.Button(self.frame, width=20, height=2,
#                         font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="SHOW COURSES", command=self.show)
#         btn.grid(row=4, columnspan=2, padx=10, pady=10)
#
#         # GO BACK
#         self.btn = tk.Button(self.frame1, width=20, height=2,
#                         font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="LOGOUT",
#                              command=self.back)
#         self.btn.grid(row=0, column=0, padx=10, pady=10)
#
#         # GO BACK
#         self.btn = tk.Button(self.frame1,  width=20, height=2,
#                         font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="GO BACK",
#                              command=self.back2)
#         self.btn.grid(row=0, column=1, padx=10, pady=10)
#
#     def back(self):
#         self.frame1.destroy()
#         self.frame.destroy()
#         self.another = Login_System_Teacher(self.root)
#
#     def back2(self):
#         self.frame1.destroy()
#         self.frame.destroy()
#         self.another = teacher(self.root)
#
#
#     def add(self):
#         self.frame1.destroy()
#         self.frame.destroy()
#         self.frame = tk.Frame(self.root, bg="#072227")
#         self.frame.place(relx=0.5, rely=0.5, anchor="center")
#         self.clicked4=tk.StringVar()
#
#
#         self.frame1 = tk.Frame(self.root, bg="#072227")
#         self.frame1.place(x=1075, y=100)
#         # GO BACK
#         self.btn = tk.Button(self.frame1, width=20, height=2,
#                              font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
#                              text="LOGOUT",
#                              command=self.back)
#         self.btn.grid(row=0, column=0, padx=10, pady=10)
#
#         # GO BACK
#         self.btn1 = tk.Button(self.frame1, width=20, height=2,
#                              font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
#                              text="GO BACK",
#                              command=self.back2)
#         self.btn1.grid(row=0, column=1, padx=10, pady=10)
#         self.listbox = tk.Listbox(self.frame, height=10,
#                                   width=45,
#                                   bg="#072227",
#                                   activestyle='dotbox',
#                                   font="Roboto",
#                                   fg="#4FBDBA")
#
#         # delete COURSE
#         btn = tk.Button(self.frame,width=20, height=2,
#                         font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="DELETE", command=self.delete)
#         btn.grid(row=9, columnspan=3, padx=10, pady=10)
#         mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
#         cursor = mydb.cursor()
#         select_query = "select sub_code from course"
#         cursor.execute(select_query)
#         result=cursor.fetchall()
#         for i in  result:
#             if self.sub_code.get()==i[0]:
#                 messagebox.showerror("Error","Duplicate entry!")
#                 break
#         if len(self.sub_code.get()) > 7 :
#             messagebox.showerror("Error","Sub Code can't be greater than 7 characters!!")
#         elif  len(self.sub_code.get()) < 6:
#             messagebox.showerror("Error", "Sub Code can't be less than 6 characters!!")
#         else:
#             mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
#             cursor = mydb.cursor()
#             insert_query = '''INSERT INTO consists VALUES (%s,%s,%s,%s)'''
#             record = (self.clicked4.get(),self.sub_code.get(), self.sub_name.get(),self.sem.get())
#             cursor.execute(insert_query, record)
#             select_query = "select sub_code from course"
#             cursor.execute(select_query)
#             messagebox.showinfo("Successful","Course Added!!")
#             result = cursor.fetchall()
#             n = 1
#             for i in result:
#                 self.listbox.insert(n, i)
#                 self.listbox.grid(row=5, columnspan=2,padx=20,pady=20)
#                 n = n + 1
#             mydb.commit()
#
#
#
#     def back(self):
#         self.frame1.destroy()
#         self.frame.destroy()
#         self.another = Login_System_Teacher(self.root)
#
#     def back2(self):
#         self.frame1.destroy()
#         self.frame.destroy()
#         self.another = teacher(self.root)
#
#
#
#
#     def delete(self):
#         select = self.listbox.curselection()
#         print(select)
#         value=self.listbox.get(select[0])
#         self.listbox.delete(select[0])
#         record=(value[0],)
#         print(record)
#         mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
#         cursor = mydb.cursor()
#         delete_query = "delete from course where sub_code = %s"
#         cursor.execute(delete_query,record)
#
#         result = cursor.fetchall()
#         n = 1
#         for i, j in result:
#             self.listbox.insert(n, i, j)
#             self.listbox.grid(row=5, columnspan=2,padx=20,pady=20)
#             n = n + 1
#         messagebox.showinfo("Successful", "Course deleted!!")
#         mydb.commit()
#
#
#
#
#     def show(self):
#         self.frame1.destroy()
#         self.frame.destroy()
#         self.frame = tk.Frame(self.root,bg="#072227")
#         self.frame.place(relx=0.5, rely=0.5, anchor="center")
#         self.frame1 = tk.Frame(self.root, bg="#072227")
#         self.frame1.place(x=1075, y=100)
#
#         # # display
#         # listbox = tk.Listbox(self.frame, height=10,
#         #                      width=45,
#         #                      bg="#072227",
#         #                      activestyle='dotbox',
#         #                      font="Roboto",
#         #                      fg="#4FBDBA")
#         # listbox1 = tk.Listbox(self.frame, height=10,
#         #                       width=45,
#         #                       bg="#072227",
#         #                       activestyle='dotbox',
#         #                       font="Roboto",
#         #                       fg="#4FBDBA")
#         # listbox2 = tk.Listbox(self.frame, height=10,
#         #                       width=45,
#         #                       bg="#072227",
#         #                       activestyle='dotbox',
#         #                       font="Roboto",
#         #                       fg="#4FBDBA")
#
#         # label = tk.Label(self.frame, text=" SUBJECT CODE",font=("Times new roman", 20, "bold"))
#         # label1 = tk.Label(self.frame, text=" SUBJECT NAME", font=("Times new roman", 20, "bold"))
#         # label2 = tk.Label(self.frame, text=" SEMESTER", font=("Times new roman", 20, "bold"))
#         # mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
#         # cursor = mydb.cursor()
#         #
#         # select_query1 = "select sub_code from course"
#         # cursor.execute(select_query1)
#         # result = cursor.fetchall()
#         # n = 1
#         # for i in result:
#         #     listbox.insert(n, i)
#         #     label.grid(row=4, column=0, padx=(20,0), pady=(20,0))
#         #     listbox.grid(row=5, column=0, padx=(20,0), pady=20)
#         #     n = n + 1
#         #
#         # select_query2 = "select sub_name from course"
#         # cursor.execute(select_query2)
#         # result = cursor.fetchall()
#         # n = 1
#         # for i in result:
#         #     listbox1.insert(n, i)
#         #     label1.grid(row=4, column=2,  pady=(20, 0))
#         #     listbox1.grid(row=5, column=2,  pady=20)
#         #     n = n + 1
#         #
#         # select_query3 = "select sem from course"
#         # cursor.execute(select_query3)
#         # result1 = cursor.fetchall()
#         # n = 1
#         # for i in result1:
#         #     listbox2.insert(n, i)
#         #     label2.grid(row=4, column=4, padx=(0,20), pady=(20,0))
#         #     listbox2.grid(row=5, column=4, padx=(0,20), pady=20)
#         #     n = n + 1
#         #
#         # mydb.commit()
#         mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
#         cursor = mydb.cursor()
#         select_query = "SELECT * FROM course "
#         cursor.execute(select_query)
#         result = cursor.fetchall()
#         details = list(result)
#
#         self.columns = ('SUBJECT CODE', 'SUBJECT NAME', 'SEMESTER')
#
#         style = ttk.Style()
#         style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
#                         font=('Calibri', 11),background="#072227",foreground = '#4FBDBA')  # Modify the font of the body
#         style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))  # Modify the font of the headings
#         style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
#
#         self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',style="mystyle.Treeview")
#
#         self.tree.heading('SUBJECT CODE', text='SUBJECT CODE')
#         self.tree.heading('SUBJECT NAME', text='SUBJECT NAME')
#         self.tree.heading('SEMESTER', text='SEMESTER')
#
#         for i in details:
#             self.tree.insert('', tk.END, values=i)
#
#         def item_selected(event):
#             for selected_item in self.tree.selection():
#                 item = self.tree.item(selected_item)
#                 record = item['values']
#                 print(record)
#                 print(item)
#
#         self.tree.bind('<<TreeviewSelect>>', item_selected)
#         self.tree.grid(row=4, column=0, sticky='nsew')
#
#         # add a scrollbar
#         self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
#         self.tree.configure(yscroll=self.scrollbar.set)
#         self.scrollbar.grid(row=4, column=1, sticky='ns')
#
#         # GO BACK
#         self.btn = tk.Button(self.frame1,  width=20, height=2,
#                         font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",text="LOGOUT",
#                              command=self.back)
#         self.btn.grid(row=0, column=0, padx=10, pady=10)
#
#         # GO BACK
#         self.btn = tk.Button(self.frame1, width=20, height=2,
#                         font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="GO BACK",
#                              command=self.back1)
#         self.btn.grid(row=0, column=1, padx=10, pady=10)
#
#     def back(self):
#         self.frame1.destroy()
#         self.frame.destroy()
#         self.another = Login_System_Teacher(self.root)
#
#     def back1(self):
#         self.frame1.destroy()
#         self.frame.destroy()
#         self.another = addcourse(self.root)

#ALLOWS TO VIEW STUDENT DETAILS(3RD OPTION OF TEACHER)
class viewstudent:
    def __init__(self, root):
        self.root = root
        self.root.title("teacher")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="#072227")
        # self.root.attributes('-fullscreen', True)
        self.usn = tk.StringVar()
        self.frame = tk.Frame(self.root,bg="#072227")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame1 = tk.Frame(self.root, bg="#072227")
        self.frame1.place(x=1075, y=100)


        #usn
        usn = tk.Label(self.frame, text="USN:",
                            font=("Roboto", 18), bg="#072227", fg="WHITE")
        usn.grid(row=0, column=0, pady=(20, 0), padx=(20, 0))
        usn_en = tk.Entry(self.frame,  textvariable=self.usn,bd=3, bg="#072227", width=45, fg="#AEFEFF",
                          cursor="xterm #AEFEFF",
                          insertbackground="#AEFEFF", relief=GROOVE,
                          font=("comic sans", 15))
        usn_en.grid(row=0, column=1, pady=(20, 0), padx=(0, 20))

        # show students
        btn = tk.Button(self.frame, width=40, height=2,
                             font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",text="SHOW STUDENT'S DETAILS", command=self.show)
        btn.grid(row=2, columnspan=2, padx=10, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                             font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="LOGOUT",
                             command=self.back)
        self.btn.grid(row=0, column=0, padx=10, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                             font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227", text="GO BACK",
                             command=self.back2)
        self.btn.grid(row=0, column=1, padx=10, pady=10)

    def back(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = Login_System_Teacher(self.root)

    def back2(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = teacher(self.root)


    def show(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.frame = tk.Frame(self.root,bg="#072227")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame1 = tk.Frame(self.root, bg="#072227")
        self.frame1.place(x=1075, y=100)

        # list1=['USN','NAME','ADDRESS','PHONE','EMAIL','PASSWORD','BLOOD GROUP','TENTH MARKS','TWELFTH MARKS','FATHER\'S NAME','MOTHER\'S NAME','PARENT\'S CONTACT NUMBER','YEAR OF ADMISSION','PARENT\'S EMAIL','DATE OF BIRTH']
        #
        #
        #
        #
        # # display
        # listbox = tk.Listbox(self.frame, height=10,
        #                      width=45,
        #                      bg="white",
        #                      activestyle='dotbox',
        #                      font="Helvetica",
        #                      fg="black")
        # listbox1 = tk.Listbox(self.frame, height=10,
        #                       width=45,
        #                       bg="white",
        #                       activestyle='dotbox',
        #                       font="Helvetica",
        #                       fg="black")
        #
        # label = tk.Label(self.frame, text=" TITLE", font=("Times new roman", 20, "bold"))
        # label1 = tk.Label(self.frame, text=" VALUES", font=("Times new roman", 20, "bold"))
        #
        #
        # mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        # cursor = mydb.cursor()
        #
        # select_query1 = "select * from student where usn=%s"
        # record = (self.usn.get(),)
        # cursor.execute(select_query1, record)
        # result = cursor.fetchall()

        # n = 1
        # for i in result:
        #     for j in i:
        #         if j == None:
        #             listbox1.insert(n, " None")
        #         listbox1.insert(n, j)
        #         label1.grid(row=4, column=1, padx=(0, 20), pady=(20, 0))
        #         listbox1.grid(row=5, column=1, padx=(0, 20), pady=20)
        #         n = n + 1
        #
        #
        # for i in list1:
        #     listbox.insert(n, i)
        #     label.grid(row=4, column=0, padx=(20, 0), pady=(20, 0))
        #     listbox.grid(row=5, column=0, padx=(20, 0), pady=20)
        #     n = n + 1
        #
        # mydb.commit()

        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()

        select_query1 = "select usn,name,address,phone,email,pwd,bgrp,m_ten from student where usn=%s"
        select_query2="select m_twel,fname,mname,p_numb,yoa,pemail,dob from student where usn=%s"
        record = (self.usn.get(),)
        cursor.execute(select_query1, record)
        result = cursor.fetchall()
        details = list(result)
        cursor.execute(select_query2, record)
        result = cursor.fetchall()
        details1 = list(result)


        self.columns = ('USN','NAME','ADDRESS','PHONE','EMAIL','PASSWORD','BLOOD GROUP','TENTH MARKS')
        self.columns1=('TWELTH MARKS','FATHER\'S NAME','MOTHER\'S NAME','PARENT\'S CONTACT NUMBER','YEAR OF ADMISSION','PARENT\'S EMAIL','DATE OF BIRTH')

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11), background="#072227", foreground='#4FBDBA')  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.tree = ttk.Treeview(self.frame, selectmode="extended", columns=self.columns, show='headings', style="mystyle.Treeview")
        self.tree1 = ttk.Treeview(self.frame, columns=self.columns1, show='headings', style="mystyle.Treeview")

        self.tree.heading('USN', text='USN')
        self.tree.column('USN', minwidth=0, width=100, stretch=NO)
        self.tree.heading('NAME', text='NAME')
        self.tree.column('NAME', minwidth=0, width=100, stretch=NO)
        self.tree.heading('ADDRESS', text='ADDRESS')
        self.tree.heading('PHONE', text='PHONE')
        self.tree.column('PHONE', minwidth=0, width=100, stretch=NO)
        self.tree.heading('EMAIL', text='EMAIL')
        self.tree.heading('PASSWORD', text='PASSWORD')
        self.tree.column('PASSWORD', minwidth=0, width=100, stretch=NO)
        self.tree.heading('BLOOD GROUP', text='BLOOD GROUP')
        self.tree.column('BLOOD GROUP', minwidth=0, width=100, stretch=NO)
        self.tree.heading('TENTH MARKS', text='TENTH MARKS')
        self.tree.column('TENTH MARKS', minwidth=0, width=100, stretch=NO)
        self.tree1.heading('TWELTH MARKS', text='TWELTH MARKS')
        self.tree1.column('TWELTH MARKS', minwidth=0, width=100, stretch=NO)
        self.tree1.heading('FATHER\'S NAME', text='FATHER\'S NAME')

        self.tree1.heading('MOTHER\'S NAME', text='MOTHER\'S NAME')

        self.tree1.heading('PARENT\'S CONTACT NUMBER', text='PARENT\'S CONTACT NUMBER')
        self.tree1.column('PARENT\'S CONTACT NUMBER', minwidth=0, width=100, stretch=NO)
        self.tree1.heading('YEAR OF ADMISSION', text='YEAR OF ADMISSION')

        self.tree1.heading('PARENT\'S EMAIL', text='PARENT\'S EMAIL')
        self.tree1.heading('DATE OF BIRTH', text='DATE OF BIRTH')
        self.tree1.column('DATE OF BIRTH', minwidth=0, width=100, stretch=NO)



        for i in details:
            self.tree.insert('', tk.END, values=i)
        for i in details1:
            self.tree1.insert('', tk.END, values=i)

        def item_selected(event):
            for selected_item in self.tree.selection():
                item = self.tree.item(selected_item)
                record = item['values']
                print(record)
                print(item)
        def item_selected(event):
            for selected_item in self.tree1.selection():
                item = self.tree1.item(selected_item)
                record = item['values']
                print(record)
                print(item)

        self.tree.bind('<<TreeviewSelect>>', item_selected)
        self.tree.grid(row=8, column=0, sticky='nsew')
        self.tree1.bind('<<TreeviewSelect>>', item_selected)
        self.tree1.grid(row=10, column=0, sticky='nsew')





        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                             font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
                             text="LOGOUT",
                             command=self.back)
        self.btn.grid(row=0, column=0, padx=10, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                             font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
                             text="GO BACK",
                             command=self.back1)
        self.btn.grid(row=0, column=1, padx=10, pady=10)

    def back(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = Login_System_Teacher(self.root)

    def back1(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = viewstudent(self.root)

#ALLOWS TO RESOLVE ISSUES(4TH OPTION OF TEACHER)
class resolveissues:
    def __init__(self, root):
        self.root = root
        self.root.title("teacher")
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="#072227")
        # self.root.attributes('-fullscreen', True)
        self.tid=tk.StringVar()
        self.frame = tk.Frame(self.root,bg="#072227")
        self.frame.place(relx=0.5,rely=0.5,anchor="center")

        self.frame1 = tk.Frame(self.root, bg="#072227")
        self.frame1.place(x=1075, y=100)

        self.clicked_te=tk.StringVar()


        # # teacher_id
        # tid = tk.Label(self.frame, text="ENTER TEACHER ID:",
        #                font=("Roboto", 18), bg="#072227", fg="WHITE")
        # tid.grid(row=0, column=0, pady=(20, 0), padx=(20, 0))
        # tid_en = tk.Entry(self.frame,  textvariable=self.tid, bd=3, bg="#072227", width=45, fg="#AEFEFF",
        #                   cursor="xterm #AEFEFF",
        #                   insertbackground="#AEFEFF", relief=GROOVE,
        #                   font=("comic sans", 15))
        # tid_en.grid(row=0, column=1, pady=(20, 0), padx=(0, 20))
        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        select_query = "SELECT T_id FROM teacher"
        cursor.execute(select_query)
        result = cursor.fetchall()
        self.result = list(result)
        print(self.result)
        # print(self.result[0][0])
        # self.result = ['18MAT11', '18CHE12', '18CPS13', '18ELN14', '18ME15', '18CHEL16', '18CPL16']
        self.clicked_te.set("TEACHER-ID")
        self.drop = tk.OptionMenu(self.frame, self.clicked_te, *self.result)
        self.drop.config(font=("times new roman", 12, "bold"), width=20, bd=0, height=2, bg="#4FBDBA", fg="#072227")
        self.drop.grid(row=2, column=0)

        # show students
        btn = tk.Button(self.frame, width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
                          text="SHOW ISSUES", command=self.show)
        btn.grid(row=2, column=1, padx=10)

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
                          text="LOGOUT",
                             command=self.back)
        self.btn.grid(row=0, column=0, padx=10, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                        font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
                          text="GO BACK",
                             command=self.back2)
        self.btn.grid(row=0, column=1, padx=10, pady=10)

    def back(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = Login_System_Teacher(self.root)

    def back2(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = teacher(self.root)

    def show(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.frame = tk.Frame(self.root,bg="#072227")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        self.frame1 = tk.Frame(self.root, bg="#072227")
        self.frame1.place(x=1075, y=100)
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11), background="#072227", foreground='#4FBDBA')  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        # display
        print(self.clicked_te.get())
        self.t_name = str(self.clicked_te.get())
        print(self.t_name)
        regex = re.compile(r'\w+')
        mo = regex.search(self.t_name)
        self.t_name = mo.group()
        print(self.t_name)
        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
        cursor = mydb.cursor()
        select_query="SELECT * FROM has where t_id=%s"
        self.record=(self.t_name,)
        cursor.execute(select_query,self.record)
        result = cursor.fetchall()
        issues = list(result)
        if issues == []:
            messagebox.showerror("Error","No Issues raised!")



        self.columns = ('USN', 'ISSUE_ID', 'DESCRIPTION','STATUS','SOLUTION')

        self.tree = ttk.Treeview(self.frame, columns=self.columns, show='headings',style="mystyle.Treeview")

        self.tree.heading('USN', text='USN')
        self.tree.heading('ISSUE_ID', text='ISSUE_ID')
        self.tree.heading('DESCRIPTION', text='DESCRIPTION')
        self.tree.heading('STATUS', text='STATUS')
        self.tree.heading('SOLUTION', text='SOLUTION')

        for i in issues:
            self.tree.insert('', tk.END, values=i)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        self.tree.grid(row=4, column=0, sticky='nsew')
        self.btn = tk.Button(self.frame, width=20, height=2,
                             font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
                             text="ADDRESS ISSUE",
                             command=self.address)
        self.btn.grid(row=6, column=0, padx=10)
        self.btn = tk.Button(self.frame, width=20, height=2,
                             font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
                             text="SEND EMAIL",
                             command=self.send)
        self.btn.grid(row=6, column=1, padx=10, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame1, width=20, height=2,
                             font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
                             text="LOGOUT",
                             command=self.back)
        self.btn.grid(row=0, column=0, padx=10, pady=10)

        # GO BACK
        self.btn = tk.Button(self.frame, width=20, height=2,
                             font=("times new roman", 12, "bold"), relief=GROOVE, bg="#4FBDBA", fg="#072227",
                             text="GO BACK",
                             command=self.back1)
        self.btn.grid(row=0, column=1, padx=10, pady=10)



    # def OnDoubleClick(self, event):
    #     item = self.tree.selection()[0]
    #     print("you clicked on", self.tree.item(item, "text"))

    def item_selected(self,event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            self.record = item['values']
            print(self.record)



    def address(self):
        self.newWindow = Toplevel(self.root)
        self.newWindow.title("Address Issue")
        self.newWindow.geometry("1000x700")
        self.newWindow.configure(background="#072227")
        self.frame_nw = tk.Frame(self.newWindow, bg="#072227")
        self.frame_nw.place(relx=.5, rely=.55, anchor="center")
        self.frame_nw1 = tk.Frame(self.newWindow, bg="#072227")
        self.frame_nw1.place(x=975, y=95)
        self.iss_add=tk.StringVar()

        self.label1=tk.Label(self.frame_nw,height=2,width=25,font=("Roboto", 18), bg="#072227", fg="WHITE",text="How is the issue addressed?")
        self.label1.grid(row=0,column=0)
        self.inputtxt = tk.Text(self.frame_nw,font=("Roboto", 18), bg="#072227", fg="WHITE",
                           height=10,

                           width=40)


        self.inputtxt.grid(row=1,column=0)

        # Button Creation

        self.printButton = tk.Button(self.frame_nw,
                                text="Submit",
                                command=self.soln)
        self.printButton.grid(row=2,column=0)

    def soln(self):
        self.inp = self.inputtxt.get(1.0, "end-1c")
        print(self.inp)
        print(self.record[1])
        record1 = (self.inp,self.record[1])

        mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123",database="proctor")
        cursor = mydb.cursor()
        select_query = "update has set stat='Solved',iss_add=(%s) where issue_id=(%s);"

        cursor.execute(select_query, record1)
        messagebox.showinfo("Successful","Issue Solved")
        mydb.commit()
        self.newWindow.destroy()
        self.frame_nw.destroy()
        self.frame_nw1.destroy()
        self.show()


    def send(self):
        try:

            s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
            s.starttls()
            s.login("tejasvirat72@gmail.com", "Tejasr@125")

            print(self.record[0])
            mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123", database="proctor")
            cursor = mydb.cursor()
            select_query = "select email from student where usn=(%s) "
            record1=(self.record[0],)
            cursor.execute(select_query, record1)
            result=cursor.fetchall()
            print(result)
            result=str(result)
            regex = re.compile(r'\w+@\w+.\w+')
            mo = regex.search(result)
            email = mo.group()
            print(email)

            s.sendmail("tejasvirat72@gmail.com",email, self.inp)
            messagebox.showinfo("Addressed message", f"Solution sent to {email}")
            s.quit()


        except:
            messagebox.showinfo("Send OTP via Email",
                                "Please enter the valid email address OR check an internet connection")




    #
    # def open(self):
    #     # print(self.record[1])
    #     record1 = (self.record[1],)
    #
    #     mydb = mysql.connector.connect(host="localhost", username="root", password="Root@123",
    #                                            database="proctor")
    #     cursor = mydb.cursor()
    #     select_query = "update has set stat='Pending' where issue_id=(%s);"
    #
    #     cursor.execute(select_query, record1)
    #     messagebox.showinfo("Successful","Issue Opened")
    #     mydb.commit()
    #     self.show()
    #








    def back(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = Login_System_Teacher(self.root)

    def back1(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.another = resolveissues(self.root)


root = tk.Tk()
obj = register(root)
root.mainloop()