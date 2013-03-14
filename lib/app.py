import logging
from os import path
from sys import argv

from queue.item import QueueItem
from optimizer.png import png
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

            if self.isFile(arg) and self.isSupportedFile(arg):
                self.queue.append(QueueItem(arg))

            elif self.isDirectory(arg):
                for file in self.getFilesInDirectory():
                    if self.isFile(file) and self.isSupportedFile(file):
                        self.queue.append(QueueItem(file))

    # move to fileutil
    def isOption(self, arg):
        return arg in self.options.keys()

    # move to fileutil
    def isFile(self, arg):
        return path.exists(arg) and path.isfile(arg)

    # move to fileutil
    def isDirectory(self, arg):
        return path.exists(arg) and path.isdir(arg)

    # move to fileutil
    def isSupportedFile(self, arg):
        return path.splitext(arg)[1] in [cl.ext for cl in self.optimizers]

    # move to fileutil & implement
    def getFilesInDirectory(self, arg):
        return []

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
