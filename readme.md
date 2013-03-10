# SpeedyPNG

Author: Bran van der Meer — [http://bran.name/](http://bran.name/)  
License: Public Domain. The tool (binaries) have their own licenses.

SpeedyPNG is a command line PNG optimization tool written in Python. It optimizes by running the PNG through pngcrush, OptiPNG, AdvPNG, PNGOUT and DeflOpt.

## [Download](https://github.com/branneman/SpeedyPNG/archive/master.zip)
You'll need [*Python 3.3*](http://www.python.org/download/) installed.

## Usage:
	./speedypng [options] [files...]

Options:  
-q Quiet mode, will only output on error.  
-s Silent mode, will never output.

The application will return an exit code of 0 on success, 1 on error.

## Roadmap
 - Refactor for maximum reuse of code.
 - Add support for iterating a directory recursively.
 - Refactor tests to python native unittests
 - Add tool binaries for posix systems.
 - Rename project to 'SpeedyImages':
   - Add jpeg support with jpegoptim, jpegrescan, jpegtran.
   - Add svg support with svgo.
 - Add a GUI (Tk? GTK? Qt? wx?).
