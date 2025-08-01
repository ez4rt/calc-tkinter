import math
from tkinter import *

def btn_click(item):
    global expression
    try:
        input_field['state'] = "normal"
        expression += item
        input_field.insert(END, item)

        if item == '=':
            result = str(eval(expression[:-1].replace('^', '**')))
            expression = result
            input_field.delete(0, END)
            input_field.insert(END, result)

        input_field['state'] = "readonly"
    except ZeroDivisionError:
        input_field.delete(0, END)
        input_field.insert(0, 'На ноль делить нельзя')
    except SyntaxError:
        input_field.delete(0, END)
        input_field.insert(0, 'Ошибка')

def bt_clear():
    global expression
    expression = ""
    input_field['state'] = "normal"
    input_field.delete(0, END)
    input_field['state'] = "readonly"

def bt_del():
    global expression
    input_field['state'] = "normal"
    input_field.delete(len(input_field.get()) - 1, END)
    expression = expression[:-1]
    input_field['state'] = "readonly"


def btn_sqrt():
    global expression
    input_field['state'] = "normal"
    result = str(math.sqrt(eval(expression)))
    expression = result
    input_field.delete(0, END)
    input_field.insert(END, result)
    input_field['state'] = "readonly"


root = Tk()
root.geometry("915x665")
root.title("Калькулятор")
root.resizable(0, 0)
root.configure(bg='black')

frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")

input_field = Entry(frame_input, font='TimesNewRoman 38 bold', width=24, state="readonly")
input_field.pack(fill=BOTH)

buttons = ((' ', ' ', ' ', '^', '4'),
           ('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

expression = ""

button_clear = Button(root, text='C', command=lambda: bt_clear(), font='TimesNewRoman 20 italic', bg='gray', fg='white')
button_clear.grid(row=2, column=0, sticky="nsew", padx=50, pady=20)

button_del = Button(root, text='<-', command=lambda: bt_del(), font='TimesNewRoman 20 italic', bg='gray', fg='white')
button_del.grid(row=2, column=1, sticky="nsew", padx=50, pady=20)

button_sqrt = Button(root, text='√', command=btn_sqrt, font='TimesNewRoman 20 italic', borderwidth=15, relief="ridge")
button_sqrt.grid(row=2, column=2, sticky="nsew", padx=3, pady=3)

for row in range(5):
    for col in range(4):
        if buttons[row][col] != ' ':
            Button(root, width=11, height=2, text=buttons[row][col], font='TimesNewRoman 20 bold', borderwidth=15, relief="ridge",
                   command=lambda row=row, col=col: btn_click(buttons[row][col])).grid(row=row+2, column=col, sticky="nsew", padx=3, pady=3)

root.mainloop()
