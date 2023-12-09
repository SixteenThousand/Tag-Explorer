# Tag Explorer
Tag Explorer is a desktop application that allows its users to add tags to files
& folders, a bit like how gmail works (assuming you don't just treat gmail tags
like folders!).

---


## Installation

Firstly, this project is mostly for my own personal use, so you would probably
be better off just finding another project that does something similar; if I
find any myself, I'll post links here. If you still want to use this, you will
need:
	- python version 3.11 or greater.
You can install Tag Explorer either by downloading one of the .pyz releases, or
you can build it yourself by cloning the repo and running
```
	python -m zipapp -o "./tagx.pyz" -m "app:run"
```
---


## Usage

There are three main tasks you would want to do with Tag Explorer:
	- [Create a new "Library"](#creating-a-new-"library"), that is, make Tag
	Explorer aware of a new directory so you can add tags to it
	- [Edit an existing library](#edit-an-existing-library)
	- [Search for a "book"](#search-for-a-"book"), that is, find a tagged
	file/directory in this "library"

### Creating a new "Library"
Click the "New Library" button. This will open a new window:
	![Screenshot of "New Library" Window]()
Enter the path of the directory you want to add tags to, fill in the tags you
want to use in this "Library" in the Tags text box as a comma-separated list,
(you will be able to add more tags later if necessary) then finally click 
"Create".

There should now be a file called ".tgx" in the directory you chose, and in this
file you should see something like the following:
```
	info_rgx  ;;  (.*)_(.*)\..*
	./TheColourOfMagic_TerryPratchett.pdf ;; TheColourOfMagic ;; TerryPratchett ;; fantasy,sci-fi,british
	./Neverwhere_NeilGaiman.txt ;; Neverwhere ;; NeilGaiman ;; fantasy,british
	./Maths-Books/Elements_Euclid.dvi ;; Elements ;; Euclid ;; maths,geometry
	./Maths-Books/The-Bumper-Book-Of-Differential-Equations/ ;; The-Bumper-Book-Of-Differential-Equations ;;  ;; maths,analysis,ODEs,differential equations
	./Maths-Books/Category-Theory/TheJoyOfCats.pdf ;; TheJoyOfCats ;;  ;; category theory,algebra,maths
	./Maths-Books/Category-Theory/CategoryTheoryForProgrammers_BartoszMileski.pdf ;; CategroyTheoryForProgrammers ;; BartoszMilewski ;; maths,category theory, programming, haskell
```

### Edit an existing library
### Search for a "book"
---


## Configuration
