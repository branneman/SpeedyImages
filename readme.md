# SpeedyImages

Author: Bran van der Meer — [http://bran.name/](http://bran.name/)  
License: Public Domain. The tool (binaries) have their own licenses.

SpeedyImages is a command line image optimization tool written in Python. It optimizes by running the image through several tools. For example when optimizing a PNG, the tools used are pngcrush, OptiPNG, AdvPNG, PNGOUT and DeflOpt.

## [Download](https://github.com/branneman/SpeedyImages/archive/master.zip)
You'll need [*Python 3.3*](http://www.python.org/download/) installed.

## Usage:
	./speedyimages [options] [files...]

Options:  
-v Show version, but will show nothing when combined with -s).  
-q Quiet mode, will only output on error.  
-s Silent mode, will never output.

The application will return an exit code of 0 on success, 1 on error.

## Roadmap
 - Add support for iterating a directory recursively.
 - Refactor tests to python native unittests
 - Refactor to a coding standard.
 - Add tool binaries for posix systems.
 - Add jpeg support with jpegoptim, jpegrescan, jpegtran.
 - Add svg support with svgo.
 - Add a GUI (Tk? GTK? Qt? wx?).
