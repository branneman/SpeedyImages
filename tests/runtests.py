from sys import argv
from shutil import copy as copy
from os import listdir, path, remove, name as osname
from subprocess import call

baseDir   = 'tests/'
testsDir  = baseDir + 'originals/'
targetDir = baseDir + 'output/'
testfiles = listdir(testsDir)

def prepareFile(file):
    oldPath = testsDir  + file
    newPath = targetDir + file
    if path.exists(newPath):
        remove(newPath)
    if path.exists(oldPath):
        copy(oldPath, newPath)
    return newPath

def execute(files):
    for key, file in enumerate(files):
        files[key] = prepareFile(file)
    if '-q' in argv:
        files = ['-q'] + files
    else:
        print('-' * 80)
    call(['speedyimages' + ('.bat' if osname == 'nt' else '.sh')] + files)

# Test 1: All files
for testfile in testfiles:
    execute([testfile])

# Test 2: All files together in a single command
if len(testfiles) >= 2:
    execute(testfiles)
else:
    print('Could not complete second test, 2 or more test files are needed')

if not '-q' in argv:
    print('-' * 80)
    print('Tests completed.')
