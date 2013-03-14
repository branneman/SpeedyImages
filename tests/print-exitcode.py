from sys import argv
from subprocess import call

code = call(['speedyimages.bat'] + argv[1:])

print('Exit code: ' + str(code))
