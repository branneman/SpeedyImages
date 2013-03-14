import logging
from fileutil import fileutil

class report:

    totalOriginalSize = False

    def __init__(self, filenames):
        self.totalOriginalSize = fileutil.getTotalFilesize(filenames)

    def reportItem(self, item):
        optimizedSize = fileutil.getFilesize(item.filename)
        percentage    = int(100 - (optimizedSize / item.size) * 100)
        message       = '  Reduced size with %s%%: from %s to %s bytes.'
        logging.info(message % (percentage, item.size, optimizedSize))

    def reportTotals(self, filenames):
        optimizedSize = fileutil.getTotalFilesize(filenames)
        savedBytes    = self.totalOriginalSize - optimizedSize
        percentage    = int(100 - (optimizedSize / self.totalOriginalSize) * 100)
        message       = '\n  Saved a total of %s%%, or %s bytes in %s files. '
        logging.info(message % (percentage, savedBytes, len(filenames)))
