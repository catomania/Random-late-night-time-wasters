# http://www.tutorialspoint.com/python/tk_pack.htm

# exploring pack options

from Tkinter import *

root = Tk() 
frame = Frame(root) #Frame(Tk())

# does this line need to happen before we can use Frame(root) for our buttons?
frame.pack() #widget.pack(pack_options), Frame(Tk()).pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

redbutton = Button(frame, text="Ruby", fg="red")
redbutton.pack(side=LEFT)

brownbutton = Button(frame, text="Zhongse", fg="brown")
brownbutton.pack(side=RIGHT)

bluebutton = Button(frame, text="Sapphire", fg="blue")
bluebutton.pack(side=BOTTOM)

blackbutton = Button(frame, text="Ink", fg="black")
blackbutton.pack(side=TOP)

root.mainloop() # this is what gets the window to show up

# what about expand and fill?
