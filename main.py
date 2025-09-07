import tkinter as tk
import random
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title = 'passwordGenerator'
window.geometry('600x600')

letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o",
           "p", "a", "s", "d", "f", "g", "h", "j", "k", "l",
           "z", "x", "c", "v", "b", "n", "m"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]


def show_message():
    showinfo(title='result', message='You agreed' if agreement_var.get() else 'you didnt agree')

agreement_var = tk.BooleanVar()

def password_gen():
    random.shuffle(letters)
    print(letters)

def draw_square():
    color = 'gold'
    color_border = 'red'
    d = 400
    x = 50
    y = 50
    canvas.create_rectangle(x, y, x+d, y+d, fill=color, outline=color_border)

def draw_rectangle():
    color = 'gray'
    border_color = 'black'
    canvas.create_rectangle(400, 350, 100, 400, fill=color, outline=border_color)

def draw_text():
    color = 'red'
    canvas.create_text((250, 80), text='PASSWORD GENERATOR', font=("Helvetica", 20, "bold"), fill=color)

def password():
    color = 'white'
    canvas.create_text((250, 379), text=f'{password_gen()}', font=("Helvetica", 20), fill=color)

canvas = tk.Canvas(window, bg='white', width=500, height=500)
canvas.place(x=50, y=50)

button = tk.Button(window, width=15, text='generate', command=password)
button.place(x=240, y=455)
checkbox = ttk.Checkbutton(window, text="upperCase", command=show_message, variable=agreement_var)
checkbox.place(x=170, y=200)
checkbox2 = ttk.Checkbutton(window, text="lowerCase")
checkbox2.place(x=350, y=200)
checkbox3 = ttk.Checkbutton(window, text="numbers")
checkbox3.place(x=170, y=300)
checkbox4 = ttk.Checkbutton(window, text="symbols")
checkbox4.place(x=350, y=300)

draw_square()
draw_rectangle()
draw_text()

window.mainloop()