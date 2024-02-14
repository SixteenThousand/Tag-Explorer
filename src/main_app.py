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
		- lib_list: widgets.SelectList; a list of currently managed libraries 
		  - at least at time of opening TagEx - which the user can select a
		  library to search from.
	"""
	
	def __init__(self,parent):
		super().__init__(parent)
		self.current_lib = tk.StringVar()
		self._title = ttk.Label(
			self,
			text="Library"
		)
		self.lib_list = wg.SelectList(
			self,
			3
		)
		self._lib_dialog = ttk.Button(
			self,
			text="Choose Directory..."
		)
		self._current_lib_legend = ttk.Label(
			self,
			text="Selected library:"
		)
		self._current_lib_label = ttk.Label(
			self,
			textvariable=self.current_lib
		)
	
	def on_selection(self,handler):
		"""
			Binds handler to any events that cause self.current_lib to change, 
			and passes the new value of self.current_lib to handler.
		"""
		self.lib_list.on_selection(
			lambda _: handler(backend.libs[self.lib_list.get_selection()])
		)
		self._lib_dialog.configure(
			command = lambda: handler(filedialog.askdirectory())
		)
	
	def put(self,row,col,**kwargs):
		utils.put(self,row,col,**kwargs)
		utils.put(self._title,0,0,columnspan=2)
		self.lib_list.put(1,0,sticky="e")
		utils.put(self._lib_dialog,1,1,sticky="w")
		utils.put(self._current_lib_legend,2,0,sticky="w")
		utils.put(self._current_lib_label,2,1,sticky="e")




class InputBox(tk.Frame):
	"""
		InputBox
		The frame containing all search query widgets.
		Exposes:
		- 
	"""
	
	def __init__(self,parent):
		super().__init__(parent)
		self._title = ttk.Label(
			self,
			text="Search terms"
		)
		self._book_title = wg.SearchEntry(
			self,
			"Title"
		)
		self._other_info = wg.SearchEntry(
			self,
			"Other Information"
		)
		self._tags = wg.CheckList(
			self,
			"Tags:",
			180,
			100
		)
		self._search_button = ttk.Button(
			self,
			text="Search..."
		)
	
	def on_search(self,handler):
		"""Sets handler for search button."""
		self._search_button.configure(
			command = lambda: self.perform_search(handler)
		)
	
	def perform_search(self,handler):
		"""
			Performs a search of the current library for books matching the 
			currently selected search inputs.
			- handler: Callable[[],NoReturn]; sets some other widget to display 
			  the results somewhere else.
		"""
		backend.search(
			self._book_title.search_term.get(),
			self._other_info.search_term.get(),
			self._tags.get_selection()
		)
		handler()
	
	def put(self,row,col,**kwargs):
		utils.put(self,row,col,**kwargs)
		utils.put(self._title,0,0,columnspan=2)
		self._book_title.position(1,0)
		self._other_info.position(2,0)
		self._tags.position(3,0)
		utils.put(self._search_button,4,0,columnspan=2)
	
	def set_options(self,path):
		"""Handler for LibraryBox.on_selection."""
		backend.get_library_data(path)
		self._tags.set_options(list(backend.lib_tags))

class OutputBox(tk.Frame):
	"""
		output_box: frame containing all the widgets that display the search 
		results. Contains: 
		- list of titles of results 
		- label indicating currently selected result 
		- "Open" button which allows the user to open the selected result in 
		  the current system default
	"""
	
	def __init__(self,parent):
		super().__init__(parent)
		self.selected_result = tk.StringVar()
		self._title = ttk.Label(
			self,
			text="Results"
		)
		self._results_list = wg.SelectList(
			self,
			7
		)
		self._results_list.on_selection(
			lambda _: self.selected_result.set(
				backend.results[self._results_list.get_selection()]
			)
		)
		self._selected_label = ttk.Label(
			self,
			textvariable=self.selected_result
		)
		self._open_button = ttk.Button(
			self,
			text="Open",
			command=self.open_result
		)
	
	def put(self,row,col,**kwargs):
		utils.put(self,row,col,**kwargs)
		utils.put(self._title,0,0,columnspan=2)
		self._results_list.put(1,0,columnspan=2)
		utils.put(self._selected_label,2,0)
		utils.put(self._open_button,2,1)
	
	def open_result(self):
		backend.results[self._results_list.get_selection()].sys_open()
	
	def set_results(self,results):
		self._results_list.set_options(results)


class OptionsBox(tk.Frame):
	"""
		Options Box
		The frame containing all the options/config widgets. Contains:
		- "New Library" button
		- "New Book" button
		- "Help" button
	"""
	
	def __init__(self,parent):
		super().__init__(parent)
		self._title = ttk.Label(
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
	
	def put(self,row,col,**kwargs):
		self.grid(row=row,column=col,**kwargs)
		utils.put(self._title,0,0,columnspan=len(self.buttons))
		for i in range(len(self.buttons)):
			utils.put(self.buttons[i],0,i)


class App(tk.Tk):
	"""
		The main application window. Controls everything.
	"""
	
	def __init__(self):
		# ensure the backend has initialised everything before *anything*  
		# happens
		backend.setup()
		super().__init__()
		self.title("Tag Explorer")
		self.frame = ttk.Frame(self)
		self.lib_box = LibraryBox(self.frame)
		self.input_box = InputBox(self.frame)
		self.output_box = OutputBox(self.frame)
		self.opts_box = OptionsBox(self.frame)
	
	def populate(self):
		# place everything
		utils.put(self.frame,0,0)
		self.lib_box.put(0,0,columnspan=2)
		self.input_box.put(1,0)
		self.output_box.put(1,1)
		self.opts_box.put(2,0,columnspan=2)
		# add event handlers
		self.lib_box.on_selection(self.input_box.set_options)
		self.input_box.on_search(
			lambda: self.output_box.set_results(
				[str(x) for x in backend.results]
			)
		)
		# add a little padding around all widgets
		for subframe in self.frame.winfo_children():
			for child in subframe.winfo_children():
				child.grid_configure(padx=5, pady=5)
	
	def run(self):
		# technically the entrypoint of the whole application
		self.lib_box.lib_list.set_options(backend.libs)
		utils.add_theme(self)
		self.populate()
		self.mainloop()

if __name__ == "__main__":
	app = App()
	app.run()
