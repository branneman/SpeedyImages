from os import remove, rename

from optimizer.tool.tool import tool

class pngcrush(tool):

    tool = 'pngcrush'

    commands = ['-q', '-rem gAMA', '-rem alla', '-rem cHRM', '-rem iCCP', '-rem sRGB', '-rem time']

    def getCommand(self):
        return [self.toolDir + self.tool] + self.commands + [self.file, self.file + '~.tmp']

    def after(self):
        remove(self.file)
        rename(self.file + '~.tmp', self.file)
