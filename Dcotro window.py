from tkinter import *
from tkinter.ttk import Combobox
import pyrebase
from tkinter import messagebox
import random
import math
import matplotlib.pyplot as plt
import time
import serial
import webbrowser
import pandas as pd
import seaborn as sns
from PIL import ImageTk,Image




bum = []


# Disease List / Disease 1
# colors primary :: fcf9f4
# colors secondary ::  1a0

c_name = ""
bgColor = "#adf3b2"
textColor = "#303030"
textFont = "calibri"
_height = 690
_width = 1300
pen = 0
count = ""
btcl1 = "#d6999c"
btcl2 = "#ecd0d1"
import csv


class login:

    def __init__(self, root):
        self.root = root
        self.root.title("Virtual-doctor")
        self.root.geometry("1300x690")
        # ====background image====
        self.root.resizable(False, False)
        self.root.configure(bg=bgColor)

        def back():
            start()

        def back_1():
            firstpg()

        def back_2():
            writePrescription()
        def back_3():
            secondpg()

        home = Label(self.root, text="Health Monitoring System \n(Doctor Side)", font=(textFont, 40, "bold"),
                     fg=textColor,bg=bgColor).place(x=350, y=200)
        bt2 = Button(self.root, text="Next", font=(textFont, 18, "bold"), fg="black", bg=btcl2, cursor='hand2',
                     command=back, width=14).place(x=550, y=390)
        uservalue1 = StringVar()
        passvalue1 = StringVar()

        uservalue = StringVar()
        passvalue = StringVar()
        drLink = StringVar()
        count = IntVar()

        p_name = StringVar()
        var = IntVar()
        prescriptionText = StringVar()
        medicinename = StringVar()
        timing = StringVar()
        Diet = StringVar()
        Avoid = StringVar()
        oxivalue = StringVar()
        patient_name = StringVar()

        sensorData = list()
        name = list()
        diseaseList = list()
        commentDisases = "NO Comment Found..."

        # ser = serial.Serial('COM3', 9600)
        # ser.baudrate = 9600
        a = 0
        b = 0
        # ch = ser.readline()
        # a = float(ch[0:4])
        # b = float(ch[6:10])
        print("sent {0} {1}".format(a, b))

        config = {
            "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
            "authDomain": "pythonmelody.firebaseapp.com",
            "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
            "projectId": "pythonmelody",
            "storageBucket": "pythonmelody.appspot.com"
        }
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()

        def check1():
            # count=0
            global count

            a1 = (patient_name.get())
            print(a1)

            count = str(a1)

            print(str(count))
            firstpg()

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
            # firstpg()

            if uservalue.get() and passvalue.get():
                config = {
                    "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
                    "authDomain": "pythonmelody.firebaseapp.com",
                    "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
                    "projectId": "pythonmelody",
                    "storageBucket": "pythonmelody.appspot.com"
                }
                firebase = pyrebase.initialize_app(config)
                db = firebase.database()

                print(uservalue.get())
                print(passvalue.get())

                auth = firebase.auth()
                # auth.create_user_with_email_and_password("niggaonstreet@gmail.com", "password")
                user = auth.sign_in_with_email_and_password(uservalue.get(), passvalue.get())
                auth.get_account_info(user['idToken'])
                secondpg()

                # car_df = pd.read_csv("result.csv", encoding="ISO-8859-1")
                # sns.pairplot(car_df)

        def show():
            global counter_name
            all_users = db.child("counter").get()
            counter_name = all_users.val()
            list1 = []
            list1.append("Disease")
            list2 = []
            list2.append("Age")
            for i in range(1, counter_name + 1):
                try:
                    all_user1 = db.child(str(i)).child("User Data").child("Disease List").child(str("Disease 1")).get()
                    list1.append(all_user1.val().strip())
                    all_user2 = db.child(str(i)).child("User Data").child("Age").child("Age").get()
                    list2.append(all_user2.val())
                    print(all_user1.val())
                except:
                    print("No values")
                try:
                    all_user1 = db.child(str(i)).child("User Data").child("Disease List").child(str("Disease 2")).get()
                    list1.append(all_user1.val().strip())
                    all_user2 = db.child(str(i)).child("User Data").child("Age").child("Age").get()
                    list2.append(all_user2.val())
                    print(all_user1.val())
                except:
                    print("No values")
                try:
                    all_user1 = db.child(str(i)).child("User Data").child("Disease List").child(str("Disease 3")).get()
                    list1.append(all_user1.val().strip())
                    all_user2 = db.child(str(i)).child("User Data").child("Age").child("Age").get()
                    list2.append(all_user2.val())
                    print(all_user1.val())
                except:
                    print("No values")


            print(list1)

            with open('result.csv', 'w') as output:
                output_data = csv.writer(output)
                output_data.writerows(zip(list1, list2))
            df = pd.read_csv('result.csv')
            x = df['Disease']
            y = df['Age']
            plt.subplot(1, 2, 1)
            plt.xlabel('Disease', fontsize=18)
            plt.ylabel('Age', fontsize=16)
            plt.bar(x, y)
            plt.subplot(1, 2, 2)
            plt.pie(y, labels=x, radius=1.1, autopct='%0.01f%%', shadow=True)
            # plt.plot(x, y)
            # plt.scatter(x,y)
            plt.show()


        def signup():
            print("sign up Page....")
            f3 = Frame(bg=bgColor)
            f3.place(x=0, y=0, width=_width, height=_height)
            e8 = Label(f3,
                       text="______________________________________________________________________________________________________________________________________",
                       font=(textFont, 18, "bold"),
                       fg=textColor,
                       bg=bgColor).place(x=0, y=70)

            title = Label(f3, text="Create Account", font=(textFont, 50, "bold", "underline"),
                          fg=textColor, bg=bgColor).place(x=400, y=10)
            lab1 = Label(f3, text="UserName : ", font=(textFont, 14, "bold"), fg=textColor, bg=bgColor).place(
                x=400, y=140)

            e1 = Entry(f3, font=(textFont, 14), borderwidth=1, relief="solid", textvariable=uservalue1).place(x=530,
                                                                                                              y=140)
            lab2 = Label(f3, text="Password : ", font=(textFont, 14, "bold"), fg=textColor, bg=bgColor).place(
                x=400, y=200)

            e1 = Entry(f3, font=(textFont, 14), borderwidth=1, relief="solid", textvariable=passvalue1).place(x=530,
                                                                                                              y=200)
            lab2 = Label(f3, text="Phone No. : ", font=(textFont, 14, "bold"), fg=textColor, bg=bgColor).place(
                x=400, y=280)
            e1 = Entry(f3, font=(textFont, 14), borderwidth=1, relief="solid").place(x=530, y=280)
            lab2 = Label(f3, text="Gender : ", font=(textFont, 14, "bold"), fg=textColor, bg=bgColor).place(x=400,
                                                                                                            y=340)

            dropdown = Combobox(f3, font=(textFont, 13), values=["Female", "Male", "Others"]).place(x=530, y=340)
            bt2 = Button(f3, text="Create Now", font=(textFont, 18, "bold"), fg="black", bg=btcl1, cursor='hand2',
                         command=createuser, width=14).place(x=400, y=420)

            bt2 = Button(f3, text="Login", font=(textFont, 18, "bold"), fg="black", bg=btcl2, cursor='hand2',
                         command=back_3, width=14).place(x=600, y=420)
            bt3 = Button(f3, text="Back", font=(textFont, 14, "bold"), fg="white", bg=textColor, cursor='hand2',
                         command=back, width=5, height=-1).place(x=20, y=20)

        def check():
            if var.get() == 1:
                secondpg()
            elif var1.get() == 1:
                secondpg()
            else:
                messagebox.showinfo("showinfo", "Please select the option")

        def start():
            f2 = Frame(bg=bgColor)
            f2.place(x=0, y=0, width=_width, height=_height)
            e8 = Label(f2,
                       text="______________________________________________________________________________________________________________________________________",
                       font=(textFont, 18, "bold"),
                       fg=textColor,
                       bg=bgColor).place(x=0, y=35)

            e8 = Label(f2, text="Health Monitoring System", font=(textFont, 26, "bold"),
                       fg=textColor, bg=bgColor).place(x=450, y=70)
            e8 = Label(f2, text="Doctors are the well being of human kind",
                       font=(textFont, 10, "bold"),
                       fg=textColor,
                       bg=bgColor).place(x=530, y=120)

            home = Label(f2, text="“Medicine cure diseases but only doctors can cure patients.“ -Carl Jung",
                         font=(textFont, 16, "bold"), anchor="nw", justify=LEFT,
                         fg="black", bg=bgColor).place(x=50, y=180)
            image1 = Image.open("docnew.gif")
            test = ImageTk.PhotoImage(image1)
            label1 = Label(f2, image=test,borderwidth=0,highlightthickness=0)
            label1.image = test

            label1.place(x=30, y=220)

            home = Label(f2, text="WELCOME DOCTOR", font=(textFont, 25, "bold"), anchor="nw", justify=LEFT,
                         fg="black", bg=bgColor).place(x=780, y=180)
            home = Label(f2, text="Login to see patient logs", font=(textFont, 10, "bold"), anchor="nw", justify=LEFT,
                         fg="black", bg=bgColor).place(x=840, y=220)
            lab1 = Label(f2, text="UserName : ", font=(textFont, 16, "bold"), fg=textColor, bg=bgColor).place(x=750,
                                                                                                              y=250)
            e1 = Entry(f2, font=(textFont, 14), borderwidth=1, relief="solid", textvariable=uservalue).place(x=750,
                                                                                                             y=280,
                                                                                                             width=320,
                                                                                                             height=30)
            lab2 = Label(self.root, text="Password : ", font=(textFont, 16, "bold"), fg=textColor, bg=bgColor).place(
                x=750, y=330)
            e2 = Entry(f2, font=(textFont, 14), borderwidth=1, relief="solid", textvariable=passvalue).place(x=750,
                                                                                                             y=370,
                                                                                                             width=320,
                                                                                                             height=30)
            bt2 = Button(f2, text="Login", font=(textFont, 18, "bold"), fg="black", bg=btcl1, cursor='hand2',
                         command=signin, width=12).place(x=750, y=430)
            bt2 = Button(f2, text="SignUp", font=(textFont, 18, "bold"), fg="black", bg=btcl2,
                         cursor='hand2', command=signup, width=12).place(x=950, y=430)
            bt3 = Button(f2, text="Back", font=(textFont, 14, "bold"), fg="white", bg=textColor, cursor='hand2',
                         command=f2.quit, width=5, height=0).place(x=20, y=10)

        def selectionpg():
            f3 = Frame(bg=bgColor)
            f3.place(x=0, y=0, width=_width, height=_height)
            e8 = Label(f3,
                       text="______________________________________________________________________________________________________________________________________",
                       font=(textFont, 18, "bold"),
                       fg=textColor,
                       bg=bgColor).place(x=0, y=30)
            global var
            global var1
            var = IntVar()
            var1 = IntVar()
            global counter_name
            all_users = db.child("counter").get()
            counter_name = all_users.val()
            print("counter_name :" + str(counter_name))

            # if c_name == "New":
            #     pen = 0
            # else:
            #     pen = 1
            Checkbutton(f3, text="Pending", variable=var1, font=(textFont, 20, "bold"), fg=textColor, bg=bgColor).place(
                x=150, y=180)
            Checkbutton(f3, text="Consulted", variable=var, font=(textFont, 20, "bold"), fg=textColor,
                        bg=bgColor).place(x=150, y=280)
            e8 = Label(f3, text="(" + str(counter_name) + ")", font=(textFont, 20, "bold"), fg=textColor,
                       bg=bgColor).place(x=400, y=180)
            bt2 = Button(f3, text="Next", font=(textFont, 16, "bold"), fg="black", cursor='hand2', bg=btcl1,
                         command=check, width=12).place(x=590, y=550)
            bt3 = Button(f3, text="Back", font=(textFont, 16, "bold"), fg="white", cursor='hand2', bg=textColor,
                         command=back, width=5).place(x=20, y=10)
            bt2 = Button(f3, text="Show Graph", font=(textFont, 16, "bold"), fg="black", cursor='hand2', bg=btcl1,
                         command=show, width=12).place(x=790, y=100)


        def sendagain():
            global count
            config = {
                "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
                "authDomain": "pythonmelody.firebaseapp.com",
                "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
                "projectId": "pythonmelody",
                "storageBucket": "pythonmelody.appspot.com"
            }
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()

            a2 = {"Message": "Again"}
            db.child(str(count)).child("Dr Data").child("Message").update(a2)

        def secondpg():
            global all_users
            config = {
                "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
                "authDomain": "pythonmelody.firebaseapp.com",
                "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
                "projectId": "pythonmelody",
                "storageBucket": "pythonmelody.appspot.com"
            }
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()

            f3 = Frame(bg=bgColor)
            f3.place(x=0, y=0, width=_width, height=_height)
            global counter_name
            all_users = db.child("counter").get()
            counter_name = all_users.val()
            print("counter_name :" + str(counter_name))
            j = 150

            image1 = Image.open("graph.gif")
            test = ImageTk.PhotoImage(image1)
            label1 = Label(f3, image=test,borderwidth=0,highlightthickness=0)
            label1.image = test

            label1.place(x=680, y=200)

            print(str(count))
            lab4 = Label(f3,
                       text="______________________________________________________________________________________________________________________________________",
                       font=(textFont, 18, "bold"),
                       fg=textColor,
                       bg=bgColor).place(x=0, y=30)


            lab4 = Label(f3, text="Patient Logs", font=(textFont, 25, "bold"), bg=bgColor,
                         fg=textColor).place(x=160, y=10)



            lab4 = Label(f3, text="Patient Name", font=(textFont, 20, "bold"), bg=bgColor,
                         fg=textColor).place(x=100, y=100)
            lab4 = Label(f3, text="Entry Time", font=(textFont, 20, "bold"), bg=bgColor,
                         fg=textColor).place(x=400, y=100)

            for i in range(1, counter_name + 1):
                all_users = db.child(str(i)).child("User Data").child("Paitents name").child("Name").get()
                print(all_users.val())

                lab4 = Label(f3, text=str(i) + ")" + str(all_users.val()), font=(textFont, 18), bg=bgColor,
                             fg=textColor).place(x=100, y=j)

                all_users = db.child(str(i)).child("User Data").child("Entry Time").child("Time").get()
                print(all_users.val())

                lab4 = Label(f3, text=str(all_users.val()), font=(textFont, 18), bg=bgColor,
                             fg=textColor).place(x=400, y=j)
                j += 70

            lab4 = Label(f3, text="Which patients data you want to see", font=(textFont, 30, "bold"), bg=bgColor,
                         fg=textColor).place(x=60, y=430)
            lab4 = Label(f3, text="Note : Enter number associated with paitent, to see the data.", font=(textFont, 11), bg=bgColor,
                         fg=textColor).place(x=70, y=480)
            e2 = Entry(f3, font=(textFont, 14), borderwidth=1, relief="solid", textvariable=patient_name).place(x=70,
                                                                                                                y=520,
                                                                                                                width=140,
                                                                                                                height=30)

            bt2 = Button(f3, text="Next", font=(textFont, 16, "bold"), fg="black", cursor='hand2', bg=btcl1,
                         command=check1, width=12).place(x=70, y=555)
            bt3 = Button(f3, text="Back", font=(textFont, 16, "bold"), fg="white", cursor='hand2', bg=textColor,
                         command=back, width=6).place(x=15, y=10)


            lab4 = Label(f3, text="Statistics", font=(textFont, 25, "bold"), bg=bgColor,
                         fg=textColor).place(x=790, y=95)

            bt2 = Button(f3, text="Show Graph", font=(textFont, 16, "bold"), fg="black", cursor='hand2', bg=btcl1,
                         command=show, width=12).place(x=790, y=160)

        def firstpg():

            global count

            config = {
                "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
                "authDomain": "pythonmelody.firebaseapp.com",
                "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
                "projectId": "pythonmelody",
                "storageBucket": "pythonmelody.appspot.com"
            }
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()

            # getting sensor Data.....
            print(str(count))
            all_users = db.child(str(count)).child("User Data").child("Sensor Data").get()
            for user in all_users.each():
                sensorData.append(user.val())
                # print(user.key())  # Morty
                # print(user.val())  # {name": "Mortimer 'Morty' Smith"}

            print(sensorData)

            # getting disease list
            all_users = db.child(str(count)).child("User Data").child("Disease List").get()
            for user in all_users.each():
                diseaseList.append(user.val())
                # print(user.key())  # Morty
                # print(user.val())  # {name": "Mortimer 'Morty' Smith"}

            print(diseaseList)

            # getting comment of user
            all_users = db.child(str(count)).child("User Data").child("Commented Disease").get()

            for user in all_users.each():
                commentDisases = user.val()
                # print(user.key())  # Morty
                # print(user.val())  # {name": "Mortimer 'Morty' Smith"}

            print(commentDisases)
            global c_name
            all_users = db.child(str(count)).child("User Data").child("Case").get()
            for user in all_users.each():
                c_name = user.val()
            print(c_name)

            all_users = db.child(str(count)).child("User Data").child("Entry Time").get()
            for user in all_users.each():
                e_name = user.val()
            print(e_name)

            all_users = db.child(str(count)).child("User Data").child("Paitents name").get()
            for user in all_users.each():
                p_name = user.val()
            print(p_name)

            all_users = db.child(str(count)).child("User Data").child("Age").get()
            for user in all_users.each():
                ag_name = user.val()
            print(ag_name)

            all_users = db.child(str(count)).child("User Data").child("Address").get()
            for user in all_users.each():
                ad_name = user.val()
            print(ad_name)

            all_users = db.child(str(count)).child("User Data").child("Video Call").get()
            for user in all_users.each():
                v_name = user.val()
            print(v_name)

            f3 = Frame(bg=bgColor)
            f3.place(x=0, y=0, width=_width, height=_height)
            e8 = Label(f3,
                       text="______________________________________________________________________________________________________________________________________",
                       font=(textFont, 18, "bold"),
                       fg=textColor,
                       bg=bgColor).place(x=0, y=30)
            lab4 = Label(f3, text="Data of Patient", font=(textFont, 32, "bold"), bg=bgColor,
                         fg=textColor).place(x=500, y=10)

            lab5 = Label(f3, text="Personal data of patient ", font=(textFont, 18, "bold"),
                         bg=bgColor, fg=textColor).place(x=50, y=80)

            lab5 = Label(f3, text="Case: ", font=(textFont, 16, "bold"),
                         bg=bgColor, fg=textColor).place(x=60, y=120)

            e5 = Label(f3, text=str(c_name), font=(textFont, 14), bg=bgColor,
                       fg=textColor).place(x=70, y=150)

            lab6 = Label(f3, text="Entry Time : ", font=(textFont, 16, "bold"),
                         bg=bgColor, fg=textColor).place(x=60, y=180)

            e6 = Label(f3, text=str(e_name), font=(textFont, 14), bg=bgColor,
                       fg=textColor).place(x=70, y=210)

            lab7 = Label(f3, text="Patients Name : ", font=(textFont, 16, "bold"),
                         bg=bgColor, fg=textColor).place(x=520, y=120)

            e7 = Label(f3, text=str(p_name), font=(textFont, 14), bg=bgColor,
                       fg=textColor).place(x=520, y=150)

            lab8 = Label(f3, text="Age : ", font=(textFont, 16, "bold"),
                         bg=bgColor, fg=textColor).place(x=520, y=180)

            e8 = Label(f3, text=str(ag_name), font=(textFont, 14), bg=bgColor,
                       fg=textColor).place(x=520, y=210)

            lab9 = Label(f3, text="Address : ", font=(textFont, 16, "bold"),
                         bg=bgColor, fg=textColor).place(x=60, y=240)

            e9 = Label(f3, text=str(ad_name), font=(textFont, 14), bg=bgColor,
                       fg=textColor).place(x=70, y=270)

            lab10 = Label(f3, text="Video Call : ", font=(textFont, 16, "bold"),
                          bg=bgColor, fg=textColor).place(x=520, y=240)

            e10 = Label(f3, text=str(v_name), font=(textFont, 14), bg=bgColor,
                        fg=textColor).place(x=520, y=270)


            e8 = Label(f3,
                       text="_____________________________________________________________________",
                       font=(textFont, 18, "bold"),
                       fg=textColor,
                       bg=bgColor).place(x=20, y=300)

            lab4 = Label(f3, text="Disease description", font=(textFont, 18, "bold"), bg=bgColor,
                         fg=textColor).place(x=50, y=340)

            lab4 = Label(f3, text="Sensor Data :", font=(textFont, 16, "bold"), bg=bgColor,
                         fg=textColor).place(x=70, y=380)

            lab4 = Label(f3, text="Temperature", font=(textFont, 16), bg=bgColor,
                         fg=textColor).place(x=70, y=410)

            lab4 = Label(f3, text=str(sensorData[1]) + " 'C", font=(textFont, 16), bg=bgColor,
                         fg=textColor).place(x=240, y=410)

            lab4 = Label(f3, text="Oxigen SPO2", font=(textFont, 16), bg=bgColor,
                         fg=textColor).place(x=70, y=440)

            lab4 = Label(f3, text=str(sensorData[0]), font=(textFont, 18), bg=bgColor,
                         fg=textColor).place(x=240, y=440)

            lab4 = Label(f3, text="Disease patient facing:", font=(textFont, 18, "bold"), bg=bgColor,
                         fg=textColor).place(x=520, y=380)

            i = 410
            for val in diseaseList:
                lab4 = Label(f3, text="- " + val, font=(textFont, 16), bg=bgColor,
                             fg=textColor).place(
                    x=520, y=i)
                i = i + 30

            lab4 = Label(f3, text="Description:", font=(textFont, 16, "bold"), bg=bgColor,
                         fg=textColor).place(x=70, y=490)

            # if(len(commentDisases))
            # temp = "Remark Please hold the temperature Please Please hold hold the temperature Please Please hold the temperature sensor gently hold the temperature Please Please hold the temperature sensor gently hold the temperature Please Please hold the temperature sensor gently hold the temperature Please Please hold the temperature sensor gently hold the temperature Please Please hold the temperature sensor gently the temperature sensor gently hold the temperature sensor gently sensor gently"
            if commentDisases:
                commentDisases = commentDisases
            else:
                commentDisases = "No Comment Found :)"

            lab4 = Label(f3, text=commentDisases, font=(textFont, 16), bg=bgColor, wraplength=400, justify=LEFT,
                         fg=textColor).place(x=70, y=520)
            lab11 = Label(f3, text="Understood Clearly :", font=(textFont, 16, "bold"), bg=bgColor, wraplength=400,
                          justify=LEFT,
                          fg=textColor).place(x=950, y=200)
            bt = Button(root, text="Write Prescription", font=(textFont, 14, "bold"), fg="black", cursor='hand2',
                        bg=btcl2,
                        activebackgroun=bgColor, command=writePrescription, width=26).place(x=950, y=260)
            lab12 = Label(f3, text=" Not Understood Clearly :", font=(textFont, 16, "bold"), bg=bgColor, wraplength=400,
                          justify=LEFT,
                          fg=textColor).place(x=950, y=350)
            bt = Button(root, text="Send Again", font=(textFont, 14, "bold"), fg="black", cursor='hand2',
                        bg=btcl1, activebackgroun=bgColor, command=sendagain, width=26).place(x=950, y=410)
            bt3 = Button(f3, text="Back", font=(textFont, 16, "bold"), fg="white", cursor='hand2', bg=textColor,
                         command=back, width=5).place(x=20, y=10)

        def sel():
            global count
            selection = "You selected the option " + str(var.get())
            print(selection)

            print(count)
            print(str(count))

            config = {
                "apiKey": "AIzaSyDJxmveUpxm34nFLm55KS1GyTVi65-sGwc",
                "authDomain": "pythonmelody.firebaseapp.com",
                "databaseURL": "https://pythonmelody-default-rtdb.firebaseio.com",
                "projectId": "pythonmelody",
                "storageBucket": "pythonmelody.appspot.com"
            }
            firebase = pyrebase.initialize_app(config)
            db = firebase.database()

            a2 = {"Message": "good"}
            db.child(str(count)).child("Dr Data").child("Message").update(a2)

            if prescriptionText.get():
                a1 = {"Prescription": str(prescriptionText.get())}
                db.child(str(count)).child("Dr Data").child("Prescription").update(a1)
            else:
                a1 = {"Prescription": "No Prescription Found"}
                db.child(str(count)).child("Dr Data").child("Prescription").update(a1)
            if medicinename.get():
                a1 = {"Medicine Name": str(medicinename.get())}
                db.child(str(count)).child("Dr Data").child("Medicine").update(a1)
            else:
                a1 = {"Medicine Name": "No medicine found"}
                db.child(str(count)).child("Dr Data").child("Medicine").update(a1)
            if timing.get():
                a1 = {"Meeting Timing": str(timing.get())}
                db.child(str(count)).child("Dr Data").child("Meeting Time").update(a1)
            else:
                a1 = {"Meeting Timing": "No meeting Found"}
                db.child(str(count)).child("Dr Data").child("Meeting Time").update(a1)
            if Diet.get():
                a1 = {"Diet": str(Diet.get())}
                db.child(str(count)).child("Dr Data").child("Diet").update(a1)
            else:
                a1 = {"Diet": "No Diet Found"}
                db.child(str(count)).child("Dr Data").child("Diet").update(a1)
            if Avoid.get():
                a1 = {"Avoid": str(Avoid.get())}
                db.child(str(count)).child("Dr Data").child("Avoid").update(a1)
            else:
                a1 = {"Avoid": "No Avoid Found"}
                db.child(str(count)).child("Dr Data").child("Avoid").update(a1)
            digits = [i for i in range(0, 10)]
            random_str = ""
            for i in range(6):
                ## generating a random index
                ## if we multiply with 10 it will generate a number between 0 and 10 not including 10
                ## multiply the random.random() with length of your base list or str
                index = math.floor(random.random() * 10)

                random_str += str(digits[index])

                ## displaying the random string
            print(random_str)
            a1 = {"Code": random_str}
            db.child(str(count)).child("Dr Data").child("Code").update(a1)

            if drLink.get():
                a1 = {"link": drLink.get()}
                db.child(str(count)).child("Dr Data/Video Link").update(a1)
            else:
                a1 = {"link": "https://meet.google.com/bvb-dihc-wwm"}
                db.child(str(count)).child("Dr Data/Video Link").update(a1)

            # mc

            f3 = Frame(bg=bgColor)
            f3.place(x=0, y=0, width=_width, height=_height)
            lab4 = Label(f3, text="Prescription & vending \nmachine option send to patient :)",
                         font=(textFont, 34, "bold"),
                         bg=bgColor, fg=textColor).place(x=160,
                                                         y=150)
            bt3 = Button(f3, text="Back", font=(textFont, 14, "bold"), fg="white", bg=textColor, cursor='hand2',
                         command=back_2, width=10).place(x=20, y=20)

            # label.config(text=selection)

        def writePrescription():

            f3 = Frame(bg=bgColor)
            e8 = Label(f3,
                       text="______________________________________________________________________________________________________________________________________",
                       font=(textFont, 18, "bold"),
                       fg=textColor,
                       bg=bgColor).place(x=0, y=30)


            f3.place(x=0, y=0, width=_width, height=_height)
            lab4 = Label(f3, text="Prescription", font=(textFont, 30, "bold"), bg=bgColor,
                         fg=textColor).place(x=200, y=0)

            lab4 = Label(f3, text="Write Prescription:", font=(textFont, 18, "bold"), bg=bgColor,
                         fg=textColor).place(x=100, y=100)
            e1 = Entry(f3, font=(textFont, 12), borderwidth=1, relief="solid", textvariable=prescriptionText).place(
                x=100, y=150, width=315,height=70)
            lab4 = Label(f3, text="Medicines Name:", font=(textFont, 18, "bold"), bg=bgColor,
                         fg=textColor).place(x=100, y=250)
            e1 = Entry(f3, font=(textFont, 12), borderwidth=1, relief="solid", textvariable=medicinename).place(x=100,
                                                                                                                y=300,height=70,
                                                                                                                width=315)
            lab4 = Label(f3, text="Video Call Link:", font=(textFont, 18, "bold"), bg=bgColor,
                         fg=textColor).place(x=100, y=400)
            e1 = Entry(f3, font=(textFont, 12), borderwidth=1, relief="solid", textvariable=drLink).place(x=100, y=450,
                                                                                                           height=40,width=315)
            lab4 = Label(f3, text="Timing of video call link:", font=(textFont, 19, "bold"), bg=bgColor,
                         fg=textColor).place(x=700, y=100)
            e1 = Entry(f3, font=(textFont, 12), borderwidth=1, relief="solid", textvariable=timing).place(x=700, y=150,
                                                                                                          height=40,width=315)
            lab4 = Label(f3, text="Diet For Patient:", font=(textFont, 18, "bold"), bg=bgColor,
                         fg=textColor).place(x=700, y=250)
            e1 = Entry(f3, font=(textFont, 12), borderwidth=1, relief="solid", textvariable=Avoid).place(x=700, y=300,
                                                                                                         width=315,height=70)
            lab4 = Label(f3, text="To Avoid:", font=(textFont, 18, "bold"), bg=bgColor,
                         fg=textColor).place(x=700, y=400)
            e1 = Entry(f3, font=(textFont, 12), borderwidth=1, relief="solid", textvariable=Diet).place(x=700, y=450,
                                                                                                        height=40,width=315)

            bt = Button(root, text="Submit Prescription", font=(textFont, 14, "bold"), fg="black", cursor='hand2',
                        bg=btcl1, activebackgroun=bgColor, command=sel, width=30).place(x=110, y=550)
            bt3 = Button(f3, text="Back", font=(textFont, 14, "bold"), fg="white", bg=textColor, cursor='hand2',
                         command=back_1, width=10).place(x=15, y=10)

        # finish()
        # t = Button(root, text="Login", font=(textFont, 18, "bold"), fg="white", cursor='hand2', bg=textColor,
        #            activebackgroun=bgColor, command=login, width=12).place(x=25, y=400)
        # bt = Button(root, text="SignUp", font=(textFont, 18, "bold"), fg="white", cursor='hand2', bg=textColor,
        #             activebackgroun=bgColor, command=signup, width=14).place(x=200, y=400)
        # writePrescription()

        # webbrowser.open('https://meet.google.com/qdd-waft-npi')
        a = 0
        b = 0

        # auth = firebase.auth()
        # user = auth.create_user_with_email_and_password("ap0288938@gmail.com", "password")
        # auth.create_user_with_email_and_password(id, passw)
        # info = auth.get_account_info(user['idToken'])

        # print(user)


root = Tk()
obj = login(root)
root.mainloop()
