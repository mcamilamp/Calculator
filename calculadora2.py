from tkinter import *


def button_press(num):
    global equatiom_text

    equatiom_text = equatiom_text + str(num)

    equation_label.set(equatiom_text)

def equals():
    global equatiom_text

    try:

        total = str(eval(equatiom_text))

        equation_label.set(total)

        equatiom_text = total

    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equatiom_text = ""

    except SyntaxError:
        equation_label.set("Syntax error")
        equatiom_text = ""

def clear():
    global equatiom_text

    equation_label.set("")
    equatiom_text = "" 

window = Tk()
window.title("Calculator")
window.geometry("400x600")

equatiom_text = ""

equation_label = StringVar()

Label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="pink", width=24, height=2)

Label.pack()

Frame = Frame(window)
Frame.pack()

Button1 = Button(Frame, text=1, height=3, width=8, font=35, command=lambda:button_press(1))
Button1.grid(row=0, column=0)

Button2 = Button(Frame, text=2, height=3, width=8, font=35, command=lambda:button_press(2))
Button2.grid(row=0, column=1)

Button3 = Button(Frame, text=3, height=3, width=8, font=35, command=lambda:button_press(3))
Button3.grid(row=0, column=2)

Button4 = Button(Frame, text=4, height=3, width=8, font=35, command=lambda:button_press(4))
Button4.grid(row=1, column=0)

Button5 = Button(Frame, text=5, height=3, width=8, font=35, command=lambda:button_press(5))
Button5.grid(row=1, column=1)

Button6 = Button(Frame, text=6, height=3, width=8, font=35, command=lambda:button_press(6))
Button6.grid(row=1, column=2)

Button7 = Button(Frame, text=7, height=3, width=8, font=35, command=lambda:button_press(7))
Button7.grid(row=2, column=0)

Button8 = Button(Frame, text=8, height=3, width=8, font=35, command=lambda:button_press(8))
Button8.grid(row=2, column=1)

Button9 = Button(Frame, text=9, height=3, width=8, font=35, command=lambda:button_press(9))
Button9.grid(row=2, column=2)

Button0 = Button(Frame, text=0, height=3, width=8, font=35, command=lambda:button_press(0))
Button0.grid(row=3, column=0)

plus = Button(Frame, text='+', height=3, width=8, font=35, command=lambda:button_press('+'))
plus.grid(row=3, column=1)

minus = Button(Frame, text='-', height=3, width=8, font=35, command=lambda:button_press('-'))
minus.grid(row=3, column=2)

multiply = Button(Frame, text='*', height=3, width=8, font=35, command=lambda:button_press('*'))
multiply.grid(row=4, column=0)

divide = Button(Frame, text='/', height=3, width=8, font=35, command=lambda:button_press('/'))
divide.grid(row=4, column=1)

equal= Button(Frame, text='=', height=3, width=8, font=35, command=equals)
equal.grid(row=4, column=2)

decimal = Button(Frame, text='.', height=3, width=8, font=35, command=lambda:button_press('.'))
decimal.grid(row=5, column=0)

clear = Button(window, text='C', height=3, width=26, font=35, command=clear)
clear.pack()

window.mainloop()