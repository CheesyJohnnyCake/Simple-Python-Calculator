#Package Installation

from tkinter import *
from math import *
import functools
import re
window = Tk()

#---------------------

#Calculator Functions

def button_function_addition():
  add_button.bind('<Button-1>', addition_character)

def button_function_subtraction():
  subtract_button.bind('<Button-1>', subtraction_character)

def addition_character(button_function_addition):
  question_input.insert(END, str('+'))

def subtraction_character(button_function_subtraction):
  question_input.insert(END, str('-'))

def button_function_multiplication():
  multiply_button.bind('<Button-1>', multiplication_character)

def multiplication_character(button_function_multiplication):
  question_input.insert(END, str('x'))

def button_function_division():
  divide_button.bind('<Button-1>', division_character)

def division_character(button_function_division):
  question_input.insert(END, str('÷'))

def button_function_one():
  button_one.bind('<Button-1>', one_character)

def one_character(button_function_one):
  question_input.insert(END, str('1'))

def button_function_two():
  button_two.bind('<Button-1>', two_character)

def two_character(button_function_two):
  question_input.insert(END, str('2'))

def button_function_three():
  button_three.bind('<Button-1>', three_character)

def three_character(button_function_three):
  question_input.insert(END, str('3'))

def button_function_four():
  button_four.bind('<Button-1>', four_character)

def four_character(button_function_four):
  question_input.insert(END, str('4'))

def button_function_five():
  button_five.bind('<Button-1>', five_character)

def five_character(button_function_five):
  question_input.insert(END, str('5'))

def button_function_six():
  button_six.bind('<Button-1>', six_character)

def six_character(button_function_six):
  question_input.insert(END, str('6'))

def button_function_seven():
  button_seven.bind('<Button-1>', seven_character)

def seven_character(button_function_seven):
  question_input.insert(END, str('7'))

def button_function_eight():
  button_eight.bind('<Button-1>', eight_character)

def eight_character(button_function_eight):
  question_input.insert(END, str('8'))

def button_function_nine():
  button_nine.bind('<Button-1>', nine_character)

def nine_character(button_function_nine):
  question_input.insert(END, str('9'))

def button_function_zero():
  button_zero.bind('<Button-1>', zero_character)

def zero_character(button_function_zero):
  question_input.insert(END, str('0'))

def solve():
    e = question_input.get()
    for i in e:
        if i == "x":
            e = e.replace("x", "*")
        elif i == "÷":
            e = e.replace("÷", "/")
        elif i == "π":
            e = e.replace("π", "*3.1415926535")
        elif i == "%":
            e = e.replace("%", "/100")
        elif i == "²":
            e = e.replace("²", "**2")
        elif i == "√":
            e = e.replace(e[:], re.sub(r'√(\d+)', r'sqrt(\1)', e))
    e = eval(e)
    question_input.delete(0, END)
    question_input.insert(END, str(e))

def button_function_decimal():
    button_decimal.bind('<Button-1>', decimal_character)

def decimal_character(button_function_decimal):
    question_input.insert(END, str('.'))

def button_function_pi():
    button_pi.bind('<Button-1>', pi_character)

def pi_character(button_function_pi):
    question_input.insert(END, str('π'))

def button_function_percent():
    percent_button.bind('<Button-1>', percent_character)

def percent_character(button_function_percent):
    question_input.insert(END, str('%'))

def button_function_square_root():
    square_root_button.bind('<Button-1>', square_root_character)

def square_root_character(button_function_square):
    question_input.insert(END, str('√'))

def button_function_square():
    square_button.bind('<Button-1>', square_character)

def square_character(button_function_square):
    question_input.insert(END, str('²'))

def button_function_clear():
    clear_button.bind('<Button-1>', clear_character)

def clear_character(button_function_clear):
    question_input.delete(0, END)

#---------------------

