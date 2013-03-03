from shutil import copy as copy
from os import listdir, path, remove
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

def execute(parts):
    for key, part in enumerate(parts):
        parts[key] = prepareFile(part)
    print('-' * 80)
    call(['python', 'SpeedyPNG.py'] + parts)

# Test 1: All files
for testfile in testfiles:
    execute([testfile])

# Test 2: Two files together in a single command
if len(testfiles) >= 2:
    execute([testfiles[0], testfiles[1]])
else:
    print('Could not complete second test, 2 or more test files are needed')

print('-' * 80)
print('Tests completed.')
