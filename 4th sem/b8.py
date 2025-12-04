'''from tkinter import *
from tkinter import messagebox
import csv
import pandas as pd
import matplotlib.pyplot as plt
# Create CSV file with header if not exists
header = ['Batsman', 2017, 2018, 2019, 2020]
try:
with open('cricket.csv', 'x', newline='') as f:
writer = csv.writer(f)
writer.writerow(header)
except FileExistsError:
pass # File already exists
# Clear input fields
def clear():
btext.delete(0, END)
y1text.delete(0, END)
y2text.delete(0, END)
y3text.delete(0, END)
y4text.delete(0, END)
btext.focus_set()
# Submit data to CSV
def submit():
if btext.get() and y1text.get() and y2text.get() and y3text.get() and y4text.get():
try:
row = [
btext.get(),
int(y1text.get()),
int(y2text.get()),
int(y3text.get()),
int(y4text.get())
]
with open('cricket.csv', 'a', newline='') as f:
writer = csv.writer(f)
writer.writerow(row)
messagebox.showinfo(message='Submission Successful')
clear()
except ValueError:
messagebox.showerror("Invalid input", "Please enter valid integers for runs.")
else:
messagebox.showwarning('Missing Data', 'Enter all values')
# Plotting function
def plot_data():
df = pd.read_csv('cricket.csv')
df.plot(x='Batsman', kind='bar', title='Cricket Statistics', xlabel='Batsman', ylabel='Runs
Scored')
plt.xticks(rotation=10)
plt.tight_layout()
plt.show()
# Main GUI
if __name__ == '__main__':
win = Tk()
win.configure(background='light grey')
win.geometry('350x320')
win.title("Input Cricket Statistics")
# Labels
Label(win, text="Batsman:", bg='light blue').grid(row=1, column=0, padx=10, pady=5)
Label(win, text="Runs in year 2017:", bg='light blue').grid(row=2, column=0, padx=10,
pady=5)
Label(win, text="Runs in year 2018:", bg='light blue').grid(row=3, column=0, padx=10,
pady=5)
Label(win, text="Runs in year 2019:", bg='light blue').grid(row=4, column=0, padx=10,
pady=5)
Label(win, text="Runs in year 2020:", bg='light blue').grid(row=5, column=0, padx=10,
pady=5)
# Entry fields
btext = Entry(win)
y1text = Entry(win)
y2text = Entry(win)
y3text = Entry(win)
y4text = Entry(win)
btext.grid(row=1, column=1, padx=10, pady=5)
y1text.grid(row=2, column=1, padx=10, pady=5)
y2text.grid(row=3, column=1, padx=10, pady=5)
y3text.grid(row=4, column=1, padx=10, pady=5)
y4text.grid(row=5, column=1, padx=10, pady=5)
# Buttons
Button(win, text="Submit", bg="red", fg="black", command=submit).grid(row=6, column=0,
pady=10)
Button(win, text="Clear", bg="red", fg="black", command=clear).grid(row=6, column=1,
pady=10)
Button(win, text="Plot Data", bg="green", fg="white", command=plot_data).grid(row=7,
columnspan=2, pady=10)
btext.focus_set()
win.mainloop()'''