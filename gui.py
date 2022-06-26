from tkinter import *
from functools import partial
from mySearch import quickSearch

root = Tk()

def myClick(entry):
    result = quickSearch(entry.get())
    if result == -1:
        resultText = "Keyword not found"
    else:
        resultText = "Keyword '" + entry.get() + "' found at line " + str(result)
    resultLabel = Label(root, text=resultText)
    resultLabel.grid(column=0, row=2, columnspan=2)

# Create a label midget
myTitle = Label(root, text="myKeylogger")

# Create an entry widget to input data
searchEntry = Entry(root, width=20, borderwidth=2)

# Create a button
searchButton = Button(root, text="Enter", padx=10, command=partial(myClick, searchEntry))

# Place title on screen
myTitle.grid(column=0, row=0, columnspan=2)
# Shove entry widget onto screen
searchEntry.grid(column=0, row=1)

# Shove button onto screen
searchButton.grid(column=1, row=1)

root.mainloop()