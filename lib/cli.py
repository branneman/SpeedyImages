import logging

from app import App

class CLI(App):

    def __init__(self):

        self.bootstrap()

        self.welcome()
        if not len(self.queue):
            self.usage()

        self.errors()

    def welcome(self):
        lvl = logging.WARNING if self.options['-v'] else logging.INFO
        logging.log(lvl, self.name + ' - v' + str(self.VERSION))

    def errors(self):
        for dependency in self.dependenciesNotFound:
            logging.warning(' Dependency not found: ' + dependency.tool)
        for argument in self.argumentsNotRecognized:
            logging.warning(' Argument not recognized or file not found: \'%s\'' % argument)

    def usage(self):
        logging.warning('\n Usage: ./speedyimages [options] [files...]\n')
        logging.warning(' Options:')
        logging.warning('  -v  Show version.')
        logging.warning('  -q  Quiet mode, will only output on error.')
        logging.warning('  -s  Silent mode, will never output.\n')

if __name__ == '__main__':
    try:
        application = CLI()
        code = application.run()
    except:
        logging.critical('Internal error')
        code = 1
    exit(code)
