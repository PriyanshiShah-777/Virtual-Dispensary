from tkinter import *
from tkinter.ttk import Combobox
import pyrebase
import requests
import geocoder
import time
import serial
from datetime import datetime
import webbrowser
from tkinter import messagebox
import tkinter as tk
import PIL.Image
from PIL import ImageTk,Image
from tkinter import filedialog
import speech_recognition as sr




now = datetime.now()
print("now =", now)

g = geocoder.ip('me')
print(g.latlng)
latitude = g.latlng[0]
longitutde = g.latlng[1]

bgColor = "#D0ECEB"
textColor = "#303030"
textFont = "calibri"
col = "#ffffff"
_height = 690
_width = 1300
btcl1 = "#d6999c"
btcl2 = "#ecd0d1"
var2=""
var3=""
var4=""
var5=""
my_img=""
speech = ""

ot = 0

class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual-Doctor")
        self.root.geometry("1300x690")
        # ====background image====
        self.root.resizable(False, False)
        self.root.configure(bg=bgColor)

        def back():
            start()
        def back_1():
            firstpg()
        home = Label(self.root, text="Health Monitoring System \n(User Side)", font=(textFont, 40, "bold"),
                     fg=textColor,bg=bgColor).place(x=350, y=200)
        bt2 = Button(self.root, text="Next", font=(textFont, 18, "bold"), fg="black", bg=btcl2, cursor='hand2',
                     command=back, width=14).place(x=550, y=390)


        uservalue1 = StringVar()
        passvalue1 = StringVar()

        uservalue = StringVar()
        passvalue = StringVar()

        tempvalue = StringVar()
        oxivalue = StringVar()
        otherDisease = StringVar()

        usernname = StringVar()
        age = StringVar()
        address = StringVar()
        dt_string = StringVar()
        a = 35
        b = 86
        config = {
            "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
            "authDomain": "pythonmelody.firebaseapp.com",
            "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
            "projectId": "pythonmelody",
            "storageBucket": "pythonmelody.appspot.com"
        }
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        global counter_name
        all_users = db.child("counter").get()
        counter_name = all_users.val()
        print("counter_name :" +str(counter_name))




        def createuser():
            if uservalue1.get() and passvalue1.get():
                print("Create User ....")
                print(uservalue1.get())
                print(passvalue1.get())
                auth = firebase.auth()
                # auth.create_user_with_email_and_password("niggaonstreet@gmail.com", "password")
                user = auth.create_user_with_email_and_password(uservalue1.get(), passvalue1.get())
                auth.get_account_info(user['idToken'])
                auth.create_user_with_email_and_password(uservalue1.get(), passvalue1.get())
                firstpg()

        def signin():
            global address_new
            if uservalue.get() and passvalue.get():
                global counter_name

                print(uservalue.get())
                print(passvalue.get())

                auth = firebase.auth()
                # auth.create_user_with_email_and_password("niggaonstreet@gmail.com", "password")
                user = auth.sign_in_with_email_and_password(uservalue.get(), passvalue.get())
                # uuid = auth.get_account_info(user['idToken'])['users'][0]['localId']
                counter_name += 1
                a2 = {"counter": counter_name}
                db.update(a2)
                print("c_value : " + str(counter_name))


                auth.get_account_info(user['idToken'])
                selectionpg()



        def check():
            if var.get() == 1:
                firstpg()
            elif var1.get() == 1:
                firstpg()
            else:
                messagebox.showinfo("showinfo","Please select the option")

        def start():
            f3 = Frame(bg=bgColor)
            f3.place(x=0, y=0, width=_width, height=_height)



            e8 = Label(f3, text="______________________________________________________________________________________________________________________________________", font=(textFont, 18, "bold"),
                           fg=textColor,
                           bg=bgColor).place(x=0, y=35)



            e8 = Label(f3, text="Health Monitoring System", font=(textFont, 26, "bold"),
                         fg=textColor,
                         bg=bgColor).place(x=440, y=70)
            e8 = Label(f3, text="Note : User can explain the problem he is facing in detail by our platform", font=(textFont, 10, "bold"),
                         fg=textColor,
                         bg=bgColor).place(x=435, y=110)

            home = Label(f3, text="“Medicine cure diseases but only doctors can cure patients.“ \n-Carl Jung",
                         font=(textFont, 16, "bold"), anchor="nw", justify=LEFT,
                         fg="black", bg=bgColor).place(x=30, y=200)
            home = Label(f3, text="“The best doctor gives the least medicines.”. \n– Benjamin Franklin",
                         font=(textFont, 16, "bold"), anchor="nw", justify=LEFT,
                         fg="black", bg=bgColor).place(x=30, y=300)
            home = Label(f3, text="“When you cry out in pain from a broken wrist, no one questions it."
                                  "\n You just go to the hospital and take the necessary steps."
                                  "\n Mental illness is just as real, even if it can't be seen”. \n– Torrey DeVitto",
                         font=(textFont, 16, "bold"), anchor="nw", justify=LEFT,
                         fg="black", bg=bgColor).place(x=30, y=400)
            home = Label(f3, text="WELCOME",font=(textFont, 30, "bold"), anchor="nw", justify=LEFT,
                         fg="black", bg=bgColor).place(x=800, y=180)

            lab1 = Label(f3, text="UserName : ", font=(textFont, 16, "bold"), fg=textColor, bg=bgColor).place(x=750,y=250)
            e1 = Entry(f3, font=(textFont, 14),borderwidth=1,relief="solid" ,textvariable=uservalue).place(x=750, y=280, width=320, height=30)

            lab2 = Label(self.root, text="Password : ", font=(textFont, 16, "bold"), fg=textColor, bg=bgColor).place(x=750,y=330)
            e2 = Entry(f3, font = (textFont, 14),borderwidth=1,relief="solid" , textvariable = passvalue).place(x=750, y=370,width=320,height=30)

            bt2 = Button(f3, text="Login", font=(textFont, 18, "bold"), fg="black", bg=btcl1, cursor='hand2',
            command = signin, width = 12).place(x=750, y=430)

            bt2 = Button(f3, text="SignUp", font=(textFont, 18, "bold"), fg="black", bg=btcl2,
            cursor = 'hand2',command = signup, width = 12).place(x=950, y=430)

            bt3 = Button(f3, text="Back", font=(textFont, 14, "bold"), fg="white", bg=textColor, cursor='hand2',
            command = root.quit, width =5,height=-1).place(x=20, y=10)


        def selectionpg():
            f3 = Frame(bg=bgColor)
            f3.place(x=0, y=0, width=_width, height=_height)
            e8 = Label(f3,
                       text="______________________________________________________________________________________________________________________________________",
                       font=(textFont, 18, "bold"),
                       fg=textColor,
                       bg=bgColor).place(x=0, y=35)

            home = Label(f3, text="Hii We are here to solve your Problem.",
                         font=(textFont, 25, "bold"), anchor="nw", justify=LEFT,
                         fg="black", bg=bgColor).place(x=150, y=12)
            global var
            global var1,var2,var3,var4,var5
            var = IntVar()
            var1 = IntVar()
            var2 = IntVar()
            var3 = IntVar()
            var4 = IntVar()
            var5 = IntVar()
            Label(f3, text="Select Doctor", font=(textFont, 20, "bold"), fg=textColor,
                  bg=bgColor).place(x=150, y=80)
            Label(f3, text="Note : Select doctor according to the avaibility time.", font=(textFont, 10), fg=textColor,
                  bg=bgColor).place(x=150, y=120)

            Label(f3, text="Note : Select new if you are visiting first time.", font=(textFont, 10), fg=textColor,
                  bg=bgColor).place(x=700, y=120)
            Label(f3, text="File type", font=(textFont, 20, "bold"), fg=textColor,
                  bg=bgColor).place(x=700, y=80)

            Checkbutton(f3, text="New",  variable=var,font=(textFont, 18, "bold"), fg=textColor, bg=bgColor).place(x=700, y=180)
            Checkbutton(f3, text="Old", variable=var1, font=(textFont, 18, "bold"), fg=textColor, bg=bgColor).place(x=830, y=180)
            Checkbutton(f3, text="\n\nDr Manav Shah \nSpecialist = Child Specialist\n Timing = 10:00AM to 5:00PM", variable=var2, font=(textFont, 14, "bold"), fg=textColor,
                        bg=bgColor).place(x=150,y=140)
            Checkbutton(f3, text="\n\nDr Mehul Modi \n Specialist = Skin Specialist\n Timing = 10:00AM to 3:00PM", variable=var3, font=(textFont, 14, "bold"), fg=textColor,
                        bg=bgColor).place(x=150 ,y=260)
            Checkbutton(f3, text="\n\nDr Sudhir Patel \n Specialist = Heart Specialist\n Timing = 10:00AM to 5:00PM", variable=var4, font=(textFont, 14, "bold"), fg=textColor,
                        bg=bgColor).place(x=150,y=380)
            Checkbutton(f3, text="\n\nDr Rahul Nuwal \n Specialist = Eye Specialist\n Timing = 10:00AM to 5:00PM", variable=var5, font=(textFont, 14, "bold"), fg=textColor,
                        bg=bgColor).place(x=150,y=500)
            bt2 = Button(f3, text="Next", font=(textFont, 16, "bold"), fg="black", cursor='hand2', bg=btcl1,
                         command=check, width=12).place(x= 700, y=550)
            bt3 = Button(f3, text="Back", font=(textFont, 12, "bold"), fg="white", cursor='hand2', bg=textColor,
                         command=back, width=5).place(x=20, y=15)

        def signup():
            print("sign up Page....")
            f3 = Frame(bg=bgColor)
            f3.place(x=0, y=0, width=_width, height=_height)
            e8 = Label(f3,
                       text="______________________________________________________________________________________________________________________________________",
                       font=(textFont, 18, "bold"),
                       fg=textColor,
                       bg=bgColor).place(x=0, y=60)

            title = Label(f3, text="Create Account", font=(textFont, 40, "bold", "underline"), fg=textColor,
                          bg=bgColor).place(x=400,y=10)
            lab1 = Label(f3, text="UserName : ", font=(textFont, 16, "bold"), fg=textColor, bg=bgColor).place(x=400,y=140)

            e1 = Entry(f3, font=(textFont, 14), textvariable=uservalue1).place(x=530, y=140)
            lab2 = Label(f3, text="Password : ", font=(textFont, 16, "bold"), fg=textColor, bg=bgColor).place(x=400,y=200)

            e1 = Entry(f3, font=(textFont, 14), textvariable=passvalue1).place(x=530, y=200)
            lab2 = Label(f3, text="Phone No. : ", font=(textFont, 16, "bold"), fg=textColor, bg=bgColor).place(x=400,y=280)
            e1 = Entry(f3, font=(textFont, 14)).place(x=530, y=280)
            lab2 = Label(f3, text="Gender : ", font=(textFont, 14, "bold"), fg=textColor, bg=bgColor).place(x=400,y=340)

            dropdown = Combobox(f3, font=(textFont, 13), values=["Female", "Male", "Others"]).place(x=530,
                                                                                                    y=340)

            bt2 = Button(f3, text="Create Now", font=(textFont, 18, "bold"), fg="black", bg=btcl1, cursor='hand2',
                         command=createuser, width=10).place(x=400, y=420)
            # title = Label(f2, text="OR", font=(textFont, 15), fg="#d25d17", bg="pink").place(x=300, y=325)
            bt2 = Button(f3, text="Login", font=(textFont, 18, "bold"), fg="black", bg=btcl2, cursor='hand2',
                         command=back, width=10).place(x=600, y=420)
            bt3 = Button(f3, text="Back", font=(textFont, 14, "bold"), fg="white", bg=textColor, cursor='hand2',
                         command=back, width=5,height=-1).place(x=20, y=10)
        def payment():
            webbrowser.open_new_tab('payment.html')
            finish()
        def pay():
            config = {
                "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
            "authDomain": "pythonmelody.firebaseapp.com",
            "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
            "projectId": "pythonmelody",
            "storageBucket": "pythonmelody.appspot.com"
            }
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()
            all_users = db.child(str(counter_name)).child("User Data").child("Case").get()
            for user in all_users.each():
                r_name = user.val()
            f3 = Frame(bg=bgColor)
            f3.place(x=0, y=0, width=_width, height=_height)
            if r_name == "New":
                Label(f3, text="Payment Voucher", font=(textFont, 22, "bold"), fg=textColor,
                      bg=bgColor).place(x=500, y=30)
                Label(f3, text="____________________________________________", font=(textFont, 22, "bold"), fg=textColor,
                      bg=bgColor).place(x=370, y=70)
                Label(f3, text="PV No : ", font=(textFont, 20, "bold"), fg=textColor,
                      bg=bgColor).place(x=400, y=120)
                Label(f3, text=str(counter_name), font=(textFont, 20, "bold"), fg=textColor,
                      bg=bgColor).place(x=480, y=120)
                Label(f3, text="Date : ", font=(textFont, 20, "bold"), fg=textColor,
                      bg=bgColor).place(x=650, y=120)
                dt_string1 = now.strftime("%d/%m/%Y ")
                Label(f3, text=dt_string1, font=(textFont, 20, "bold"), fg=textColor,
                      bg=bgColor).place(x=750, y=120)
                Label(f3, text="Sum Of Rupees : ", font=(textFont, 20, "bold"), fg=textColor,
                      bg=bgColor).place(x=400, y=170)
                Label(f3, text="500", font=(textFont, 20, "bold"), fg=textColor,
                      bg=bgColor).place(x=650, y=170)
                Label(f3, text="In Words : ", font=(textFont, 20, "bold"), fg=textColor,
                      bg=bgColor).place(x=400, y=220)
                Label(f3, text="Five Hundred Rupees", font=(textFont, 20, "bold"), fg=textColor,
                      bg=bgColor).place(x=650, y=220)
                Label(f3, text="Paid to : ", font=(textFont, 20, "bold"), fg=textColor,
                      bg=bgColor).place(x=400, y=270)
                if var2.get() == 1:
                    lab4 = Label(f3, text="Dr Manav Shah ", font=(textFont, 20,"bold"), bg=bgColor,
                                 fg=textColor).place(x=650,
                                                     y=270)
                elif var3.get() == 1:
                    lab4 = Label(f3, text="Dr Mehul Modi", font=(textFont, 20,"bold"), bg=bgColor,
                                 fg=textColor).place(x=650,
                                                     y=270)
                elif var4.get() == 1:
                    lab4 = Label(f3, text="Dr Sudhir Patel ", font=(textFont, 20,"bold"), bg=bgColor,
                                 fg=textColor).place(x=650,
                                                     y=270)
                elif var5.get() == 1:
                    lab4 = Label(f3, text="Dr Rahul Nuwal ", font=(textFont, 20,"bold"), bg=bgColor,
                                 fg=textColor).place(x=650,
                                                     y=270)
                Label(f3, text="On Account Of : ", font=(textFont, 20, "bold"), fg=textColor,
                      bg=bgColor).place(x=400, y=320)

                Label(f3, text=usernname.get(), font=(textFont, 20, "bold"), fg=textColor,
                          bg=bgColor).place(x=650, y=320)

            bt3 = Button(f3, text="Pay", font=(textFont, 14, "bold"), fg="white", bg=textColor, cursor='hand2',
                         command=payment, width=8, height=-1).place(x=600, y=500)

        def reading_temp():

            global ot
            if [list1.get(idx) for idx in list1.curselection()] or otherDisease.get():
                values = [list1.get(idx) for idx in list1.curselection()]
                print("Alist :: " + str(values))

                config = {
                    "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
            "authDomain": "pythonmelody.firebaseapp.com",
            "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
            "projectId": "pythonmelody",
            "storageBucket": "pythonmelody.appspot.com"
                }
                firebase = pyrebase.initialize_app(config)
                db = firebase.database()
                storage = firebase.storage()

                i = 1
                db.child(str(counter_name)).child("User Data").child("Disease List").remove()
                db.child(str(counter_name)).child("User Data").child("Commented Disease").remove()

                # sending selected disease...
                for val in values:
                    print(val)
                    print(i)
                    a1 = {"Disease " + str(i): str(val)}

                    db.child(str(counter_name)).child("User Data").child("Disease List").update(a1)
                    i = i + 1

                # sending commented disease...
                print("otottt :: " + str(ot))
                global speech
                if (ot == 0):
                    a2 = {"Comment": otherDisease.get()}
                    db.child(str(counter_name)).child("User Data").child("Commented Disease").update(a2)
                elif (ot == 1):
                    a2 = {"Comment": speech}
                    db.child(str(counter_name)).child("User Data").child("Commented Disease").update(a2)
                else:
                    a2 = {"Comment": "No description"}
                    db.child(str(counter_name)).child("User Data").child("Commented Disease").update(a2)


                a7 = {"Name": usernname.get()}
                db.child(str(counter_name)).child("User Data").child("Paitents name").update(a7)

                a8 = {"Age": age.get()}
                db.child(str(counter_name)).child("User Data").child("Age").update(a8)

                a17 = {"Address": address.get()}
                db.child(str(counter_name)).child("User Data").child("Address").update(a17)
                global my_img


                if v.get() == 1:
                    a18 = {"Video Call": "Yes"}
                    db.child(str(counter_name)).child("User Data").child("Video Call").update(a18)

                elif v1.get()==1:
                    a18 = {"Video Call": "No"}
                    db.child(str(counter_name)).child("User Data").child("Video Call").update(a18)
                else:
                    messagebox.showinfo("show info","Select the Option")
                if var.get()==1:
                    a19 = {"Case": "New"}
                    db.child(str(counter_name)).child("User Data").child("Case").update(a19)
                elif var1.get()==1:
                    a19 = {"Case": "Old"}
                    db.child(str(counter_name)).child("User Data").child("Case").update(a19)



                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print("date and time =", dt_string)
                a8 = {"Time": dt_string}
                db.child(str(counter_name)).child("User Data").child("Entry Time").update(a8)

                # sending temperature value...
                # a = tempvalue.get()
                print('temperature Value :: ' + str(a))
                a1 = {"Temperature": int(a)}
                db.child(str(counter_name)).child("User Data").child("Sensor Data").update(a1)

                # sending oxigen value...
                # b = oxivalue.get()
                # b = 28
                print('Oxi Value :: ' + str(b))
                b1 = {"Spo2": int(b)}
                db.child(str(counter_name)).child("User Data").child("Sensor Data").update(b1)

                config = {
                    "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
                    "authDomain": "pythonmelody.firebaseapp.com",
                    "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
                    "projectId": "pythonmelody",
                    "storageBucket": "pythonmelody.appspot.com"
                }
                firebase = pyrebase.initialize_app(config)
                db = firebase.database()
                user1 = db.child("payment").get()
                c1 = user1.val()
                print(c1)
                if c1 == "failure":
                    pay()
                elif c1 == "success":
                    finish()



        def firstpg():



            f3 = Frame(bg=bgColor)
            f3.place(x=0, y=0, width=_width, height=_height)

            e8 = Label(f3,
                       text="______________________________________________________________________________________________________________________________________",
                       font=(textFont, 18, "bold"),
                       fg=textColor,
                       bg=bgColor).place(x=0, y=25)

            # lab2 = Label(f3, text="Please select the issues that you are facing, so we can help you!",
            #              font=(textFont, 16), bg=bgColor, fg="#000000").place(x=135, y=20)
            lab9 = Label(f3, text="Select the Disease :",font=(textFont, 14,"bold"), bg=bgColor, fg=textColor).place(x=500, y=100)


            # f4 = Frame()
            # f4.pack()
            #
            global list1
            global commentEntry
            list1 = Listbox(f3, selectmode=MULTIPLE,borderwidth=1,relief="solid")
            list1.place(x=500, y=270,height=80,width=350)
            # list1.insert(1, "Cough")
            # list1.insert(2, "Fever")
            # list1.insert(3, "Joints Pain")
            # list1.insert(4, "Cold")
            # list1.insert(5, "Loose Motion")
            # list1.insert(6, "Headache")
            # list1.insert(7, "Vomiting")
            # list1.configure(font=(textFont, 14))
            # list1.grid(row=50, column=90)
            # list1.pack()
            def speak():
                global ot

                r = sr.Recognizer()
                print(sr.Microphone.list_microphone_names())
                global speech


                with sr.Microphone() as source:
                    ot = 1
                    r.adjust_for_ambient_noise(source, duration=1)
                    # r.energy_threshold()
                    print("say anything : ")
                    audio = r.listen(source)
                    try:
                        global speech
                        speech = r.recognize_google(audio)
                        print(speech)

                        lab4 = Label(f3, text=speech, borderwidth=1,relief="solid",font=(textFont, 14, "bold"),
                                     bg=bgColor, fg=textColor, background="#FFFFFF").place(x=500, y=490, width=350, height=80)
                    except:
                        print("sorry, could not recognise")



            lab4 = Label(f3, text="Explain the problem you are facing in detail.", font=(textFont, 17,"bold"),
                         bg=bgColor, fg=textColor).place(x=30, y=700)

            lab4 = Label(f3, text="Description about Disease :", font=(textFont, 14,"bold"),
                         bg=bgColor, fg=textColor).place(x=500, y=370)

            commentEntry = Entry(f3, font=(textFont, 14), textvariable=otherDisease,borderwidth=1,relief="solid").place(x=500, y=410, width=350, height=80)

            bt4 = Button(f3, text="Speak", font=(textFont, 10, "bold"), fg="white", cursor='hand2', bg=textColor,
                         command=speak, width=5).place(x=805, y=465)

            lab5 = Label(f3, text="Name: ", font=(textFont, 14,"bold"),bg=bgColor, fg=textColor).place(x=50, y=100)
            p_name = Entry(f3, font=(textFont, 14), textvariable=usernname,borderwidth=1,relief="solid").place(x=50, y=130, width=380,height=30)

            lab6 = Label(f3, text="Age: ", font=(textFont, 14,"bold"),bg=bgColor, fg=textColor).place(x=50, y=180)
            a_name = Entry(f3, font=(textFont, 14), textvariable=age,borderwidth=1,relief="solid").place(x=50, y=210, width=380,height=30)

            lab7 = Label(f3, text="Address: ", font=(textFont, 14,"bold"),bg=bgColor, fg=textColor).place(x=50, y=260)
            global address_new
            ad_name = Entry(f3, font=(textFont, 14),textvariable =address,borderwidth=1,relief="solid").place(x=50, y=290, width=380,height=40)

            lab8 = Label(f3, text="Want Video Call: ", font=(textFont, 14,"bold"), bg=bgColor, fg=textColor).place(x=50, y=350)
            global v, v1
            v = IntVar()
            v1 = IntVar()
            Checkbutton(f3, text="Yes", variable=v, font=(textFont, 18, "bold"), fg=textColor, bg=bgColor).place(x=50, y=380)
            Checkbutton(f3, text="No", variable=v1, font=(textFont, 18, "bold"), fg=textColor, bg=bgColor).place(x=270, y=380)



            if var2.get() == 1:

                lab4 = Label(f3, text="Doctor Name : ", font=(textFont, 14,"bold"), bg=bgColor, fg=textColor).place(x=950, y=100)
                lab4 = Label(f3, text="Dr Manav Shah ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,y=130)

                lab4 = Label(f3, text="Specialist : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950, y=180)
                lab4 = Label(f3, text="Child Specialist", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,y=210)

                lab4 = Label(f3, text="Address : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950, y=250)
                lab4 = Label(f3, text="Sanjeevni Multispeciality Hospital,\n Udhana - Magdalla Rd,\n Surat, Gujarat 395007", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,y=280)

                lab4 = Label(f3, text="Phone No : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950, y=360)
                lab4 = Label(f3, text="098241 28460 ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,y=390)

                lab4 = Label(f3, text="Timing : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950, y=440)
                lab4 = Label(f3, text="10AM to 5PM ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,y=470)

                lab4 = Label(f3, text="Status : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,y=520)
                lab4 = Label(f3, text="Open ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950, y=550)
            elif var3.get() == 1:
                lab4 = Label(f3, text="Doctor Name : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950, y=100)
                lab4 = Label(f3, text="Dr Mehul Modi ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,y=130)

                lab4 = Label(f3, text="Specialist : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950, y=180)
                lab4 = Label(f3, text="Skin Specialist", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,y=210)

                lab4 = Label(f3, text="Address : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,y=250)
                lab4 = Label(f3,text="5th Floor, Gandhi Smruti Vacant b/s Mahavir hospital,\n Nanpura, Surat, Gujarat 395001",
                             font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950, y=280)

                lab4 = Label(f3, text="Phone No : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,y=360)
                lab4 = Label(f3, text="099252 28151 ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,y=390)

                lab4 = Label(f3, text="Timing : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,y=440)
                lab4 = Label(f3, text="10AM to 3PM ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950, y=470)

                lab4 = Label(f3, text="Status : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,y=520)
                lab4 = Label(f3, text="Open ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950, y=550)
            elif var4.get() == 1:
                lab4 = Label(f3, text="Doctor Name : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(
                    x=950, y=100)
                lab4 = Label(f3, text="Dr Sudhir Patel ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,
                                                                                                             y=130)

                lab4 = Label(f3, text="Specialist : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(
                    x=950, y=180)
                lab4 = Label(f3, text="Heart Specialist", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,
                                                                                                              y=210)

                lab4 = Label(f3, text="Address : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,
                                                                                                                 y=250)
                lab4 = Label(f3,
                             text="Pumping Station, Anand Apartment,\n Dhobi Sheri, Sayedpura, Surat, Gujarat 395003",                             font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950, y=280)

                lab4 = Label(f3, text="Phone No : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,
                                                                                                                  y=360)
                lab4 = Label(f3, text="081282 53811 ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,
                                                                                                            y=390)

                lab4 = Label(f3, text="Timing : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,
                                                                                                                y=440)
                lab4 = Label(f3, text="10AM to 5PM ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950, y=470)

                lab4 = Label(f3, text="Status : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,
                                                                                                                y=520)
                lab4 = Label(f3, text="Open ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950, y=550)
            elif var5.get() == 1:
                lab4 = Label(f3, text="Doctor Name : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(
                    x=950, y=100)
                lab4 = Label(f3, text="Dr Rahul Shah ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,
                                                                                                               y=130)

                lab4 = Label(f3, text="Specialist : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(
                    x=950, y=180)
                lab4 = Label(f3, text="Eye Specialist", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,
                                                                                                               y=210)

                lab4 = Label(f3, text="Address : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,
                                                                                                                 y=250)
                lab4 = Label(f3,
                             text="Pumping Station, Anand Apartment,\n Dhobi Sheri, Sayedpura, Surat, Gujarat 395003",
                             font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950, y=280)

                lab4 = Label(f3, text="Phone No : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,
                                                                                                                  y=360)
                lab4 = Label(f3, text="081282 53811 ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950,
                                                                                                            y=390)

                lab4 = Label(f3, text="Timing : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,
                                                                                                                y=440)
                lab4 = Label(f3, text="10AM to 5PM ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950, y=470)

                lab4 = Label(f3, text="Status : ", font=(textFont, 14, "bold"), bg=bgColor, fg=textColor).place(x=950,
                                                                                                                y=520)
                lab4 = Label(f3, text="Open ", font=(textFont, 14), bg=bgColor, fg=textColor).place(x=950, y=550)


            # print(commentEntry.get())
            bt2 = Button(f3, text="Submit", font=(textFont, 16, "bold"), fg="black", cursor='hand2', bg=btcl1,
                         command=reading_temp, width=12).place(x=50, y=530)
            bt3 = Button(f3, text="Back", font=(textFont, 14, "bold"), fg="white", bg=textColor, cursor='hand2',
                         command=back, width=5,height=0).place(x=20, y=10)
            home = Label(f3, text = usernname.get(),font=(textFont, 14, "bold"),bg=bgColor, fg=textColor).place(x=800,y=20,width=280)


            def on_keyrelease(event):
                # get text from entry
                value = event.widget.get()
                value = value.strip().lower()

                # get data from test_list
                if value == '':
                    data = test_list
                else:
                    data = []
                    for item in test_list:
                        if value in item.lower():
                            data.append(item)

                            # update data in listbox
                listbox_update(data)

            def listbox_update(data):
                # delete previous data
                listbox.delete(0, 'end')

                # sorting data
                data = sorted(data, key=str.lower)

                # put new data
                for item in data:
                    listbox.insert('end', item)

            def on_select(event):
                # display element selected on list
                entry.delete(0,'end')
                entry.insert(0,listbox.get(ACTIVE))
                print('(event) previous:', event.widget.get('active'))
                print('(event)  current:', event.widget.get(event.widget.curselection()))
                print('---')

            # --- main ---

            test_list = (
            ' Anes', ' Asthma', ' Anxiety', ' Arthritis', ' Bone Cancer', ' Blood Poisoning', ' Binge Eating', ' Chicken Pox', 'Chest pain', 'Common Cold', 'Cold Sore', 'Dehydration', 'Diabeties', 'Depression', 'Dry Mouth', 'Diastonia'
            'Eye Cancer','Epilepsy', 'Earache', 'Flu', 'Fever', 'Food Poisoning', 'Gum Disease', 'Gout',
            'Chicken Pox', 'Headache','Hay Fever', 'Hearing Loss', 'Insomnia', 'Indigestion', 'Itching', 'Kidney Stone','Cough','Malaria','Typhoid','Dengue'
            )

            def delete():
                list1.delete(ANCHOR)
            def add():

                list1.insert(END,entry.get())

            entry = Entry(f3, font=(textFont, 14),borderwidth=1,relief="solid")

            entry.place(x=500, y=130, width=300)
            entry.bind('<KeyRelease>', on_keyrelease)


            my_scrollbar = Scrollbar(f3, orient=VERTICAL, command=Listbox.yview)
            listbox = Listbox(f3,borderwidth=1,relief="solid", yscrollcommand=my_scrollbar.set)
            listbox.place(x=500,y=170,height=80,width=350)
            my_scrollbar.config(command=listbox.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)
            # listbox.bind('<Double-Button-1>', on_select)
            listbox.bind('<<ListboxSelect>>', on_select)
            listbox_update(test_list)
            bt4  = Button(f3, text="Add", font=(textFont, 10, "bold"), fg="white", cursor='hand2', bg=textColor,
                         command=add, width=5).place(x=800, y=130)
            bt5 = Button(f3, text="Delete", font=(textFont, 10, "bold"), fg="white", cursor='hand2', bg=textColor,
                         command=delete, width=5).place(x=805, y=322)
            # global listbox1
            # listbox1 = Listbox(f3)
            # listbox1.place(x=450,y=250)

        def reading_pulse():
            if tempvalue.get():
                config = {
                    "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
            "authDomain": "pythonmelody.firebaseapp.com",
            "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
            "projectId": "pythonmelody",
            "storageBucket": "pythonmelody.appspot.com"
                }
                firebase = pyrebase.initialize_app(config)
                db = firebase.database()
                # a = 55
                a = tempvalue.get()
                print('temperature Value :: ' + str(a))
                a1 = {"Temperature": int(a)}
                db.child(str(counter_name)).child("User Data").child("Sensor Data").update(a1)

                f3 = Frame(bg=bgColor)
                f3.place(x=0, y=0, width=_width, height=_height)
                lab4 = Label(f3, text="Please hold the pulse sensor gently", font=(textFont, 26), bg=bgColor,
                             fg=textColor).place(
                    x=180,
                    y=150)
                e4 = Entry(f3, textvariable=oxivalue, font=(textFont, 26)).place(x=180, y=200)
                bt2 = Button(f3, text=" Send ", font=(textFont, 18, "bold"), fg="white", cursor='hand2', bg=textColor,
                             command=finish, width=14).place(x=180, y=265)

                bt = Button(root, text="Back", font=(textFont, 14, "bold"), fg="black", cursor='hand2', bg=bgColor,
                            activebackgroun=bgColor, command=reading_temp, bd=0).place(x=15, y=15)

        def stream_handler(message):
            # print(message["event"]) # put
            # print(message["path"]) # /-K7yGTTEp7O549EzTYtI
            # print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
            print(message["path"] + " - " + str(message["data"]))
            if (str(message["data"]) != "None"):
                showdocresponse(str(message["data"]))

        def done():

            config = {
                "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
            "authDomain": "pythonmelody.firebaseapp.com",
            "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
            "projectId": "pythonmelody",
            "storageBucket": "pythonmelody.appspot.com"
            }
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()
            db.child(str(counter_name)).child("Dr Data").remove()
            print("patient data removed")
            root.destroy()

        def call():

            config = {
                "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
            "authDomain": "pythonmelody.firebaseapp.com",
            "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
            "projectId": "pythonmelody",
            "storageBucket": "pythonmelody.appspot.com"
            }
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()
            call = db.child(str(counter_name)).child("Dr Data/Video Link/link").get()
            url = call.val()
            print("calling on link - " + str(url))
            webbrowser.open(str(url))

        def showdocresponse(prescription):
            print("prescription =  " + prescription)
            config = {
                "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
            "authDomain": "pythonmelody.firebaseapp.com",
            "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
            "projectId": "pythonmelody",
            "storageBucket": "pythonmelody.appspot.com"
            }
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()
            all_users = db.child(str(counter_name)).child("Dr Data").child("Medicine").get()
            for user in all_users.each():
                m_name = user.val()
            print(m_name)
            all_users = db.child(str(counter_name)).child("Dr Data").child("Message").get()
            for user in all_users.each():
                send_name = user.val()
            print(send_name)

            all_users = db.child(str(counter_name)).child("Dr Data").child("Meeting Time").get()
            for user in all_users.each():
                me_name = user.val()
            print(me_name)
            all_users = db.child(str(counter_name)).child("Dr Data").child("Code").get()
            for user in all_users.each():
                c_name = user.val()
            print(c_name)
            all_users = db.child(str(counter_name)).child("Dr Data").child("Diet").get()
            for user in all_users.each():
                d_name = user.val()
            print(d_name)
            all_users = db.child(str(counter_name)).child("Dr Data").child("Avoid").get()
            for user in all_users.each():
                avoid_name = user.val()
            print(avoid_name)

            if str(send_name)=="Again":
                f3 = Frame(bg=bgColor)
                f3.place(x=0, y=0, width=_width, height=_height)
                e8 = Label(f3,
                           text="______________________________________________________________________________________________________________________________________",
                           font=(textFont, 18, "bold"),
                           fg=textColor,
                           bg=bgColor).place(x=0, y=45)

                Label(f3, text="Message:", font=(textFont, 18, "bold", "underline"),
                      bg=bgColor, fg=textColor).place(x=30,y=50)
                Label(f3, text=str(send_name), font=(textFont, 16),
                      bg=bgColor, fg=textColor, wraplength=400, justify=LEFT, ).place(x=30,y=70)
                Button(f3, text="Send Again", font=(textFont, 18, "bold"), fg="black", cursor='hand2', bg="#E0E0E0",
                       activebackgroun=bgColor, command=back, width=14).place(x=30, y=300)

            else:
                f3 = Frame(bg=bgColor)
                f3.place(x=0, y=0, width=_width, height=_height)


                Label(f3, text="Doctor's Name ", font=(textFont, 18, "bold", "underline"),
                      bg=bgColor, fg=textColor).place(x=30,y=20)
                if var2.get()==1:
                    lab4 = Label(f3, text="Dr Manav Shah ", font=(textFont, 20),bg=bgColor, fg=textColor).place(x=30,
                                                             y=70)
                elif var3.get()==1:
                    lab4 = Label(f3, text="Dr Mehul Modi ", font=(textFont, 20),bg=bgColor, fg=textColor).place(x=30,
                                                             y=70)
                elif var4.get()==1:
                    lab4 = Label(f3, text="Dr Sudhir Patel ", font=(textFont, 20),bg=bgColor, fg=textColor).place(x=30,
                                                             y=70)
                elif var5.get()==1:
                    lab4 = Label(f3, text="Dr Rahul Nuwal ", font=(textFont, 20),bg=bgColor, fg=textColor).place(x=30,
                                                             y=70)
                Label(f3, text="Doctor's Prescription :", font=(textFont, 18, "bold", "underline"),
                      bg=bgColor, fg=textColor).place(x=30,y=170)
                Label(f3, text= prescription, font=(textFont, 20),
                      bg=bgColor, fg=textColor, wraplength=400, justify=LEFT, ).place(x=30,
                                                                                      y=220)
                Label(f3, text="Medicine Name :", font=(textFont, 18, "bold", "underline"),
                      bg=bgColor, fg=textColor).place(x=30,
                                                      y=320)
                Label(f3, text=str(m_name), font=(textFont, 20),
                      bg=bgColor, fg=textColor, wraplength=400, justify=LEFT, ).place(x=30,
                                                                                      y=370)
                Label(f3, text="Meeting Time", font=(textFont, 18, "bold", "underline"),
                      bg=bgColor, fg=textColor).place(x=30,
                                                      y=470)
                Label(f3, text=str(me_name), font=(textFont, 20),
                      bg=bgColor, fg=textColor, wraplength=400, justify=LEFT, ).place(x=30,
                                                                                      y=510)
                Label(f3, text="Unique Code", font=(textFont, 18, "bold", "underline"),
                      bg=bgColor, fg=textColor).place(x=550,
                                                      y=20)
                Label(f3, text=c_name, font=(textFont, 20),
                      bg=bgColor, fg=textColor, wraplength=400, justify=LEFT, ).place(x=550,
                                                                                      y=70)
                Label(f3, text="Diet For Patient", font=(textFont, 18, "bold", "underline"),
                      bg=bgColor, fg=textColor).place(x=550,
                                                      y=150)
                Label(f3, text=d_name, font=(textFont, 20),
                      bg=bgColor, fg=textColor, wraplength=400, justify=LEFT, ).place(x=550,
                                                                                      y=190)
                Label(f3, text="To Avoid", font=(textFont, 18, "bold", "underline"),
                      bg=bgColor, fg=textColor).place(x=550,
                                                      y=280)
                Label(f3, text=avoid_name, font=(textFont, 20),
                      bg=bgColor, fg=textColor, wraplength=400, justify=LEFT, ).place(x=550,
                                                                                      y=330)
                Button(f3, text="Exit", font=(textFont, 18, "bold"), fg="black", cursor='hand2', bg="#E0E0E0",
                       activebackgroun=bgColor, command=done, width=14).place(x=30, y=600)
                Button(f3, text="Call", font=(textFont, 18, "bold"), fg="black", cursor='hand2', bg="#E0E0E0",
                       activebackgroun=bgColor, command=call, width=14).place(x=280, y=600)
                print("Stream stopped")

        def finish():
            if True:
                # config = {
                #     "apiKey": "AIzaSyDqzY3riaf_oerVYIS72cU4GW5ywXNqWxs",
                #     "authDomain": "projectc-5c725.firebaseapp.com",
                #     "databaseURL": "https://projectc-5c725-default-rtdb.firebaseio.com/",
                #     "storageBucket": "projectc-5c725.appspot.com"
                # }
                # firebase = pyrebase.initialize_app(config)
                # db = firebase.database()
                # b = oxivalue.get()
                # # b = 28
                # print('Oxi Value :: ' + str(b))
                # b1 = {"Sp2": int(b)}
                # db.child("User Data").child("Sensor Data").update(b1)

                f3 = Frame(bg=bgColor)
                f3.place(x=0, y=0, width=_width, height=_height)
                e8 = Label(f3,
                           text="______________________________________________________________________________________________________________________________________",
                           font=(textFont, 18, "bold"),
                           fg=textColor,
                           bg=bgColor).place(x=0, y=25)

                if var2.get()==1:
                    lab4 = Label(f3, text="Dr Manav Shah will reply you soon", font=(textFont, 20),bg=bgColor, fg=textColor).place(x=30,
                                                             y=100)
                elif var3.get()==1:
                    lab4 = Label(f3, text="Dr Mehul Modi will reply you soon", font=(textFont, 20),bg=bgColor, fg=textColor).place(x=30,
                                                             y=100)
                elif var4.get()==1:
                    lab4 = Label(f3, text="Dr Sudhir Patel will reply you soon", font=(textFont, 20),bg=bgColor, fg=textColor).place(x=30,
                                                             y=100)
                elif var5.get()==1:
                    lab4 = Label(f3, text="Dr Rahul Nuwal will reply you soon", font=(textFont, 20),bg=bgColor, fg=textColor).place(x=30,
                                                             y=100)
                else:
                    lab4 = Label(f3, text="Please select the consultant doctor", font=(textFont, 24), bg=bgColor,
                                 fg=textColor).place(x=30,
                                                     y=150)
                lab4 = Label(f3, text="Please wait............", font=(textFont, 24), bg=bgColor,
                             fg=textColor).place(x=30,
                                                 y=220)
                lab4 = Label(f3, text="If you want to send another response", font=(textFont, 24), bg=bgColor,
                             fg=textColor).place(x=30,
                                                 y=300)



                config = {
                    "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
            "authDomain": "pythonmelody.firebaseapp.com",
            "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
            "projectId": "pythonmelody",
            "storageBucket": "pythonmelody.appspot.com"
                }
                firebase = pyrebase.initialize_app(config)
                db = firebase.database()
                print("streaming started")
                my_stream = db.child(str(counter_name)).child("Dr Data/Prescription/Prescription").stream(stream_handler)

                bt2 = Button(f3, text="Send it again", font=(textFont, 18, "bold"), fg="white", cursor='hand2',
                             bg=textColor,
                             command=firstpg).place(x=30, y=390,width=150)
                bt3 = Button(f3, text="Back", font=(textFont, 14, "bold"), fg="white", bg=textColor, cursor='hand2',
                             command=back_1, width=8).place(x=20, y=10)





        # finish()
        # firstpg()
        # showdocresponse("A long Prescription is there you have to read it carefully and do what ever you want... go to hell")

        # webbrowser.open('https://meet.google.com/qdd-waft-npi')
        # a = 0
        # b = 0

        # auth = firebase.auth()
        # user = auth.create_user_with_email_and_password("ap0288938@gmail.com", "password")
        # auth.create_user_with_email_and_password(id, passw)
        # info = auth.get_account_info(user['idToken'])

        # print(user)


root = Tk()
obj = login(root)
root.mainloop()
