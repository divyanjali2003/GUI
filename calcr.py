

from tkinter import *
root=Tk()
root.title("calculator")
entry=Entry(root,justify=CENTER,bg="light blue",fg="white",width=15,font=(("arial","30")))
entry.place(x=14,y=150)
def clicked(num):
    present=entry.get()
    if num == "=":
        try:
            out=str(eval(present))
            entry.delete(0,END)
            entry.insert(END,out)
        except:
            entry.delete(0,END)
            entry.insert(END,"error occured")
    elif num == "C":
        entry.delete(0,END)
    else:
        entry.insert(END,num)
b1=Button(root,text='1',fg='light blue',bg='black',command=lambda:clicked(1),height=5,width=10) 
b1.place(x=20,y=200)
b2=Button(root,text='2',fg='light blue',bg='black',command=lambda:clicked(2),height=5,width=10) 
b2.place(x=100,y=200) 
b3=Button(root,text='3',fg='light blue',bg='black',command=lambda:clicked(3),height=5,width=10) 
b3.place(x=180,y=200) 
b4=Button(root,text='4',fg='light blue',bg='black',command=lambda:clicked(4),height=5,width=10) 
b4.place(x=20,y=300) 
b5=Button(root,text='5',fg='light blue',bg='black',command=lambda:clicked(5),height=5,width=10) 
b5.place(x=100,y=300)
b6=Button(root,text='6',fg='light blue',bg='black',command=lambda:clicked(6),height=5,width=10) 
b6.place(x=180,y=300)
b7=Button(root,text='7',fg='light blue',bg='black',command=lambda:clicked(7),height=5,width=10) 
b7.place(x=20,y=400) 
b8=Button(root,text='8',fg='light blue',bg='black',command=lambda:clicked(8),height=5,width=10) 
b8.place(x=100,y=400)
b9=Button(root,text='9',fg='light blue',bg='black',command=lambda:clicked(9),height=5,width=10) 
b9.place(x=180,y=400) 
b10=Button(root,text='0',fg='light blue',bg='black',command=lambda:clicked(0),height=5,width=10) 
b10.place(x=100,y=500) 
b11=Button(root,text='+',fg='black',bg='light green',command=lambda:clicked("+"),height=5,width=10) 
b11.place(x=260,y=200) 
b12=Button(root,text='-',fg='black',bg='light green',command=lambda:clicked("-"),height=5,width=10) 
b12.place(x=260,y=300) 
b13=Button(root,text='*',fg='black',bg='light green',command=lambda:clicked("*"),height=5,width=10) 
b13.place(x=260,y=400) 
b14=Button(root,text='/',fg='black',bg='light green',command=lambda:clicked("/"),height=5,width=10) 
b14.place(x=260,y=400) 
b15=Button(root,text='=',fg='black',bg='light green',command=lambda:clicked("="),height=5,width=10) 
b15.place(x=260,y=500)  
b16=Button(root,text='C',fg='black',bg='orange',command=lambda:clicked("C"),height=5,width=10) 
b16.place(x=20,y=500)
b17=Button(root,text='.',fg='white',bg='black',command=lambda:clicked('.'),height=5,width=10) 
b17.place(x=180,y=500) 
root.geometry("800x800")
root.mainloop() 