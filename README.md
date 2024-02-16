### Note
This project is in an unstable unusable state. When it is usable, the relevant 
commit will be labelled "v0.0", at which point there will be full installation 
instructions below.

For now, treat this document as more of a road map to version 0.0 than a 
description of how Tag Explorer works now.

---


# Tag Explorer
Tag Explorer is a desktop application that allows its users to add tags to 
files & folders, a bit like how gmail works (assuming you don't just treat 
gmail tags like folders!).

---


## Requirements
Tag Explorer currently is only tested on Windows 10 with python 3.12. It will 
likely work on any windows system with python 3.

---


<!-- ## Installation -->
<!-- ``` -->
<!-- 	python -m zipapp -o "./tagx.pyz" -m "main_app:run" -->
<!-- ``` -->
<!---->
<!-- --- -->


## Usage
There are three main tasks you would want to do with Tag Explorer:
	- [Search for a "Book"](#search-for-a-"book"), that is, find a tagged
		file/directory in this "library";
	- [Create a new "Library"](#creating-a-new-"library"), that is, make Tag
		Explorer aware of a new directory so you can add tags to it;
	- [Add a new "Book"](#add-a-new-"book"), that is, add tags to a 
	  file/directory not currently tracked by Tag Explorer.
More options may be added in future, but this is all you will be able to do 
once the project has reached v0.0. See [Possible Future 
Features](#possible-future-features).

Before that though, we should define some terms:
- A *Library* is a directory with a `.tgx` file in it. The `.tgx` file is while 
  the tags data is stored, allowing Tag Explorer to search through this 
  directory.
- A *Book* is a file *OR* a directory within a Library. These are the things 
  that Tag Explorer helps you to find.
- A *Shelf* is a directory within a Library that only contains Books and other 
  Shelves. These are not part of the `.tgx` file at all, but are instead just  
  used when creating a Library for the first time, so Tag Explorer knows what 
  is a Book and what isn't without you having to manually tell it in every 
  case.

### Search for a "Book"
1. Select a Library you want to search in. You can do this either by choosing 
   from the list of Libraries Tag Explorer knows about already, or via a file 
   explorer dialog.
   You should see the absolute path of the Library you chose just below the 
   library list, and see that the box next to "Tags:" is now populated.
1. Tick all tags you want search results to have; Tag Explorer will only show 
   you books that have *all* of the selected tags. You can also search for the 
   Book's "title" or "other information". These things are just data extracted 
   from the file/directory names. For these fields, Tag Explorer will match any 
   book whose tile or other information contains your search query, ignoring 
   case.
1. Click Search.
1. See if what you were looking for is in the results list. If it is, click on 
   it and click the "Open" button to, well, open it.
	<!-- ![Labelled screenshot of main window]() -->


### Creating a new "Library"
1. Click the "New Library" button. This will open a new window:
	<!-- ![Screenshot of "New Library" Window]() -->
1. Choose whether you want Tag Explorer to automatically generate tags. If you 
   tick this box, Tag Explorer will add the existing directory names in the 
   path of each Book as tags of that Book.
1. Choose Shelves. These are the subdirectories of the Library that tag 
   Explorer will look for Books in. Note that each Shelf should *only* contain 
   Books and other Shelves.
1. Assign an information regex. This is how tag explorer will get the title and 
   other information from each Book. By default, the titles will be the 
   file/directory name of the Book, minus any file extensions, and the other 
   information will be any file extensions. For more information, click the 
   help button on the right.
1. Click "Create New Library".

There should now be a file called ".tgx" in the directory you chose, and in this
file you should see something like the following:
```
	./TheColourOfMagic_TerryPratchett.pdf ;; TheColourOfMagic ;; TerryPratchett ;; fantasy,sci-fi,british
	./Neverwhere_NeilGaiman.txt ;; Neverwhere ;; NeilGaiman ;; fantasy,british
	./Maths-Books/Elements_Euclid.dvi ;; Elements ;; Euclid ;; maths,geometry
	./Maths-Books/The-Bumper-Book-Of-Differential-Equations/ ;; The-Bumper-Book-Of-Differential-Equations ;;  ;; maths,analysis,ODEs,differential equations
	./Maths-Books/Category-Theory/TheJoyOfCats.pdf ;; TheJoyOfCats ;;  ;; category theory,algebra,maths
	./Maths-Books/Category-Theory/CategoryTheoryForProgrammers_BartoszMileski.pdf ;; CategoryTheoryForProgrammers ;; BartoszMilewski ;; maths,category theory, programming, haskell
```
You can just manually add tags to books in the database now - indeed, that is
why Tag Explorer uses a text file rather than a proper database - or you can
add click on "New Book" and overwrite the existing data on some book with new
data.


### Add a new "Book"
1. Click the "New book" button at the bottom. This will open  a new window:
	<!-- ![Screenshot of "New Book" window]() -->
1. Click "Select file/directory". This will open a file explorer dialog from 
   which you can choose a new file or directory for Tag Explorer to manage. 
   Your choice will be shown below the button.
1. Enter a title & other information, if you wish. If left empty, they will 
   default to the filename (minus any extension) or "---" if the selected item 
   is a directory.
1. Add tags. These can existing tags in the Library, selected via checklist, or 
   new ones, which should be comma separated and without spaces (unless a space 
   is part of the tag).
1. Click "Finish".


## Features needed for v0.0
- [x] ability to select a library & search
- [x] ability to open a Book
- [ ] ability to create a new library
- [ ] ability to create a new book
- [ ] Working build script

## Possible Future Features
These are things that could be in a future v0.1:
- [ ] Command Line Interface
- [ ] Ability to edit the data stored about a particular book
- [ ] Ability to search for all Books which match *any* tags selected, rather 
  than all
