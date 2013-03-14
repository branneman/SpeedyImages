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

    def run(self):

        filenames = [q.filename for q in self.queue]
        results = report(filenames)

        for item in self.queue:

            logging.info('\n  Optimizing: ' + item.filename)

            item.createBackup()

            try:
                pass
                # implement something like item.getFiletype
                #for tool in self.tools:
                #    logging.info('    Running ' + tool.__name__)
                #    tool(file).compress()
            except:
                logging.error('  Error while compressing ' + file)
            else:
                item.removeBackup()
                results.reportItem(item)

        results.reportTotals(filenames)
