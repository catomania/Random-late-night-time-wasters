# http://zetcode.com/gui/tkinter/drawing/

# exploring how to draw in Tkinter (using canvas widget)

# draw rectangles and also make classes!

from Tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent # this is in the Sudoku tutorial as well
		self.initUI() # same as in Sudoku tutorial

	def initUI(self):

		self.parent.title("Colors") # is parent = the background frame?
		self.pack(fill=BOTH, expand=1) # what is pack, fill, and expand? 

		canvas = Canvas(self)
		canvas.create_rectangle(30, 10, 120, 80, outline="#fb0", fill="#fb0")
		canvas.create_rectangle(150, 10, 240, 80, outline="#05f", fill="#05f")
		canvas.pack(fill=BOTH, expand=1)


def main():
	root=Tk()
	ex = Example(root) #so Tk() is frame
	root.geometry("400x100+300+300") # how big the window is?
	root.mainloop()

if __name__ == "__main__":
	main()
