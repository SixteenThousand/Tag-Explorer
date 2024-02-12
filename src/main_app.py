import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import widgets as wg
import utils
import backend
import new_lib
import new_book


root = tk.Tk()
root.title("Tag Explorer")
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
results_sl = wg.SelectList(
	output_box,
	7
)
selected_result= tk.StringVar()
results_sl.on_selection(
	lambda evt: selected_result.set(
		backend.results[results_sl.get_selection()]
	)
)
result_la = ttk.Label(output_box,textvariable=selected_result)
def open_result():
	backend.results[results_sl.get_selection()].sys_open()
open_bu = ttk.Button(
	output_box,
	text="Open",
	command=open_result
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
tags_cl = wg.CheckList(
	input_box,
	"Tags:",
	180,
	100
)
def perform_search():
	backend.search(
		title_sw.search_term.get(),
		other_info_sw.search_term.get(),
		tags_cl.get_selection()
	)
	results_sl.set_options([str(x) for x in backend.results])
search_bu = ttk.Button(
	input_box,
	text="Search...",
	command=perform_search
)

# library box: frame containing widgets needed to select a library to search
# within. Contains:
# - directory ("Library") search box
lib_box = ttk.Frame(frame)
lib_box_title = ttk.Label(
	lib_box,
	text="Library"
)
current_lib_legend_la = ttk.Label(
    lib_box,
    text="Selected library:"
)
current_lib_var = tk.StringVar()
current_lib_la = ttk.Label(
	lib_box,
	textvariable=current_lib_var
)
def choose_lib(path):
	backend.get_library_data(path)
	tags_cl.set_options(list(backend.lib_tags))
	current_lib_var.set(backend.current_lib)
lib_dialog_bu = ttk.Button(
	lib_box,
	text="Choose Directory...",
	command=lambda: choose_lib(filedialog.askdirectory())
)
lib_sl = wg.SelectList(
	lib_box,
	3
)
lib_sl.on_selection(
	lambda evt: choose_lib(
		backend.libs[lib_sl.get_selection()]
	)
)

# opt_box: the frame containing all the options/config widgets. Contains:
# - "New Library" button
# - "New Book" button
# - "Help" button
opt_box = ttk.Frame(frame)
opt_box_title = ttk.Label(
	opt_box,
	text="Options..."
)
opt_widgets = [
	ttk.Button(
		opt_box,
		text="New Library",
		command=new_lib.run
	),
	ttk.Button(
		opt_box,
		text="New Book",
		command=utils.display_msg
	),
	ttk.Button(
		opt_box,
		text="Help...",
		command=utils.display_msg
	)
]





def populate():
	# decides where all the widgets should go
	root.rowconfigure(0,weight=1)
	root.columnconfigure(0,weight=1)
	utils.put(frame,0,0,sticky="nw")
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
	# +++ THE OPTIONS/CONFIGURATION BOX +++
	utils.put(opt_box,2,0,columnspan=2)
	utils.put(opt_box_title,0,0,columnspan=len(opt_widgets))
	for i in range(len(opt_widgets)):
		utils.put(opt_widgets[i],1,i+1)
	
	# add a little padding around all widgets
	for subframe in frame.winfo_children():
		for child in subframe.winfo_children():
			child.grid_configure(padx=5, pady=5)


def run():
	# technically the entrypoint of the whole application
	backend.setup()
	lib_sl.set_options(backend.libs)
	utils.add_theme(root)
	populate()
	root.mainloop()

if __name__ == "__main__":
	run()
