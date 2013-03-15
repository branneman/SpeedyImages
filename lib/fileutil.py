from shutil import copy
from os import path, remove

class fileutil:

    def isFile(file):
        return path.exists(file) and path.isfile(file)

    def isDirectory(file):
        return path.exists(file) and path.isdir(file)

    # todo implement
    def getFilesInDirectory(arg):
        return []

    def createBackup(file):
        copy(file, file + '~')

    def removeBackup(file):
        remove(file + '~')

    def getFiletype(file):
        return path.splitext(file)[1]

    def getFilesize(file):
        return path.getsize(file)

    def getTotalFilesize(filelist):
        return sum([fileutil.getFilesize(file) for file in filelist])
