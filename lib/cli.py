import logging

from app import App

class CLI(App):

    def __init__(self):

        self.bootstrap()
        self.welcome()
        self.dependencies()

        if len(self.queue):
            self.run()
        else:
            self.usage()

    def welcome(self):
        lvl = logging.WARNING if self.options['-v'] else logging.INFO
        logging.log(lvl, self.name + ' - v' + str(self.VERSION))

    def dependencies(self):
        for dependency in self.dependenciesNotFound:
            logging.error(' Dependency not found: ' + dependency.tool)

    def usage(self):
        logging.warning('\n Usage: ./speedyimages [options] [files...]\n')
        logging.warning(' Options:')
        logging.warning('  -v  Show version (will show nothing when combined with -s).')
        logging.warning('  -q  Quiet mode, will only output on error.')
        logging.warning('  -s  Silent mode, will never output.\n')

if __name__ == '__main__':
    CLI()
