# SpeedyPNG

Author: Bran van der Meer — [http://bran.name/](http://bran.name/)  
License: Public Domain

SpeedyPNG is a command line PNG optimization tool written in Python. It optimizes by running the PNG through pngcrush, OptiPNG, AdvPNG, PNGOUT and DeflOpt.

## [Download](https://github.com/branneman/SpeedyPNG/archive/master.zip)
You'll need [*Python 3.3*](http://www.python.org/download/) installed.

## Usage:
	speedypng [options] [files...]

	Options:
	 -q  Quiet mode, will only output on error.
	 -s  Silent mode, will never output.

## Roadmap
 - Create useful exitcodes.
 - Add tool binaries for posix systems.
 - Rename project to 'SpeedyImages':
   - Add jpeg support with jpegoptim, jpegrescan, jpegtran.
   - Add svg support with svgo.
 - Output 'overall report' when optimizing multiple files.
 - Add support for iterating a directory recursively.
 - Add a GUI.
