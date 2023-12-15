import sys
import tkinter as tk
import tkinter.ttk as ttk

class SearchEntry():
	def __init__(self,frame,name):
		self.name = ttk.Label(frame,text=f"{name}: ")
		self.search_term = tk.StringVar()
		self.input_wg = ttk.Entry(
			frame,
			width=50,
			textvariable=self.search_term
		)
	
	def position(self,r,c):
		self.name.grid(row=r,column=c,sticky="e")
		self.input_wg.grid(row=r,column=c+1,sticky="w")

class SearchList():
	def __init__(self,frame,name,height):
		self.name = ttk.Label(frame,text=f"{name}: ")
		self.selected_item = tk.StringVar()
		self.input_wg = tk.Listbox(
			frame,
			width=50,
			height=height,
			listvariable=self.selected_item
		)
	
	def position(self,r,c):
		self.name.grid(row=r,column=c,sticky="ne")
		self.input_wg.grid(row=r,column=c+1,sticky="w")
