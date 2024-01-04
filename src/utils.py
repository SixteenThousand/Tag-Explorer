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
	frame = ttk.Frame(root)
	frame.grid(row=0,column=0)
	ttk.Label(frame,text=msg).grid(row=0,column=0)
	root.mainloop()

def get_pyobj(s):
	"""
		Takes a string that is the representation of a python expression, and
		converts it to that python expression.
	"""
	return eval(compile(s,"<string>","eval"))

def put(tk_obj,row,column,**kwargs):
	tk_obj.grid(row=row,column=column,**kwargs)