#GUI
button_zero = Button(window, text='0', fg='black', bd=1, bg = "gainsboro", width=5, padx = 4, pady = 5)
button_one = Button(window, text='1', fg='black', bd=1, bg='gainsboro', width=5, padx = 4, pady = 5)
button_two = Button(window, text='2', fg='black', bd=1, bg='gainsboro', width=5, padx = 4, pady = 5)
button_three = Button(window, text='3', fg='black', bd=1, bg='gainsboro', width=5, padx = 4, pady = 5)
button_four = Button(window, text='4', fg='black', bd=1, bg='gainsboro', width=5, padx = 4, pady = 5)
button_five = Button(window, text='5', fg='black', bd=1, bg='gainsboro', width=5, padx = 4, pady = 5)
button_six = Button(window, text='6', fg='black', bd=1, bg='gainsboro', width=5, padx = 4, pady = 5)
button_seven = Button(window, text='7', fg='black', bd=1, bg='gainsboro', width=5, padx = 4, pady = 5)
button_eight = Button(window, text='8', fg='black', bd=1, bg='gainsboro', width=5, padx = 4, pady = 5)
button_nine = Button(window, text='9', fg='black', bd=1, bg='gainsboro', width=5, padx = 4, pady = 5)
button_decimal = Button(window, text='.', fg='black', bd=1, bg='gray', width=5, padx=4, pady=5)
button_pi = Button(window, text='π', fg='black', bd=1, bg='gray', width=5, padx = 4, pady = 5)
button_zero.place(x=0, y=221)
button_seven.place(x=0, y=190)
button_eight.place(x=47, y=190)
button_nine.place(x=93, y=190)
button_four.place(x=0, y=160)
button_five.place(x=47, y=160)
button_six.place(x=93, y=160)
button_one.place(x=0, y=130)
button_two.place(x=47, y=130)
button_three.place(x=93, y=130)
button_decimal.place(x=47, y=221)
button_pi.place(x=93, y=221)

button_function_zero()
button_function_one()
button_function_two()
button_function_three()
button_function_four()
button_function_five()
button_function_six()
button_function_seven()
button_function_eight()
button_function_nine()
button_function_decimal()
button_function_pi()

add_button = Button(window, text='+', fg='black', bd=1, bg='gray', width=5, padx = 4, pady = 5)
button_function_addition()

subtract_button = Button(window, text='-', fg='black', bd=1, bg='gray', width=5, padx = 4, pady = 5)
button_function_subtraction()

divide_button = Button(window, text='÷', fg='black', bd=1, bg='gray', width=5, padx = 4, pady = 5)
button_function_division()

multiply_button = Button(window, text='x', fg='black', bd=1, bg='gray', width=5, padx = 4, pady = 5)
button_function_multiplication()

percent_button = Button(window, text='%', fg='black', bd=1, bg='gray', width=5, padx = 4, pady = 5)
button_function_percent()

square_root_button = Button(window, text='√', fg='black', bd=1, bg='gray', width=5, padx= 4, pady= 5)
button_function_square_root()

square_button = Button(window, text='x²', fg='black', bd=1, bg='gray', width=5, padx=4, pady= 5)
button_function_square()

add_button.place(x=141, y=190)
subtract_button.place(x=141, y=159)
divide_button.place(x=141, y=129.2)
multiply_button.place(x=141, y=98)
percent_button.place(x=141, y=221)
square_root_button.place(x=93, y=98)
square_button.place(x=47, y=98)

clear_button = Button(window, text='CE', fg='black', bd=1, bg='gray', width=5, padx = 4, pady = 5)
clear_button.place(x=0, y=98)
button_function_clear()

question_input = Entry(window, width=31)
question_input.place(x=0, y=78)

answer_button = Button(window, text='=',fg='black', bd=1, bg='gray64', width=26, command=solve, padx = 4, pady= 5)
answer_button.place(x=-6, y=252)

window.title('Single Equation Calculator')
window.geometry("200x300")
window.mainloop()
#---------------------
