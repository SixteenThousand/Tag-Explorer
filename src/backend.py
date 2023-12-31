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
	libs = []
	global lib_tags
	lib_tags = set()
	global lib_books
	lib_books = set()
	global lib_path
	
	# the location of all data used by tag explorer
	global EXT
	EXT = ".tgx"
	global DATA_DIR
	DATA_DIR = "tag-explorer"
	global SEPARATOR
	SEPARATOR = " ;; "
	
	# list of search results
	global results
	results = []
	
	# create config/data directory if it does not exist already
	if os.name == "nt":
		DATA_DIR = os.path.join(os.environ["home"],"AppData\\Local",DATA_DIR)
	else:
		DATA_DIR = os.path.join("~/.config",DATA_DIR)
	if os.path.exists(DATA_DIR):
		os.makedirs(DATA_DIR,exist_ok=True)
	
	# getting the names of the libraries
	for thing in os.scandir(DATA_DIR):
		if not thing.name.endswith(EXT):
			continue
		libs.append(thing.name.split(".")[0])



class Book():
	def __init__(self,line):
		data = line.split(SEPARATOR)
		self.path = data[0]
		self.title = Book.parse_title(data[1])
		self.other_info = data[2]
		self.tags = set(data[3].split(","))
	
	@staticmethod
	def parse_title(title_str):
		return title_str
	
	def __str__(self):
		return f"{self.title}, {self.other_info}"
	
	def __repr__(self):
		return "\n".join([
			f"Title: {self.title}",
			f"Other Information: {self.other_info}",
			f"Location: {self.path}",
			f"Tags: {self.tags}"
		])
	
	def sys_open(self,path):
		print(os.path.join(path,self.path))  # debug
		os.startfile(os.path.join(path,self.path))


def get_library_data(lib_name):
	lib_tags.clear()
	global lib_path
	with open(os.path.join(DATA_DIR,lib_name+EXT),"r",encoding="utf-8") as fp:
		lib_path = fp.readline().strip()
		for line in fp:
			b = Book(line.strip())
			lib_books.add(b)
			lib_tags.update(b.tags)

def title_match(search_term,item):
	return search_term.lower() in item.lower()

def other_info_match(search_term,item):
	return search_term.lower() in item.lower()


def search(title,other_info,tags):
	results.clear()
	for book in lib_books:
		if (
				set(tags) < book.tags and
				title_match(title,book.title) and
				other_info_match(other_info,book.other_info)
			):
			results.append(book)
