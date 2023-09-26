from tkinter import *
from tkinter import messagebox
count=1;
def add_button():
    global count
    task=v1.get()
    if task:
        l2.insert(END,task)
        count+=1
        e1.delete(0,END)
    else:
        messagebox.showwarning("WARNING","PLEASE ENTER A TASK!")
def remove_button():
    selected_task_index=l2.curselection()
    if selected_task_index:
        l2.delete(selected_task_index)
    else:
        messagebox.showwarning("WARNING","PLEASE SELECT A TASK TO REMOVE!")
def edit_button():
    selected_task_index=l2.curselection()
    if selected_task_index:
        selected_task=l2.get(selected_task_index)
        e1.insert(0,selected_task)
        e1.focus()
        new_text=e1.get()
        l2.delete(selected_task_index)
    else:
        messagebox.showwarning("WARNING","PLEASE SELECT THE TASK TO EDIT")
def clear_button():
    l2.delete(0,END)
root=Tk()
root.geometry('400x500')
root.title('TO DO LIST')
root.config(bg='black')
root.resizable(0,0)
l1=Label(root,text="WELCOME! TO-DO LIST",font=('Times New Roman',24,'bold'),fg='crimson',bg='light blue',borderwidth=10)
l1.place(x=0,y=0)
v1=StringVar()
e1=Entry(root,width=30,font=('Times New Roman',15,'bold'),textvariable=v1,bg='beige',fg='dark blue',bd=5)
e1.place(x=45,y=80)
e1.focus()
b1=Button(root,text="ADD TASK",font=('Times New Roman',10,'bold'),width=10,bg='BROWN',fg='white',command=add_button)
b1.place(x=160,y=135)
b2=Button(root,text="REMOVE TASK",font=('Times New Roman',10,'bold'),width=13,bg='RED',fg='white',command=remove_button)
b2.place(x=30,y=445)
b2=Button(root,text="EDIT TASK",font=('Times New Roman',10,'bold'),width=13,bg='gold',fg='white',command=edit_button)
b2.place(x=155,y=445)
b3=Button(root,text="CLEAR LIST",font=('Times New Roman',10,'bold'),width=13,bg='GREEN',fg='white',command=clear_button)
b3.place(x=280,y=445)
l2=Listbox(root,width=30,bg='beige',bd=5,font=("Times New Roman",15,'bold'),fg='dark blue')
l2.place(x=45,y=175)
l3=Label(root,text="@MADE BY VIVEK TRIPATHI",fg='white',font=('Times New Roman',7,'bold'),bg='light blue')
l3.place(x=264,y=55)
root.mainloop()