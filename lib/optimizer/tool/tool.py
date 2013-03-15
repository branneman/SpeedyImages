from os import devnull, name as osname
from subprocess import call
from platform import architecture

class tool:

    toolDir = 'tools/' + osname + '/' + architecture()[0] + '/'

    def __init__(self, item):
        self.file = item.filename

    def before(self):
        pass

    def after(self):
        pass

    def execute(self):
        self.before()
        call(self.getCommand(), stdout = open(devnull, 'w'))
        self.after()

    def getCommand(self):
        return [self.toolDir + self.tool] + self.commands + [self.file]
