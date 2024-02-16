# module for any generic functions used
import tkinter as tk
import tkinter.ttk as ttk


def add_theme(root):
	styling = ttk.Style()
	root.tk.call(
		"lappend",
		"auto_path",
		"./themes/awthemes-10.4.0"
	)
	root.tk.call("package","require","awdark")
	styling.theme_use("awdark")


DEFAULT_MSG = """
This is a mock window, here as a test handler for buttons.
Please close this window.
"""

def display_msg(msg=DEFAULT_MSG,isfile=False):
	if isfile:
		fp = open(msg,"r",encoding="utf-8")
		lines = [line for line in fp]
		fp.close()
		msg = "".join(lines)
	root = tk.Toplevel()
	root.title("---")
	frame = ttk.Frame(root)
	frame.grid(row=0,column=0)
	ttk.Label(frame,text=msg).grid(row=0,column=0)
	add_theme(root)
	root.mainloop()


def get_pyobj(s):
	"""
		Takes a string that is the representation of a python expression, and
		converts it to that python expression.
	"""
	return eval(compile(s,"<string>","eval"))


def put(tk_obj,row,column,**kwargs):
	tk_obj.grid(row=row,column=column,**kwargs)


def to_unix(path):
	"""Takes a path-like object and converts it to a unix-syle path."""
	return path.replace("\\","/")


def abs_to_rel(path,ancestor):
	"""Removes one path-like object from the start of another"""
	path = to_unix(path)
	ancestor = to_unix(ancestor)
	if path.startswith(ancestor):
		result = path[len(ancestor):]
	else:
		return path
	if result[0] == "/":
		return result[1:]
	return result
