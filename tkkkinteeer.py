from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title('Resident Evil')
window.geometry('400x420')

title = Label(window, text='Resident Evil', fg='white' , bg='red', width=40)
title.pack(pady = 10)
imgg = Image.open('leon.png')
imgg = imgg.resize((300,180))
photo = ImageTk.PhotoImage(imgg)
pic = Label(window, image=photo)
pic.pack(pady=5)

def show_msg():
    messagebox.showinfo('You clicked in this photo')
msg_btn = Button(window, text='Click to see', bg = 'blue', fg= 'white', command=show_msg)
msg_btn.pack(pady=5)

def show_data():
    top = Toplevel()
    top.title('View Info')
    top.geometry('200x120')
    info = Label(top,text='Name: Leon S. Kennedy (FBI)')
    info.pack(pady=5)
    place = Label(top, text='Monster Slayer')
    place.pack(pady=5)
    top.mainloop()

data_btn = Button(window, text='See bio', fg= 'white', bg='gray', command=show_data)
data_btn.pack(pady=5)

window.mainloop()
