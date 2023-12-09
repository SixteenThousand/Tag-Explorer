# module for any mocks used in testing
import tkinter as tk
import tkinter.ttk as ttk

def button_handler():
	root = tk.Tk()
	root.title("+++TEST+++")
	msg = ttk.Label(text="This is a mock window, here as a default handler for buttons in the main app.\nPlease exit now.")
	msg.grid(row=0,column=0)
	root.mainloop()
