# module for any mocks used in testing
import tkinter as tk
import tkinter.ttk as ttk

def button_handler():
	root = tk.Tk()
	root.title("+++TEST+++")
	root.rowconfigure(0,weight=1)
	root.columnconfigure(0,weight=1)
	main_frame = ttk.Frame(root)
	main_frame.grid(row=0,column=0)
	msg = ttk.Label(main_frame,text="This is a mock window, here as a default handler for buttons in the main app.\nPlease exit now.")
	msg.grid(row=0,column=0)
	root.mainloop()

def display_msg(msg):
	root = tk.Tk()
	root.title("---")
	ttk.Label(text=msg).grid(row=0,column=0)
	root.mainloop()
