from tkinter import *
from tkinter import ttk
from simple_calculator import *


def calculate(*args):
    try:
        equation = str(inputValue.get())
        outputValue.set(simple_compute(equation))
    except ValueError:
        pass


root = Tk()
root.title("Simple Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

inputValue = StringVar()
outputValue = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=inputValue)
feet_entry.grid(column=1, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=outputValue).grid(column=1, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Enter calculation here: ").grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="Result: ").grid(column=0, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
