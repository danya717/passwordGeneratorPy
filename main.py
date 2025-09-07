import tkinter as tk

from tkinter import ttk


window = tk.Tk()
window.title = 'passwordGenerator'
window.geometry('600x600')



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

canvas = tk.Canvas(window, bg='white', width=500, height=500)
canvas.place(x=50, y=50)

button = tk.Button(window, width=15, text='generate')
button.place(x=240, y=455)
checkbox = ttk.Checkbutton(window, text="upperCase")
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