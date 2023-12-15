import tkinter as tk
import tkinter.ttk as ttk
import mock
import search
import new_lib
import edit_lib
import new_book
import config

def run():
	# technically the entrypoint of the whole application
	root = tk.Tk()
	root.title("Tag Explorer")
	root.rowconfigure(0,weight=1)
	root.columnconfigure(0,weight=1)
	style = ttk.Style()
	style.theme_use("clam")
	frame = ttk.Frame(root)
	frame.grid(column=0,row=0,sticky="nw")
	populate(frame)
	root.mainloop()


class SearchWidget():
	def __init__(self,frame,name,row_num,widget_type=None):
		self.label = ttk.Label(frame,text=f"{name}: ")
		self.label.grid(row=row_num,column=0,sticky="e")
		if widget_type in [None,"entry"]:
			self.search_term = tk.StringVar()
			self.entry = ttk.Entry(frame,width=50,textvariable=self.search_term)
			self.entry.grid(row=row_num,column=1,sticky="w")
		elif widget_type == "list":
			mock.display_msg("Functionality not yet built!")
		else:
			mock.display_msg("An error has occurred.\nPlease panic now.")


def populate(frame):
	# library box: frame containing widgets needed to select a library to search
	# within
	# - directory ("Library") search box
	lib_box = ttk.Frame(frame)
	
	# input_box: frame containing all the input widgets; includes
	# - title search box
	# - list of possible tags
	# - other info search box
	# - "Search" button
	input_box = ttk.Frame(frame)
	input_box.grid(row=0,column=0)
	lib_sw = SearchWidget(input_box,"Library",0)
	title_sw = SearchWidget(input_box,"Title",1)
	other_info_sw = SearchWidget(input_box,"Other Information",2)
	tags_sw = SearchWidget(input_box,"Tags",3)
	search_b = ttk.Button(input_box,text="Search",command=mock.button_handler)
	search_b.grid(row=4,column=0,columnspan=2,sticky="e")
	
	# output_box: frame containing all the widgets that display the search 
	# results; includes
	# - list of titles of results
	output_box = ttk.Frame(frame)
	output_box.grid(row=1,column=0,columnspan=2)
	title_la = ttk.Label(output_box,text="Search Results")
	title_la.grid(row=0,column=0,sticky="s")
	results_list = tk.StringVar()
	results_lb = tk.Listbox(output_box,height=10,width=100,listvariable=results_list)
	# results_list.set(["thing1","thing2"])  # debug
	results_lb.grid(row=1,column=0)
	open_b = ttk.Button(output_box,text="Open",command=mock.button_handler)
	open_b.grid(row=2,column=0)
	
	# opt_box: the frame containing all the options/config widgets
	# includes:
	# - "New Library" button
	# - "Edit Library" button
	# - "New Book" button
	# - "Configuration" button
	opt_box = ttk.Frame(frame)
	opt_box.grid(row=0,column=1)
	opt_widgets = [
		ttk.Button(opt_box,text="New Library",command=mock.button_handler),
		ttk.Button(opt_box,text="Edit Library",command=mock.button_handler),
		ttk.Button(opt_box,text="New Book",command=mock.button_handler),
		ttk.Button(opt_box,text="Configuration",command=mock.button_handler)
	]
	for i in range(len(opt_widgets)):
		opt_widgets[i].grid(row=i,column=0)
	
	for subframe in frame.winfo_children():
		for child in subframe.winfo_children():
			child.grid_configure(padx=5, pady=5)


if __name__ =="__main__":
	run()
