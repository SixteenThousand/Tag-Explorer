# module for any generic functions used
import tkinter as tk
import tkinter.ttk as ttk

DEFAULT_MSG = """
	This is a mock window, here as a test handler for buttons in the main app.
	Please exit now.
"""

def display_msg(msg=DEFAULT_MSG):
	root = tk.Tk()
	root.title("---")
	ttk.Label(text=msg).grid(row=0,column=0)
	root.mainloop()
