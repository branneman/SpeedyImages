# SpeedyImages

Author: Bran van der Meer — [http://bran.name/](http://bran.name/)  
License: Public Domain. The tool (binaries) have their own licenses.

SpeedyImages is a command line image optimization tool written in Python. It optimizes by running the image through several tools. For example when optimizing a PNG, the tools used are pngcrush, OptiPNG, AdvPNG, PNGOUT and DeflOpt.

## [Download](https://github.com/branneman/SpeedyImages/archive/master.zip)
You'll need [*Python 3.3*](http://www.python.org/download/) installed.

## Usage:
	./speedyimages [options] [files...]

Options:  
`-v` Show version, but will show nothing when combined with -s).  
`-q` Quiet mode, will only output on error.  
`-s` Silent mode, will never output.

The CLI application will return an exit code of 0 on success, 1 on error.