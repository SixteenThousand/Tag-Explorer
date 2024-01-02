import tkinter as tk
import tkinter.ttk as ttk
import utils

class SearchEntry():
	"""
		'Wrapper' class for the Entry widget.
		Adds a label widget that it positions relative to the Entry widget.
		Attributes:
		- label: ttk.Label; The label widget mentioned above.
		- search_term: tk.StringVar; The user's input.
		- input_wg: ttk.Entry; The Entry widget
	"""
	def __init__(self,frame,name):
		self.label = ttk.Label(frame,text=f"{name}: ")
		self.search_term = tk.StringVar()
		self.input_wg = ttk.Entry(
			frame,
			width=50,
			textvariable=self.search_term
		)
	
	def position(self,r,c):
		self.label.grid(row=r,column=c,sticky="e")
		self.input_wg.grid(row=r,column=c+1,sticky="w")

class SearchList():
	"""
		'Wrapper' class for the Listbox widget.
	"""
	def __init__(self,frame,name,height,mode):
		self.label = ttk.Label(frame,text=f"{name}: ")
		self.options = tk.StringVar()
		self.input_wg = tk.Listbox(
			frame,
			width=50,
			height=height,
			listvariable=self.options,
			selectmode=mode
		)
	
	def position(self,r,c):
		self.label.grid(row=r,column=c,sticky="ne")
		self.input_wg.grid(row=r,column=c+1,sticky="w")
	
	def get_selection(self):
		return [
				utils.get_pyobj(self.options.get())[i] 
				for i in self.input_wg.curselection()
		]
