import tkinter as tk
import tkinter.ttk as ttk
import utils
import backend
import widgets as wg


assets = "../assets/"

root = tk.Tk()
root.title("New Library")
frame = ttk.Frame(root)

dir_se = wg.SearchEntry(frame,"Choose a directory")

auto_tags_la = ttk.Label(frame,text="Automatically generate tags?")
auto_tags_var = tk.IntVar()  # will be 1 if button is ticked, 0 otheriwse
auto_tags_cb = ttk.Checkbutton(frame,variable=auto_tags_var)

auto_tags_h = wg.HelpButton(frame,assets+"auto-tags-help")

shelves_cl = wg.CheckList(frame,"Shelves:",200,150)

shelves_h = wg.HelpButton(frame,assets+"shelves-help")

info_rgx_se = wg.SearchEntry(
	frame,
	"Information regex\n(leave blank if you do not want to use this)",
)

info_rgx_h = wg.HelpButton(frame,assets+"info-regex-help")

create_bu = ttk.Button(frame,text="Create New Library")



def populate():
	utils.put(frame,0,0)
	dir_se.position(0,0)
	utils.put(auto_tags_la,1,0,sticky="ne")
	utils.put(auto_tags_cb,1,1,sticky="nw")
	auto_tags_h.put(1,2)
	shelves_cl.position(2,0)
	shelves_h.put(2,2)
	info_rgx_se.position(3,0)
	info_rgx_h.put(3,2)
	utils.put(create_bu,4,0,columnspan=3)
	
	for child in frame.winfo_children():
		child.grid_configure(padx=7,pady=7)

def run():
	utils.add_theme(root)
	populate()
	root.mainloop()


if __name__ == "__main__":
	run()
