"""
Magic 8 Ball: Takes a user question and shows a random response. Please note: there isn't yet
any input validation for this exercise
"""

from Tkinter import *
import ttk
from random import randrange

fortunes_list = [
"Yes, in due time.",
"My sources say no.",
"Definitely not.",
"Yes.",
"You will have to wait.",
"I have my doubts.",
"Outlook so so."]

# ask button, returns a fortune
def ask_question():
	random_answer = randrange(0, int(len(fortunes_list)))
	fortune_display.set(fortunes_list[random_answer])

# play again button
def play_again():
	# clear response and question
	try:
		question.set("")
		fortune_display.set("")
	except ValueError:
		pass

# quit button 
def quit_button():
	raise SystemExit

# GUI portion

root = Tk()
root.title("Magic 8 Ball")

mainframe = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1) # if the main window is resized, the frame should expand to take up the extra space.
mainframe.rowconfigure(0, weight=1)

# string variables to gather question and display fortune
question = StringVar()
fortune_display = StringVar()

# entry box for question
question_entry = ttk.Entry(mainframe, width=110, textvariable=question)
question_entry.grid(column=2, row=1, sticky=(W, E))

# labels
ttk.Label(mainframe, text="Question").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Fortune:").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, textvariable=fortune_display).grid(column=2, row=2, sticky=W)

# padding around each widget
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# action buttons
ttk.Button(mainframe, text="Ask", command=ask_question).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="Play Again", command=play_again).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="Quit", command=quit_button).grid(column=3, row=4, sticky=W)


# moves cursor automatically to the input text box
question_entry.focus()
root.bind('<Return>', ask_question)

root.mainloop()
