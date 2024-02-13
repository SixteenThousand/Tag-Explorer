import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import widgets as wg
import utils
import backend
import new_lib
import new_book


class LibraryBox(tk.Frame):
	"""
		Library box
		The frame containing widgets needed to select a library to search 
		within.
		Exposes:
		- current_lib: tk.StringVar; stores the path to the library currently 
		  selected by the user
	"""
	
	def __init__(self,input_box):
		self.__init__()
		self.current_lib = tk.StringVar()
		self.__title = ttk.Label(
			self,
			text="Library"
		)
		self.__lib_list = wg.SelectList(
			self,
			3
		)
		self.__lib_dialog = ttk.Button(
			self,
			text="Choose Directory..."
		)
		self.__current_lib_legend = ttk.Label(
			self,
			text="Selected library:"
		)
		self.__current_lib_label = ttk.Label(
			self,
			textvariable=self.current_lib
		)
	
	def on_selection(self,handler):
		"""
			Binds handler to any events that cause self.current_lib to change, 
			and passes the new value of self.current_lib to handler.
		"""
		self.__lib_list.on_selection(
			lambda _: handler(backend.libs[self.__lib_list.get_selection()])
		)
		self.__lib_dialog.configure(
			command = lambda: handler(filedialog.askdirectory())
		)
	
	def position(self,row,col,**kwargs):
		utils.put(self,row,col,**kwargs)
		utils.put(self.__title,0,0,columnspan=2)
		utils.put(self.__lib_list,1,0,sticky="e")
		utils.put(self.__lib_dialog,1,0,sticky="w")
		utils.put(self.__current_lib_legend,2,0,sticky="w")
		utils.put(self.__current_lib_label,2,1,sticky="e")




class InputBox(tk.Frame):
	"""
		InputBox
		The frame containing all search query widgets.
		Exposes:
		- 
	"""
	
	def __init__(self):
		self.__init__()
		self.__title = ttk.Label(
			self,
			text="Search terms"
		)
		self.__book_title = wg.SearchEntry(
			self,
			"Title"
		)
		self.__other_info = wg.SearchEntry(
			self,
			"Other Information"
		)
		self.__tags = wg.CheckList(
			self,
			"Tags:",
			180,
			100
		)
		self.__search_button = ttk.Button(
			self,
			text="Search...",
			command=self.perform_search
		)
	
	def on_search(self,handler):
		backend.search(
			self.__book_title.search_term.get(),
			self.__other_info.search_term.get(),
			self.__tags.get_selection()
		)
		self.__search_button.configure(
			command = handler
		)
	

class OutputBox(tk.Frame):
	"""
		output_box: frame containing all the widgets that display the search 
		results. Contains: 
		- list of titles of results 
		- label indicating currently selected result 
		- "Open" button which allows the user to open the selected result in 
		  the current system default
	"""
	
	def __init__(self):
		self.__init__()
		self.selected_result = tk.StringVar()
		self.__title = ttk.Label(
			self,
			text="Results"
		)
		self.__results_list = wg.SelectList(
			self,
			7
		)
		self.__results_list.on_selection(
			lambda _: self.selected_result.set(
				backend.results[self.__results_list.get_selection()]
			)
		)
		self.selected_label = ttk.Label(
			self,
			textvariable=self.selected_result
		)
		self.open_button = ttk.Button(
			self,
			text="Open",
			command=self.open_result
		)
	
	def open_result(self):
		backend.results[self.__results_list.get_selection()].sys_open()
	
	def set_results(self,results):
		self.__results_list.set_options(results)


class OptionsBox(tk.Frame):
	"""
		opt_box: the frame containing all the options/config widgets. Contains:
		- "New Library" button
		- "New Book" button
		- "Help" button
	"""
	
	def __init__(self):
		self.__init__()
		self.__title = ttk.Label(
			self,
			text="Options..."
		)
		self.buttons = [
			ttk.Button(
				self,
				text="New Library",
				command=new_lib.run
			),
			ttk.Button(
				self,
				text="New Book",
				command=utils.display_msg
			),
			ttk.Button(
				self,
				text="Help...",
				command=utils.display_msg
			)
		]
	
	def position(self,row,col,**kwargs):
		self.grid(row=row,column=col,**kwargs)
		utils.put(self.__title,0,0,columnspan=len(self.buttons))
		for i in range(self.buttons):
			utils.put(self.buttons[i],0,i)


class App(tk.Tk):
	"""
		The main application window. Controls everything.
	"""
	
	def __init__(self):
		self.__init__()
		self.title("Tag Explorer")
		self.frame = ttk.Frame(self)
		self.lib_box = LibraryBox()
		self.input_box = InputBox()
		self.output_box = OutputBox()
		self.opts_box = OptionsBox()
		# set up event listeners
		self.input_box.on_search(
			lambda: self.output_box.set_results(
				[str(x) for x in backend.results]
			)
		)
	
	def choose_lib(path):
		backend.get_library_data(path)
		tags_cl.set_options(list(backend.lib_tags))
		current_lib_var.set(backend.current_lib)

	def populate(self):
		# decides where all the widgets should go
		self.rowconfigure(0,weight=1)
		self.columnconfigure(0,weight=1)
		utils.put(self.frame,0,0,sticky="nw")
		# +++ THE LIBRARY BOX +++
		utils.put(lib_box,0,0,columnspan=2)
		utils.put(lib_box_title,0,0,columnspan=2)
		lib_sl.put(1,0)
		utils.put(lib_dialog_bu,1,1)
		utils.put(current_lib_legend_la,3,0,sticky="e")
		utils.put(current_lib_la,3,1,sticky="w")
		# +++ THE INPUT BOX +++
		utils.put(input_box,1,0,sticky="n")
		utils.put(input_box_title,0,0,columnspan=2)
		title_sw.position(1,0)
		other_info_sw.position(2,0)
		tags_cl.position(3,0)
		utils.put(search_bu,4,0,columnspan=2,sticky="e")
		# +++ THE RESULTS BOX +++
		utils.put(output_box,1,1,sticky="n")
		utils.put(output_box_title,0,0,columnspan=2)
		results_sl.put(1,0,columnspan=2)
		utils.put(result_la,3,0)
		utils.put(open_bu,3,1)
		
		# add a little padding around all widgets
		for subframe in frame.winfo_children():
			for child in subframe.winfo_children():
				child.grid_configure(padx=5, pady=5)
	
	def run():
		# technically the entrypoint of the whole application
		backend.setup()
		lib_sl.set_options(backend.libs)
		utils.add_theme(self)
		self.populate()
		self.mainloop()

if __name__ == "__main__":
	app = App()
	app.run()
