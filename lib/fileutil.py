from shutil import copy
from os import path, remove

class fileutil:

    def createBackup(file):
        copy(file, file + '~')

    def removeBackup(file):
        remove(file + '~')

    def getFilesize(file):
        return path.getsize(file)

    def getTotalFilesize(filelist):
        return sum([fileutil.getFilesize(file) for file in filelist])
