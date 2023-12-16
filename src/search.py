# module for search functions
lib_list_loc = "./.tgxlibs"

libs = []
lib_tags = set()
lib_books = dict()

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
	if os.path.exists(lib_list_loc):
		fp = open(lib-lib_list_loc,"r",encoding="utf-8")
		for line in fp:
			libs.append(line)
