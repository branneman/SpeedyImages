# SpeedyPNG

Author: Bran van der Meer — [http://bran.name/](http://bran.name/)  
License: Public Domain

SpeedyPNG is a command line PNG optimization tool written in Python 3.3 for Windows. It optimizes by running the PNG through pngcrush, OptiPNG, AdvPNG, PNGOUT and DeflOpt.

## Requirements
- Python 3.3

It is currently only tested on Windows 8, but it _should_ work on other posix systems as long as the binaries are available in the tools directory.

## Usage:

	python SpeedyPNG.py [FILES...]

## [Download](https://github.com/branneman/SpeedyPNG/archive/master.zip)

## Roadmap
 - Add tool binaries for posix, and test them on linux and osx.
 - Rename project to 'SpeedyImages' and add jpeg support with jpegoptim, jpegrescan, jpegtran.
 - Create os-specific application binaries, so the 'python app.py' syntax isn't necessary anymore.
 - Add -q parameter for quiet version.
 - Add a GUI.