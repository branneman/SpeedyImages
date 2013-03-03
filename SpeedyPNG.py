# SpeedyPNG
#  Author: Bran van der Meer — http://bran.name/
#  License: Public Domain
#
# TODO
#  - add dependency checks (python version?)
#  - add -q parameter for quiet version
#  - add config for 'tool dir', 'backup & temp filenames'
#  - graphical interface?

from sys import argv
from shutil import copy as fcopy
from os import path, rename, remove, devnull, name as osname
from subprocess import call
from copy import copy as vcopy
from platform import architecture

class Application:

    VERSION = 1.0

    files = []
    tools = []
    toolDir = 'tools/' + osname + '/' + architecture()[0] + '/'

    def __init__(self):
        print('SpeedyPNG - v' + str(self.VERSION))
        if not self.processArguments():
            print(' Usage: ' + __file__ + ' [FILES...]')

    def addTool(self, tool):
        file = self.toolDir + tool.tool + ('.exe' if osname == 'nt' else '')
        if path.exists(file):
            self.tools.append(tool)
        else:
            print(' Dependency not found: ' + file)

    def processArguments(self):
        if len(argv) <= 1:
            return False
        for arg in argv:
            if arg and arg.find(__file__) == -1:
                if path.exists(arg):
                    self.files.append(arg)
                else:
                    print(' File not found: ' + arg)
        return True

    def run(self):

        for file in self.files:

            print('\n  Optimizing: ' + file)

            originalBytes = self.getFilesize(file)
            self.createBackup(file)

            failure = False
            try:
                for tool in self.tools:
                    print('    Running ' + tool.__name__)
                    toolInstance = tool(file)
                    toolInstance.compress()
            except:
                print('  Error while compressing ' + file)
                failure = True

            if not failure:
                self.removeBackup(file)
                self.report(file, originalBytes)

    def createBackup(self, file):
        fcopy(file, file + '~')

    def removeBackup(self, file):
        remove(file + '~')

    def getFilesize(self, file):
        return path.getsize(file)

    def report(self, file, originalBytes):
        optimizedBytes  = self.getFilesize(file)
        savedBytes      = originalBytes - optimizedBytes
        savedPercentage = int(100 - (optimizedBytes / originalBytes) * 100)
        print('  Saved ' + str(savedBytes) + ' bytes (of ' + str(originalBytes) + '), which is ' + str(savedPercentage) + '% savings.')

class Optimizer:

    def __init__(self, file):
        self.file = file

    def before(self):
        pass

    def after(self):
        pass

    def compress(self):
        self.before()
        call(self.getCommand(), stdout = open(devnull, 'w'))
        self.after()

    def getCommand(self):
        return [Application.toolDir + self.tool] + self.commands + [self.file]

class pngcrush(Optimizer):
    tool = 'pngcrush'
    commands = ['-q', '-rem gAMA', '-rem alla', '-rem cHRM', '-rem iCCP', '-rem sRGB', '-rem time']
    def getCommand(self):
        return [Application.toolDir + self.tool] + self.commands + [self.file, self.file + '~.tmp']
    def after(self):
        remove(self.file)
        rename(self.file + '~.tmp', self.file)

class OptiPNG(Optimizer):
    tool = 'optipng'
    commands = ['-force', '-q', '-o7']

class AdvPNG(Optimizer):
    tool = 'advpng'
    commands = ['-qz4']

class PNGOUT(Optimizer):
    tool = 'pngout'
    commands = ['-q']

class DeflOpt(Optimizer):
    tool = 'DeflOpt'
    commands = ['/ds']

# Create application instance
app = Application()

# Register tools
app.addTool(pngcrush)
app.addTool(OptiPNG)
app.addTool(AdvPNG)
app.addTool(PNGOUT)
app.addTool(DeflOpt)

# Run!
app.run()
