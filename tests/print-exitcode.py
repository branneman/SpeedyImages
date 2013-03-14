from sys import argv
from subprocess import call

code = call(['speedypng.bat'] + argv[1:])

print('Exit code: ' + str(code))
