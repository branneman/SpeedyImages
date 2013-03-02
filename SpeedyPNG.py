# SpeedyPNG
#  Author: Bran van der Meer — http://bran.name/
#  License: Public Domain
#
# TODO
#  - add pngrewrite & pngout
#  - write report when done (% file size reduction)
#  - add python version check
#  - add dependency check (see if all the tools are there)
#  - add -q parameter for quiet version
#  - make backup & temp filenames configurable
#  - create windows binary, if possible as single file distribution
#  - graphical interface?

from sys import argv
from shutil import copy as fcopy
from os import rename, remove, devnull
from subprocess import call
from copy import copy as vcopy

class Application:

    VERSION = 1.0

    files = []
    tools = []

    def __init__(self):

        print('SpeedyPNG - v' + str(self.VERSION))

        if len(argv) <= 1:
            return print(' Usage: ' + __file__ + ' [FILES...]')

        for arg in argv:
            if arg and arg.find(__file__) == -1:
                self.files.append(arg)

    def run(self):

        for file in self.files:

            print('  Optimizing ' + file)

            self.createBackup(file)

            failure = False
            try:
                for tool in self.tools:
                    print('    Running ' + tool.__name__)
                    toolInstance = tool(file)
                    toolInstance.compress()

            except:
                print('-Error while compressing ' + file)
                failure = True

            if not failure:
                self.removeBackup(file)

    def createBackup(self, file):
        fcopy(file, file + '~')

    def removeBackup(self, file):
        remove(file + '~')

class Optimizer:

    def __init__(self, file):
        self.file = file

    def before(self):
        pass

    def compress(self):

        self.before()

        for command in self.commands:

            cmd = vcopy(command)

            cmd[0] = 'tools/' + cmd[0]
            for key, part in enumerate(cmd):
                if part == 0:
                    cmd[key] = self.file
                elif part == 1:
                    cmd[key] = self.file + '~.tmp'

            retcode = call(cmd, stdout = open(devnull, 'w'))

        self.after()

    def after(self):
        pass

class pngrewrite(Optimizer):
    commands = []

class pngcrush(Optimizer):
    commands = [['pngcrush.exe', '-q', '-rem', 'gAMA', '-rem', 'alla', '-rem', 'cHRM', '-rem', 'iCCP', '-rem', 'sRGB', '-rem', 'time', 0, 1]]
    def after(self):
        remove(self.file)
        rename(self.file + '~.tmp', self.file)

class OptiPNG(Optimizer):
    commands = [['optipng.exe', '-force', '-q', '-o7', 0]]

class AdvPNG(Optimizer):
    commands = [['advpng.exe', '-qz4', 0]]

class PNGOUT(Optimizer):
    commands = []

class DeflOpt(Optimizer):
    commands = [['DeflOpt.exe', '/ds', 0]]

# Create application instance
app = Application()

# Register tools
#app.tools.append(pngrewrite)
app.tools.append(pngcrush)
app.tools.append(OptiPNG)
app.tools.append(AdvPNG)
#app.tools.append(PNGOUT)
app.tools.append(DeflOpt)

# Run!
app.run()
