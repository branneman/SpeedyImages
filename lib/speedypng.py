# SpeedyPNG
#
#  Author:  Bran van der Meer — http://bran.name/
#  License: Public Domain
#

from sys import argv, exit
from shutil import copy as fcopy
from os import path, rename, remove, devnull, name as osname
from subprocess import call
from copy import copy as vcopy
from platform import architecture

class Application:

    VERSION = 1.0

    failure = 0

    files = []
    tools = []
    toolDir = 'tools/' + osname + '/' + architecture()[0] + '/'

    def __init__(self):
        self.outputMessage('SpeedyPNG - v' + str(self.VERSION))
        if not self.processArguments():
            self.outputMessage('\n Usage: ./speedypng [options] [files...]\n')
            self.outputMessage(' Options:')
            self.outputMessage('  -q  Quiet mode, will only output on error.')
            self.outputMessage('  -s  Silent mode, will never output.\n')

    def outputMessage(self, message):
        if not '-q' in argv and not '-s' in argv:
            print(message)

    def outputError(self, message):
        self.failure = 1
        if not '-s' in argv:
            print(message)

    def addTool(self, tool):
        file = self.toolDir + tool.tool + ('.exe' if osname == 'nt' else '')
        if path.exists(file):
            self.tools.append(tool)
        else:
            self.outputError(' Dependency not found: ' + file)

    def processArguments(self):

        filesSpecified = False

        for arg in argv:
            if not self.isParameterOption(arg) and (arg.find(__file__) == -1):
                filesSpecified = True
                if path.exists(arg):
                    self.files.append(arg)
                else:
                    self.outputError(' File not found: ' + arg)

        if len(argv) <= 1 or (not len(self.files) and not filesSpecified):
            self.outputError('No files specified.')
            return False

        return True

    def isParameterOption(self, param):
        return param in ['-q', '-s']

    def run(self):

        totalOriginalSize = self.getTotalFilesize()

        for file in self.files:

            self.outputMessage('\n  Optimizing: ' + file)

            originalSize = self.getFilesize(file)
            self.createBackup(file)

            try:
                for tool in self.tools:
                    self.outputMessage('    Running ' + tool.__name__)
                    tool(file).compress()
            except:
                self.outputError('  Error while compressing ' + file)
            else:
                self.removeBackup(file)
                self.report(file, originalSize)

        if len(self.files) > 1:
            self.reportTotal(totalOriginalSize)

        return self.failure

    def createBackup(self, file):
        fcopy(file, file + '~')

    def removeBackup(self, file):
        remove(file + '~')

    def getFilesize(self, file):
        return path.getsize(file)

    def getTotalFilesize(self):
        return sum([self.getFilesize(file) for file in self.files])

    def report(self, file, originalSize):
        optimizedSize = self.getFilesize(file)
        percentage    = int(100 - (optimizedSize / originalSize) * 100)
        message       = '  Reduced size with %s%%: from %s to %s bytes.'
        self.outputMessage(message % (percentage, originalSize, optimizedSize))

    def reportTotal(self, totalOriginalSize):
        optimizedSize = self.getTotalFilesize()
        savedBytes    = totalOriginalSize - optimizedSize
        percentage    = int(100 - (optimizedSize / totalOriginalSize) * 100)
        message       = '\n  Saved a total of %s%%, or %s bytes in %s files. '
        self.outputMessage(message % (percentage, savedBytes, len(self.files)))

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
exit(app.run())
