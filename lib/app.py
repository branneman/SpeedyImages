import logging
from os import path
from sys import argv

from queue.item import QueueItem
from optimizer.png import png
from fileutil import fileutil
from report import report

class App:

    name = 'SpeedyImages'
    VERSION = 1.1

    options = {
        '-v': False,
        '-q': False,
        '-s': False
    }

    dependenciesNotFound = []
    optimizers = [png()]
    queue = []

    def bootstrap(self):
        self.processOptionArguments()
        self.setupLogging()
        self.processFileArguments()
        self.checkDependencies()

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

            if fileutil.isFile(arg) and self.isSupportedFile(arg):
                self.queue.append(QueueItem(arg))

            elif fileutil.isDirectory(arg):
                for file in fileutil.getFilesInDirectory():
                    if fileutil.isFile(file) and self.isSupportedFile(file):
                        self.queue.append(QueueItem(file))

    def isOption(self, arg):
        return arg in self.options.keys()

    def isSupportedFile(self, arg):
        return path.splitext(arg)[1] in [cl.ext for cl in self.optimizers]

    def checkDependencies(self):
        for optimizer in self.optimizers:
            notfound = optimizer.checkDependencies()
            if notfound:
                self.dependenciesNotFound += notfound

    def getOptimizer(self, item):
        for optimizer in self.optimizers:
            if optimizer.ext == item.filetype:
                return optimizer
        return False

    def run(self):

        filenames = [q.filename for q in self.queue]
        results = report(filenames)

        for item in self.queue:

            logging.info('\n  Optimizing: ' + str(item))

            item.createBackup()

            try:
                for tool in self.getOptimizer(item).tools:
                    logging.info('    Running ' + tool.__name__)
                    tool(item).execute()

            except:
                logging.error('  Error while compressing \'' + str(item) + '\'')

            else:
                item.removeBackup()
                results.reportItem(item)

        results.reportTotals(filenames)
