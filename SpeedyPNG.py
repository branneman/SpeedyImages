# SpeedyPNG
#  Author: Bran van der Meer — http://bran.name/
#  License: Public Domain
#
# TODO
#  - write report when done (% savings and all)
#  - add python version check
#  - add dependency check (see if all the tools are there)
#  - add -q parameter for quiet version
#  - create windows binary, if possible as single file distribution
#  - graphical interface

VERSION = 0.1

from sys import argv
from shutil import copy
from os import remove, devnull
from subprocess import call

def compress(file):

    print(' Compressing: ' + file)

    # Define the various commands
    commands = [
        {'name': 'OptiPNG',  'commands': ['optipng.exe', '-force', '-q', '-o7']},
        {'name': 'AdvPNG',   'commands': ['advpng.exe', '-qz4']},
        #{'name': 'pngcrush', 'commands': ['pngcrush.exe', '-rem', 'gAMA', '-rem', 'alla', '-rem', 'cHRM', '-rem', 'iCCP', '-rem', 'sRGB', '-rem', 'time']},
        {'name': 'DeflOpt',  'commands': ['DeflOpt.exe', '/ds']}
    ]

    # Create a backup file
    copy(file, file + '~')

    # Run compress commands
    failure = False
    try:
        for cmd in commands:
            print('  Running ' + cmd['name'])
            command = cmd['commands']
            command.append(file);
            command[0] = '.\\tools\\' + command[0]
            retcode = call(command, stdout = open(devnull, 'w'))
    except:
        failure = True

    # On success, remove backup file
    if not failure:
        remove(file + '~')

# Welcome message
print('SpeedyPNG - v' + str(VERSION))

# Check for passed arguments
if len(argv) == 1:
    print('Usage: SpeedyPNG.py [FILES...]')
else:
    for arg in argv:
        if arg and arg.find(__file__) == -1:
            compress(arg)
