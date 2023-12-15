# module for search functions

tags = set()
books = dict()

def get_book(line):
	pass
def parse_tgx(path):
	with open(path,"r",encoding="utf-8") as fp:
		fp.readline()
		tags_line = fp.readline()
		for line in fp:
			get_book(line)
