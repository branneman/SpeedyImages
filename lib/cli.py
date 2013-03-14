import logging

from app import App

class CLI(App):

    def __init__(self):

        self.processOptionArguments()
        self.setupLogging()
        self.welcome()
        self.processFileArguments()

        if not len(self.queue):
            logging.warning('\n Usage: ./speedypng [options] [files...]\n')
            logging.warning(' Options:')
            logging.warning('  -v  Show version, but will show nothing when combined with -s).')
            logging.warning('  -q  Quiet mode, will only output on error.')
            logging.warning('  -s  Silent mode, will never output.\n')

    def welcome(self):
        lvl = logging.WARNING if self.options['-v'] else logging.INFO
        logging.log(lvl, 'SpeedyPNG - v' + str(self.VERSION))

if __name__ == '__main__':
    CLI()
