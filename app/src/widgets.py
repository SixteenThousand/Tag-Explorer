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
	def __init__(self,frame,name,char_width):
		self.label = ttk.Label(frame,text=f"{name}: ")
		self.search_term = tk.StringVar()
		self.input_wg = ttk.Entry(
			frame,
			width=char_width,
			textvariable=self.search_term
		)
	
	def position(self,row,col):
		self.label.grid(row=row,column=col,sticky="ne")
		self.input_wg.grid(row=row,column=col+1,sticky="nw")


class SearchList():
	"""
		**DEPRECATED**
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
	
	def position(self,row,col):
		self.label.grid(row=row,column=col,sticky="ne")
		self.input_wg.grid(row=row,column=col+1,sticky="w")
	
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
	
	def __init__(self,parent,name,width,height):
		# declare a frame to hold all the widgets
		self.container = ttk.Frame(parent)
		# declare the actual widgets
		self.label = ttk.Label(parent,text=name)
		self.canvas = tk.Canvas(
			self.container,
			width=width,
			height=height,
			background=utils.DEFAULT_BG_COLOUR
		)
		self.scrollbar = ttk.Scrollbar(
			self.container,
			orient=tk.VERTICAL,
			command=self.canvas.yview
		)
		# frame that manages placement of checkboxes wothin the canvas
		self.inner_frame = ttk.Frame(self.canvas)
		# configuring the scrollbar
		self.canvas.configure(yscrollcommand=self.scrollbar.set)
		self.inner_frame.bind(
			"<Configure>",
			lambda evt: self.canvas.configure(
				scrollregion=self.canvas.bbox("all")
			)
		)
		# variables holding the current state
		self.checked = []
		# position the widgets relative to self.container
		self.canvas.create_window(0,0,anchor="nw",window=self.inner_frame)
		utils.put(self.canvas,0,1)
		utils.put(self.scrollbar,0,2,sticky="ns")
	
	def set_options(self,options):
		# sort the options so people can find stuff!
		options.sort(key=str.lower)
		# remove any existing entries in the checklist
		self.checked.clear()
		for child in self.inner_frame.winfo_children():
			child.destroy()
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
			self.checked.append(item_name)
			utils.put(box,i,0,sticky="nw")
	
	def position(self,row,col):
		utils.put(self.label,row,col,sticky="ne")
		utils.put(self.container,row,col+1,sticky="nw")
	
	def get_selection(self):
		return list(filter(None,map(lambda x: x.get(),self.checked)))


class SelectList():
	"""
		Widget that displays a scrollable list of items that the user can 
		choose exactly one of. Essentially a glorified wrapper around the 
		ttk.Treeview widget.
	"""
	
	def __init__(self,parent,num_rows,width):
		self.container = ttk.Frame(parent)
		self.tree = ttk.Treeview(
			self.container,
			height=num_rows,
			selectmode="browse"
		)
		self.tree.column("#0",width=width)
		self.scrollbar = ttk.Scrollbar(
			self.container,
			orient=tk.VERTICAL,
			command=self.tree.yview
		)
		self.tree.configure(yscrollcommand=self.scrollbar.set)
		# postion the widgets relative to container
		utils.put(self.tree,0,0)
		utils.put(self.scrollbar,0,1,sticky="ns")
		# list of IDs of self.tree`s items
		self._options = []
	
	def set_options(self,new_options):
		for option in self._options:
			self.tree.delete(option)
		self._options.clear()
		for option in new_options:
			self._options.append(self.tree.insert("","end",text=option))
	
	def put(self,row,col,**kwargs):
		utils.put(self.container,row,col,**kwargs)
	
	def get_selection(self):
		# selection returns ("I{1-indexed, hexdecimal, index of item}",)
		# for children of the root item
		# NOTE: index of item includes *deleted items*
		return self._options.index(self.tree.selection()[0])
	
	def on_selection(self,func):
		self.tree.bind("<<TreeviewSelect>>",func)


class HelpButton():
	"""
		Wrapper for ttk.Button. Opens a new window with a message from a given
		file.
	"""
	
	def __init__(self,parent,msg_file):
		self.button = ttk.Button(
			parent,
			text="Help...",
			command=lambda: utils.display_msg(msg_file,True)
		)
	
	def put(self,row,column,**kwargs):
		utils.put(self.button,row,column,**kwargs)
