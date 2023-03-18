import tkinter as tk

window=tk.Tk()
window.title('Killometer to miles')
window.minsize(150,150)

#lable 1 that doesnt exist
'''lable_1=tk.Label(text='                                     ')
lable_1.grid(column=0,row=0)'''

#an input that position(1,0) an entry holds values
user_input=tk.Entry(width=10)
user_input.grid(column=1,row=0)



# the lable2 at position (2,0) holds text
Miles =tk.Label(text='    Miles')
Miles.grid(column=2,row=0)


# the 3th lable that holds text at position (1,0)

Equals_text=tk.Label(text='is Equal to ')
Equals_text.grid(column=0,row=1)



# the 4th label
km_values=tk.Label(text='0')
km_values.grid(column=1,row=1)


# the 5th lable

Km_lable=tk.Label(text='Km')
Km_lable.grid(column=2,row=1)

def button_used():
    Value=float(user_input.get())
    km_values.config(text=str(Value*1.609))
buttom=tk.Button(fg='white',background='black',text='Calculate',command=button_used)
buttom.grid(column=1,row=2)
window.mainloop()


