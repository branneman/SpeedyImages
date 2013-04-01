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

    argumentsNotRecognized = []
    unsupportedFiles       = []
    dependenciesNotFound   = []

    optimizers = [png()]
    queue = []

    def bootstrap(self):
        self.setupLogging()
        self.checkDependencies()
        self.processArguments()

    def setupLogging(self):

        lvl = 'INFO'
        if '-q' in argv:
            lvl = 'WARNING'
        if '-s' in argv:
            lvl = 'ERROR'

        logging.basicConfig(
            level  = lvl,
            format = '%(message)s'
        )

    def checkDependencies(self):
        for optimizer in self.optimizers:
            notfound = optimizer.checkDependencies()
            if notfound:
                self.dependenciesNotFound += notfound

    def processArguments(self):

        for arg in argv:

            if self.isOption(arg):
                self.options[arg] = True

            elif fileutil.isFile(arg):
                if self.isSupportedFile(arg):
                    self.queue.append(QueueItem(arg))
                elif not self.isSelf(arg):
                    self.unsupportedFiles.append(arg)

            elif fileutil.isDirectory(arg):
                for file in fileutil.getFilesInDirectory(arg):
                    if fileutil.isFile(arg) and self.isSupportedFile(arg):
                        self.queue.append(QueueItem(arg))

            else:
                self.argumentsNotRecognized.append(arg)

    def isOption(self, arg):
        return arg in self.options.keys()

    def isSupportedFile(self, arg):
        return fileutil.getFiletype(arg) in [cl.ext for cl in self.optimizers]

    def isSelf(self, arg):
        return arg.split('/')[-1] in ['cli.py', 'gui.py']

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
