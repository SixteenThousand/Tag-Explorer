import tkinter as tk
import tkinter.ttk as ttk
import ast
import widgets as wg
import utils
import search
import new_lib
import edit_lib
import new_book
import config


root = tk.Tk()
root.title("Tag Explorer")
style = ttk.Style()
style.theme_use("clam")
frame = ttk.Frame(root)

# output_box: frame containing all the widgets that display the search 
# results. Contains:
# - list of titles of results
# - label indicating currently selected result
# - "Open" button which allows the user to open the selected result in the current
# system default
output_box = ttk.Frame(frame)
output_box_title = ttk.Label(
		output_box,
		text="Results"
)
results_list = tk.StringVar()
results_lb = tk.Listbox(
		output_box,
		height=10,
		width=100,
		listvariable=results_list,
		selectmode="browse"  # only allows one item to be selected at a time
)
open_bu = ttk.Button(
		output_box,
		text="Open",
		command=utils.display_msg
)

# input_box: frame containing all the input widgets. Contains:
# - title search box
# - list of possible tags
# - other info search box
# - "Search" button
input_box = ttk.Frame(frame)
input_box_title = ttk.Label(
		input_box,
		text="Search terms"
)
title_sw = wg.SearchEntry(
		input_box,
		"Title"
)
other_info_sw = wg.SearchEntry(
		input_box,
		"Other Information"
)
tags_sl = wg.SearchList(
		input_box,
		"Tags",
		6,
		"extended"  # allows multiple items to be selected at once
)
search_bu = ttk.Button(
		input_box,
		text="Search...",
		command=utils.display_msg
)

# library box: frame containing widgets needed to select a library to search
# within. Contains:
# - directory ("Library") search box
lib_box = ttk.Frame(frame)
lib_box_title = ttk.Label(
		lib_box,
		text="Library"
)
lib_sl = wg.SearchList(
		lib_box,
		"Select Library",
		3,
		"browse"  # only allows one item to be selected at a time
)
def select_library():
	search.get_library_data(lib_sl.get_selection()[0])
	tags_sl.options.set(list(search.lib_tags))
select_bu = ttk.Button(
		lib_box,
		text="Confirm",
		command=select_library
)

# opt_box: the frame containing all the options/config widgets. Contains:
# - "New Library" button
# - "Edit Library" button
# - "New Book" button
# - "Configuration" button
opt_box = ttk.Frame(frame)
opt_box_title = ttk.Label(
		opt_box,
		text="Options..."
)
opt_widgets = [
	ttk.Button(
		opt_box,
		text="New Library",
		command=utils.display_msg
	),
	ttk.Button(
		opt_box,
		text="Edit Library",
		command=utils.display_msg
	),
	ttk.Button(
		opt_box,
		text="New Book",
		command=utils.display_msg
	),
	ttk.Button(
		opt_box,
		text="Configuration",
		command=utils.display_msg
	)
]




def populate():
	# decides where all the widgets should go
	root.rowconfigure(0,weight=1)
	root.columnconfigure(0,weight=1)
	frame.grid(column=0,row=0,sticky="nw")
	# +++ THE LIBRARY BOX +++
	lib_box.grid(row=0,column=0,columnspan=2)
	lib_box_title.grid(row=0,column=0,columnspan=2)
	lib_sl.position(1,0)
	select_bu.grid(row=1,column=2)
	# +++ THE INPUT BOX +++
	input_box.grid(row=1,column=0,sticky="n")
	input_box_title.grid(row=0,column=0,columnspan=2)
	title_sw.position(1,0)
	other_info_sw.position(2,0)
	tags_sl.position(3,0)
	search_bu.grid(row=4,column=0,columnspan=2,sticky="e")
	# +++ THE RESULTS BOX +++
	output_box.grid(row=1,column=1,sticky="n")
	output_box_title.grid(row=0,column=0,columnspan=2)
	results_lb.grid(row=2,column=0)
	open_bu.grid(row=3,column=0)
	# +++ THE OPTIONS/CONFIGURATION BOX +++
	opt_box.grid(row=2,column=0,columnspan=2)
	opt_box_title.grid(row=0,column=0,columnspan=len(opt_widgets))
	for i in range(len(opt_widgets)):
		opt_widgets[i].grid(row=0,column=i+1)
	
	# add a little padding around all widgets
	for subframe in frame.winfo_children():
		for child in subframe.winfo_children():
			child.grid_configure(padx=5, pady=5)


def run():
	# technically the entrypoint of the whole application
	search.setup()
	lib_sl.options.set(list(search.libs.keys()))
	populate()
	root.mainloop()

if __name__ =="__main__":
	run()
