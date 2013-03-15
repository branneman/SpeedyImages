from fileutil import fileutil

class QueueItem:

    filename = ''
    filetype = ''
    filesize = 0

    def __init__(self, filename):
        self.filename = filename
        self.filetype = fileutil.getFiletype(filename)
        self.filesize = fileutil.getFilesize(filename)

    def __str__(self):
        return self.filename

    def createBackup(self):
        fileutil.createBackup(self.filename)

    def removeBackup(self):
        fileutil.removeBackup(self.filename)
