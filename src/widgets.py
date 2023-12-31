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

class CheckList():
	"""
		Custom tk widget that displays a scrollable list of checkboxes and an 
		API to access the state of those checkboxes.
	"""
	def __init__(self,parent,width,height):
		self.canvas = tk.Canvas(parent,width=width,height=height)
		self.frame = ttk.Frame(self.canvas)
		self.checkboxes = []
		self.checked = []
		self.canvas.create_window(50,50,anchor="nw",window=self.frame)
	
	def set_options(self,options):
		self.checkboxes.clear()
		self.checked.clear()
		for i in range(len(options)):
			item_name = tk.StringVar()
			box = ttk.Checkbutton(
				self.frame,
				text=options[i],
				variable=item_name,
				onvalue=options[i],
				offvalue=""
			)
			self.checkboxes.append(box)
			self.checked.append(item_name)
			utils.put(box,i,0,sticky="w")
