# module for search functions; the main module for the back-end of the app

import os



def setup():
	"""
		Makes all of the things Tag Explorer needs to run on the back end.
		Specifically:
			- creating global variables to store search results/other runtime
			data
			- creating global "constants" that are relevant to the storage of
			tag explorer data on the user's machine, and create a directory
			for storing that data
	"""
	# data about the selected library
	global libs
	libs = dict()
	global lib_tags
	lib_tags = set()
	global lib_books
	lib_books = dict()
	
	# the location of all data used by tag explorer
	global EXT
	EXT = ".tgx"
	global DATA_DIR
	DATA_DIR = "tag-explorer"
	
	# create config/data directory if it does not exist already
	if os.name == "nt":
		DATA_DIR = os.path.join(os.environ["home"],"AppData\\Local",DATA_DIR)
	else:
		DATA_DIR = os.path.join("~/.config",DATA_DIR)
	if os.path.exists(DATA_DIR):
		os.makedirs(DATA_DIR,exist_ok=True)
	
	# getting the names & locations of the libraries
	for thing in os.scandir(DATA_DIR):
		if not thing.name.endswith(EXT):
			continue
		fp = open(thing.path,"r",encoding="utf-8")
		libs[thing.name.split(".")[0]] = fp.readline()
		fp.close()
		


class Book():
	def __init__(self,path,title,other_info,tags):
		self.path = path
		self.title = title
		self.other_info = other_info
		self.tags = tags

def get_book(line):
	data = line.split(" ;; ")
	return Book(
		data[0],
		data[1],
		data[2],
		set(data[3].split(","))
	)

def get_library_data(lib_name):
	pass
