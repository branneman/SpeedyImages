# SpeedyPNG

Author: Bran van der Meer — [http://bran.name/](http://bran.name/)  
License: Public Domain

SpeedyPNG is a command line PNG optimization tool written in Python. It optimizes by running the PNG through pngcrush, OptiPNG, AdvPNG, PNGOUT and DeflOpt.

## [Download](https://github.com/branneman/SpeedyPNG/archive/master.zip)

## Requirements
- Python 3.3

It is currently only tested on Windows 8, but it _should_ work on posix systems as long as the binaries are available in the tools directory.

## Usage:
	speedypng [options] [files...]

	Options:
	 -q  Quiet mode, will only output on error.
	 -s  Silent mode, will never output.

## Roadmap
 - Create useful exitcode, and make runtests.py watch for it.
 - Add tool binaries for posix, and test them on linux and osx.
 - Rename project to 'SpeedyImages'
   - Add jpeg support with jpegoptim, jpegrescan, jpegtran.
   - Add svg support with svgo.
 - Add 'overall report' when finished multiple files.
 - Add support for iterating a directory recursively.
 - Add a GUI.
