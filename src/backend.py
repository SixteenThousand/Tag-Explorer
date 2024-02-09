# module for search functions; the main module for the back-end of the app

import os
import re
from icecream import ic  # debug


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
	# data about the currently selected library
	global lib_tags; lib_tags = set()
	global lib_books; lib_books = set()
	
	# the name of database files in directories tracked by TagEx
	global DB_NAME; DB_NAME = ".tgx"
	# the directory containing all TagEx-wide data & configuration
	global DATA_DIR; DATA_DIR = "tag-explorer"
	# the name of the file containing the list of all directories currently
		# tracked by TagEx
	global LIBS_LIST_FILE; LIBS_LIST_FILE = "libraries"
	global SEPARATOR; SEPARATOR = " ;; "
	
	# list of search results
	global results; results = []
	
	# create config/data directory if it does not exist already
	if os.name == "nt":
		DATA_DIR = os.path.join(os.environ["home"],"AppData\\Local",DATA_DIR)
		LIBS_LIST_FILE = os.path.join(DATA_DIR,LIBS_LIST_FILE)
	if os.path.exists(DATA_DIR):
		os.makedirs(DATA_DIR,exist_ok=True)
	
	# getting a list of direcories currently tracked by TagEx
	global libs
	with open(LIBS_LIST_FILE,"r",encoding="utf-8") as fp:
		libs = fp.read().split("\n")



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
		os.startfile(os.path.join(path,self.path))


def get_library_data(lib_path):
	lib_tags.clear()
	with open(os.path.join(lib_path,DB_NAME),"r",encoding="utf-8") as fp:
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
			set(tags) <= book.tags and
			title_match(title,book.title) and
			other_info_match(other_info,book.other_info)
		):
			results.append(book)



def get_shelves(path):
	"""Returns a list of all subdirectories (of any depth) of {path}."""
	results = []
	for subdir,x,y in os.walk(path):
		results.append(subdir)
	return results


DEFAULT_INFO_RGX = "(\\.?[^\\.]+)(\\.?.*)"

def create_library(path,name,use_auto_tags,shelves,info_rgx=DEFAULT_INFO_RGX):
	"""
		Writes a .tgx file for a new library.
		path: path-like; the absolute path to the library
		name: str; the name Tag Explorer wil use to refer to the new library
		use_auto_tags: bool; if True, generate tags for each book based on
		ancestor directory names
		shelves: list(str); list of the subdirectories of the library that
		should not be treated as books
		info_rgx: str; a string representing a python regular expression with
		at least TWO capture groups. The first group is the title of the book,
		the second any other information, such as author. By default title is
		whole file/directory name, minus any file extensions
	"""
	fp = open(f"{DATA_DIR}/{name}.tgx","w",encoding="utf-8")
	print(path,file=fp)
	os.chdir(path)
	for shelf in shelves:
		tags = []
		if use_auto_tags:
			tags.extend(shelf.split("/"))
		for thing in os.scandir(shelf):
			if thing.path in shelves:
				continue
			info_match = re.match(info_rgx,thing.name)
			print(
				thing.path,
				info_match[1],
				info_match[2],
				",".join(tags),
				sep=SEPARATOR,
				file=fp
			)
	fp.close()
