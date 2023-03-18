import tkinter as tk
from turtle import Turtle, Screen
window=tk.Tk()
window.title("Alert")
window.minsize(300,300)


my_lable=tk.Label(text="New Text")
my_lable.grid(column=0,row=0)


def button_clicked():
    my_lable.config( text= input.get())

button_1 =tk.Button(fg='black',bg='white',text="Click Me",command=button_clicked)
button_1.grid(column=1,row=1)

button_2=tk.Button(fg='red',background='blue',text='second button',command=button_clicked)
button_2.grid(column=2,row=0)
input=tk.Entry(width=10) 
input.grid(column=3,row=3)
def spinboxused():
    print(spinbox.get())
spinbox=tk.Spinbox(from_=1, to=10,width=5,command=spinboxused )


scale=tk.Scale(from_=0,to=100)

def checkbutton_used():
    print (check_state.get())
check_state=tk.IntVar()
check_button=tk.Checkbutton(text="Is On?", command=checkbutton_used,variable=check_state)

window.mainloop() 