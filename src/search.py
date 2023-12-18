# module for search functions; the main module for the back-end of the app

import os



# list of libraries got from LIBRARIES.
# each item is a tuple of (path of library, ID of library)

def setup():
	"""
		creates the relevant files for storing tags & locations between sessions
		the directory containing all tag-explorer data. includes:
			- a text file that lists the absolute paths to all directories currently
			handled by tag explorer (the "libraries"), along with a unique ID for each
			- a set of files, one for each library, named something like
				{library ID}.tgx
			which contain the known tags and locations of books
		***NOTE*** despite the capitalisation, this variable will be changed ONCE to
		account for operating system differences
	"""
	# data about the current library
	global libs = []
	global lib_tags = set()
	global lib_books = dict()
	# the location of all data used by tag explorer
	global LIBRARIES = "libraries"
	global EXT = ".tgx"
	
	if os.name == "nt":
		DATA_DIR = os.path.join(os.environ["home"],"AppData\\Local",DATA_DIR)
	else:
		DATA_DIR = os.path.join("~/.config",DATA_DIR)
	if os.path.exists(DATA_DIR):
		return
	os.makedirs(DATA_DIR,exist_ok=True)
	with open(os.path.join(DATA_DIR,LIBRARIES),"w",encoding="utf-8") as fp:
		fp.write("# List of Libraries")



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


def parse_tgx(path):
	with open(path,"r",encoding="utf-8") as fp:
		fp.readline()
		for line in fp:
			b = get_book(line)
			lib_books[b.path] = b
			lib_tags = lib_tags | b.tags

def get_libs():
	# returns a list of all the directories that have a .tgx file (aka
	# "libraries")
	if os.path.exists(LIBRARIES):
		fp = open(lib-LIBRARIES,"r",encoding="utf-8")
		for line in fp:
			libs.append(line)
