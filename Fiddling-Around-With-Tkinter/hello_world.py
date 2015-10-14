# http://www.tutorialspoint.com/python/tk_label.htm
from Tkinter import * 

root = Tk()

var = StringVar()

label = Label(root, textvariable=var, relief=RAISED )

var.set("Hello world!")
label.pack()
root.mainloop()
