from tkinter import *


# Function to update the input expression
def press(num):
 global expression
 expression = expression + str(num)
 equation.set(expression)


# Function to evaluate the expression
def equalpress():
 try:
  global expression
  total = str(eval(expression))
  equation.set(total)
  expression = ""
 except:
  equation.set("Error")
  expression = "" 



# Function to clear the input field
def clear():
 global expression
 expression = ""
 equation.set("")


# Main GUI window
window = Tk()
window.title("Simple Calculator")
window.geometry("500x500")
expression = ""
equation = StringVar()



# Entry widget to display the expression
expression_field = Entry(window, textvariable=equation, font=('Arial', 20))
expression_field.grid(columnspan=4, ipadx=8, ipady=25)


# Buttons
Button(window, text='1', fg='black', height=2, width=7, command=lambda:press(1)).grid(row=2, column=0)
Button(window, text='2', fg='black', height=2, width=7, command=lambda:press(2)).grid(row=2, column=1)
Button(window, text='3', fg='black', height=2, width=7, command=lambda:press(3)).grid(row=2, column=2)
Button(window, text='+', fg='black', height=2, width=7, command=lambda:press('+')).grid(row=2, column=3)
Button(window, text='4', fg='black', height=2, width=7, command=lambda:press(4)).grid(row=3, column=0)
Button(window, text='5', fg='black', height=2, width=7, command=lambda:press(5)).grid(row=3, column=1)
Button(window, text='6', fg='black', height=2, width=7, command=lambda:press(6)).grid(row=3, column=2)
Button(window, text='-', fg='black', height=2, width=7, command=lambda:press('-')).grid(row=3, column=3)
Button(window, text='7', fg='black', height=2, width=7, command=lambda:press(7)).grid(row=4, column=0)
Button(window, text='8', fg='black', height=2, width=7, command=lambda:press(8)).grid(row=4, column=1)
Button(window, text='9', fg='black', height=2, width=7, command=lambda:press(9)).grid(row=4, column=2)
Button(window, text='*', fg='black', height=2, width=7, command=lambda:press('*')).grid(row=4, column=3)
Button(window, text='0', fg='black', height=2, width=7, command=lambda:press(0)).grid(row=5, column=0)
Button(window, text='C', fg='black', height=2, width=7, command=clear).grid(row=5,column=1)
Button(window, text='=', fg='black', height=2, width=7, command=equalpress).grid(row=5,column=2)
Button(window, text='/', fg='black', height=2, width=7, command=lambda:press('/')).grid(row=5, column=3)


# Run the GUI loop
window.mainloop()