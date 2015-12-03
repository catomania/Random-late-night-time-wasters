# http://zetcode.com/gui/tkinter/introduction/

from Tkinter import Tk, Frame, BOTH # importing Tk (root window) and Frame (widget container) classes

class Example(Frame): # example inherits from the Frame container widget

	def __init__(self, parent):
		Frame.__init__(self, parent, background="white") # save reference to parent widget, the Tk root window

		self.parent = parent

		self.initUI()

	def initUI(self): # creates the UI
		self.parent.title("Simple") # this uses the title method
		self.pack(fill=BOTH, expand=1) # pack method is a geometry manager in Tkinter, organizes widgets into boxes


def main():

	root = Tk() # main app window in our programs, has title bar and borders
	root.geometry("250x250+300+300") # width, height, x+y screen coordinates
	app = Example(root) # you create the Example class before using it
	root.mainloop() # mainloop event

if __name__ == '__main__':
	main()