from tkinter import*
from tkinter import Tk
root=Tk()
root.title("https://web.instagram.com/login/device/")
l1=Label(root,text="instagram",fg="black",font=("Billabong","25"))
l1.place(x=350,y=100)
l2=Label(root,text="Phone number OR email address",font=("normal","15"))
l2.place(x=350,y=200)
entry1=Entry(root,justify=CENTER,font=(("arial","15")))
entry1.place(x=350,y=250)
label3=Label(root,text="Password :",font=(("normal","18")))
label3.place(x=350,y=300)
entry2=Entry(root,justify=CENTER,font=(("arial","15")))
entry2.place(x=350,y=350)
def Login():
    print("login successfully")
button=Button(root,text="Log In",command="Log in",activebackground="silver",fg="white",bg="blue",width=30)
button.place(x=350,y=420)
l3=Label(root,text="           forgotten password?",fg="blue",font=("normal","10"))
l3.place(x=350,y=600)
l4=Label(root,text="------------------------- or -------------------------",fg="black",font=("normal","10"))
l4.place(x=350,y=500)
l5=Label(root,text="      Log In with FaceBook  ",fg="blue",font=(("normal","13")))
l5.place(x=350,y=560)
root.geometry("1000x800")
root.mainloop()

# from tkinter import *
# from tkinter import ttk

# user=Tk()
# user.title("www.instagram/login/page/meta.com")

# label1=Label(user,text="Instagram",fg="black",font=(("Billabong","80")))
# label1.place(x=500,y=0)

# label2=Label(user,text="E-Mail or Phone Number :",font=(("normal","15")))
# label2.place(x=600,y=200)

# entry=Entry(user,justify=CENTER,font=(("arial","15")))
# entry.place(x=599,y=250)

# label3=Label(user,text="Password :",font=(("normal","18")))
# label3.place(x=660,y=350)

# entry1=Entry(user,justify=CENTER,font=(("arial","15")))
# entry1.place(x=602,y=410)

# def Login():
#     print("login successfully")

# btn=Button(user,text="Log In",command=Login,activebackground="silver",fg="white",bg="blue",width=30)
# btn.place(x=620,y=500)

# label4=Label(user,text="----------------------------------OR--------------------------------",fg="black",font=(("normal","10")))
# label4.place(x=588,y=550)

# label5=Label(user,text="Log In with FaceBook",fg="blue",font=(("normal","13")))
# label5.place(x=670,y=600)

# path1=PhotoImage(file="C:/Users/karth/Downloads/OIP (1).png")
# label_image=Label(user,image=path1,width=30,height=30)
# label_image.place(x=630,y=595)

# label6=Label(user,text="Forgot PassWord ?",fg="blue",font=(("normal","10")))
# label6.place(x=680,y=660)

# path2=PhotoImage(file="C:/Users/karth/OneDrive/Pictures/245465857-80df6e7f-b157-4389-911c-176db3871f19.png")
# my_image=Label(user,image=path2,width=400,height=800)
# my_image.place(x=0,y=0)

# user.geometry("1400x1200")
# user.mainloop()


