import logging
from os import path
from sys import argv

from queue.item import QueueItem
from optimizer.png import png

class App:

    name = 'SpeedyImages'
    VERSION = 1.1

    options = {
        '-v': False,
        '-q': False,
        '-s': False
    }

    optimizers = [png()]
    queue = []

    def setupLogging(self):

        lvl = 'INFO'
        if self.options['-q']:
            lvl = 'WARNING'
        if self.options['-s']:
            lvl = 'ERROR'

        logging.basicConfig(
            level  = lvl,
            format = '%(message)s'
        )

    def processOptionArguments(self):
        for arg in argv:
            if self.isOption(arg):
                self.options[arg] = True

    def processFileArguments(self):
        for arg in argv:
            if self.isFile(arg) and self.isSupportedFile(arg):
                self.queue.append(QueueItem(arg))
            elif self.isDirectory(arg):
                for file in self.getFilesInDirectory():
                    if self.isSupportedFile(arg):
                        self.queue.append(QueueItem(file))

    def isOption(self, arg):
        return arg in self.options.keys()

    def isFile(self, arg):
        return path.exists(arg) and path.isfile(arg)

    def isDirectory(self, arg):
        return path.exists(arg) and path.isdir(arg)

    def isSupportedFile(self, arg):
        return path.splitext(arg)[1] in [cl.ext for cl in self.optimizers]

    # todo implement
    def getFilesInDirectory(self, arg):
        return []

    def run(self, file):
        for queueitem in self.queue:
            logging.info('Optimize()\'ing ' + queueitem.filename)
