# from tkinter import*
# root=Tk()
# root.geometry("450x900")
# root.title("myapp")
# root.mainloop()

# # from tkinter import*
# root=Tk()
# root.geometry("450x900")
# root.title("my app")
# lb1=Label(root,text="my name is divya")
# lb1.pack()
# lb2=Label(root,text="my age is 21",font=("times,12"), fg='white',bg='black')
# lb2.pack()
# root.mainloop()

# from tkinter import*
# root=Tk()
# root.geometry("450x900")
# root.title("my app")
# def clicked():
#     print("my name is Divya")
# bt1=Button(root,text="login",command=clicked)
# bt1.pack()
# entry=Entry(root)
# entry.pack()
# root.mainloop()

#textbox
# from tkinter import*
# root=Tk()
# def callback():
#     text=textEditor.get(0.1,END)
#     print(text)
# textEditor=Text(root,width=43,height=10)
# textEditor.pack()
# button1=Button(root,text="Display Test",command=callback)
# button1.pack(pady=12)
# root.geometry('350x218')
# root.title("PythonLobby")
# root.mainloop()

#scrollbar
# from tkinter import*
# root=Tk()
# textbox=Text(root,width=40,height=13,wrap=WORD)
# textbox.grid(row=0)
# scroll=Scrollbar(root,orient=VERTICAL,command=textbox.yview)
# scroll.grid(row=0,column=1,sticky=N+S)
# textbox.config(yscrollcommand=scroll.set)
# root.geometry("350x220")
# root.title("PythonLobby.com")
# root.mainloop()

#listbox
# from tkinter import*
# from tkinter import ttk
# root=Tk()
# listbox=Listbox(root,width=45,height=15)
# listbox.pack(pady=20)
# listbox.insert(0,"c")
# listbox.insert(1,"c++")
# listbox.insert(2,"java")
# listbox.insert(3,"python")
# root.geometry("400x240")
# root.title("PythonLobby.com")
# root.mainloop()

#menu button
from tkinter import*
from tkinter import ttk
from time import strftime
root=Tk()
root.title('Menu Demonstration')
menubar=Menu(root)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=file)
file.add_command(label='Open',command=None)
file.add_cascade(label='Save',command=None)
file.add_separator()
file.add_command(label='exist',command=root.destroy)
edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label='edit',menu=edit)
edit.add_command(label='Cut',command=None)
edit.add_command(label='Copy',command=None)
edit.add_command(label='Paste',command=None)
edit.add_command(label='Select All',command=None)
edit.add_separator()
edit.add_command(label='Find',command=None)
edit.add_command(label='Find Again',command=None)
help=Menu(menubar,tearoff=0)
menubar.add_cascade(label='help',menu=help)
help.add_command(label='Tk Help',command=None)
help.add_command(label='Demo',command=None)
help.add_separator()
help.add_command(label='About Tk',command=None)
root.config(menu=menubar)
root.mainloop()