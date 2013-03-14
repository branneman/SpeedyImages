from fileutil import fileutil

class QueueItem:

    filename = ''
    size     = 0

    def __init__(self, filename):
        self.filename = filename
        self.size     = fileutil.getFilesize(filename)

    def getFiletype(self):
        return path.splitext(self.filename)[1][1:]

    def createBackup(self):
        fileutil.createBackup(self.filename)

    def removeBackup(self):
        fileutil.removeBackup(self.filename)
