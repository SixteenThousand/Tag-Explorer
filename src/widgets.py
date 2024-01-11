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
	
	MAX_SCROLLSIZE  = 10000
		# believe it or not, this was the simplest way to get scrolling to work.
		# I hate it.
	
	def __init__(self,parent,width,height):
		self.container = ttk.Frame(parent)
		self.canvas = tk.Canvas(
			self.container,
			width=width,
			height=height,
			scrollregion=(0,0,width,CheckList.MAX_SCROLLSIZE),
			background="#33393b"
		)
		self.scrollbar = ttk.Scrollbar(
			self.container,
			orient=tk.VERTICAL,
			command=self.canvas.yview
		)
		self.canvas["yscrollcommand"] = self.scrollbar.set
		self.inner_frame = ttk.Frame(self.canvas)
		self.checkboxes = []
		self.checked = []
		self.canvas.create_window(0,0,anchor="nw",window=self.inner_frame)
	
	def set_options(self,options):
		# remove any existing entries in the checklist
		self.checkboxes.clear()
		self.checked.clear()
		# create the new checkboxes & position them within the canvas
		for i in range(len(options)):
			item_name = tk.StringVar()
			box = ttk.Checkbutton(
				self.inner_frame,
				text=options[i],
				variable=item_name,
				onvalue=options[i],
				offvalue="",
				width=self.canvas["width"]
			)
			self.checkboxes.append(box)
			self.checked.append(item_name)
			utils.put(box,i,0,sticky="nw")
	
	def put(self,row,col,**kwargs):
		utils.put(self.canvas,0,0)
		utils.put(self.scrollbar,0,1,sticky="ns")
		self.container.grid(row=row,column=col,**kwargs)
