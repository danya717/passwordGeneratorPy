import tkinter as tk
import random
import tkinter.messagebox as messagebox
from tkinter import ttk, OptionMenu
from tkinter import StringVar

window = tk.Tk()
window.title = "passwordGenerator"
window.geometry('300x300')

letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o",
           "p", "a", "s", "d", "f", "g", "h", "j", "k", "l",
           "z", "x", "c", "v", "b", "n", "m"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

pool = []
required = []

upper_pool = list(map(str.upper, letters))
lower_pool = letters
num_pool = numbers
sym_pool = symbols

def refresh_pools():
    pool.clear()
    required.clear()
    if agreement_var1.get():
        pool.append(upper_pool)
        required.append(upper_pool)
    if agreement_var2.get():
        pool.append(lower_pool)
        required.append(lower_pool)
    if agreement_var3.get():
        pool.append(num_pool)
        required.append(num_pool)
    if agreement_var4.get():
        pool.append(sym_pool)
        required.append(sym_pool)

def upper_case():
    refresh_pools()

def lower_case():
    refresh_pools()

def numbers():
    refresh_pools()

def symbols():
    refresh_pools()

agreement_var1 = tk.BooleanVar()
agreement_var2 = tk.BooleanVar()
agreement_var3 = tk.BooleanVar()
agreement_var4 = tk.BooleanVar()

def select(choice):
    choice = variable.get()
    if choice == "4":
        print("choice is 4")
    if choice == "6":
        print("choice is 6")
    if choice == "8":
        print("choice is 8")

options = ["4", "6", "8", "10"]
variable = StringVar()
variable.set(options[2])
password = []

def password_gen():
    global password
    refresh_pools()
    password = []
    random.shuffle(num_pool)
    random.shuffle(upper_pool)
    random.shuffle(lower_pool)
    random.shuffle(sym_pool)
    length = int(variable.get())
    for group in required:
        password.append(random.choice(group))

    all_pool = []
    for group in pool:
        for char in group:
            all_pool.append(char)

    if not all_pool:
        all_pool = lower_pool
    while len(password) < length:
        password.append(random.choice(all_pool))
    print(password)
    return "".join(password)


def password_text():
    canvas.delete('pwd')
    color = 'white'
    canvas.create_text((150, 210), text=f'{password_gen()}', fill=color, font=(20), tags=('pwd',))

def copy_btn():
    text = ''.join(password)
    window.clipboard_clear()
    window.clipboard_append(text)
    messagebox.showinfo("Succes!", "password has been copied to clipboard")
    # print('text has been copied')

def draw_square():
    color = 'purple'
    color_border = 'red'
    d = 300
    x = 0
    y = 0
    canvas.create_rectangle(x, y, x+d, y+d, fill=color, outline=color_border)

def draw_rectangle():
    color = 'gray'
    border_color = 'black'
    canvas.create_rectangle(280, 190, 20, 230, fill=color, outline=border_color)

def draw_text():
    color = 'black'
    canvas.create_text((150, 30), text='PASSWORD GENERATOR', font=("Helvetica", 17, "bold"), fill=color)

canvas = tk.Canvas(window, bg='white', width=400, height=400)
canvas.place(x=0, y=0)

button = tk.Button(window, width=15, text='generate', command=password_text)
button.place(x=35, y=240)

checkbox = ttk.Checkbutton(window, text="upperCase", command=upper_case, variable=agreement_var1)
checkbox.place(x=30, y=100)
checkbox2 = ttk.Checkbutton(window, text="lowerCase", command=lower_case, variable=agreement_var2)
checkbox2.place(x=190, y=100)
checkbox3 = ttk.Checkbutton(window, text="numbers", command=numbers, variable=agreement_var3)
checkbox3.place(x=30, y=150)
checkbox4 = ttk.Checkbutton(window, text="symbols", command=symbols, variable=agreement_var4)
checkbox4.place(x=190, y=150)

option_menu = OptionMenu(window, variable, *options, command=select)
option_menu.place(x=30, y=55)

button2 = ttk.Button(window, text="Copy", command=copy_btn)
button2.place(x=190, y=240)


draw_square()
draw_rectangle()
draw_text()

window.resizable(width=False, height=False)
window.mainloop()