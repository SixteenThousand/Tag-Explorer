import tkinter as tk
import tkinter.ttk as ttk
import mock
import search

def run():
	# the entrypoint of the whole application
	root = tk.Tk()
	root.title("Tag Explorer")
	root.rowconfigure(0,weight=1)
	root.columnconfigure(0,weight=1)
	style = ttk.Style()
	style.theme_use("winnative")
	frame = ttk.Frame(root)
	frame.grid(column=0,row=0,sticky="nw")
	populate(frame)
	root.mainloop()

class SearchWidget():
	def __init__(self,frame,name,row_num,widget_type):
		self.label = ttk.Label(frame,text=f"{name}: ")
		self.label.grid(row=row_num,column=0,sticky="e")
		self.search_term = tk.StringVar()
		self.entry = ttk.Entry(frame,width=50,textvariable=self.search_term)
		self.entry.grid(row=row_num,column=1,sticky="w")

def populate(frame):
	# input_box: frame containing all the input widgets; includes
	# - directory ("Library") search box
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
	
	
	# output_box: frame containing all the widgets that display the search 
	# results; includes
	# - list of titles of results
	output_box = ttk.Frame(frame)
	output_box.grid(row=0,column=1)
	
	# opt_box: the frame containing all the options/config widgets
	# includes:
	# - "New Library" button
	# - "Edit Library" button
	# - "New Book" button
	# - "Configuration" button
	opt_box = ttk.Frame(frame)
	opt_box.grid(row=2,column=0,columnspan=2)
	opt_widgets = [
		ttk.Button(opt_box,text="New Library",command=mock.button_handler),
		ttk.Button(opt_box,text="New Library",command=mock.button_handler),
		ttk.Button(opt_box,text="New Book",command=mock.button_handler),
		ttk.Button(opt_box,text="Configuration",command=mock.button_handler)
	];
	for i in range(len(opt_widgets)):
		opt_widgets[i].grid(row=0,column=i)


if __name__ =="__main__":
	run()
