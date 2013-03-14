#!/usr/bin/env python

import sys, subprocess

if sys.version_info < (3, 3):
    print('Python 3.3 or greater is required')
    sys.exit(1)

command = ['/usr/bin/env', 'python', 'lib/cli.py'] + sys.argv[1:]
sys.exit(subprocess.call(command))
