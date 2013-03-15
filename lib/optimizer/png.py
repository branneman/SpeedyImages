from optimizer.optimizer import optimizer
from optimizer.tool import *

class png(optimizer):

    ext = '.png'

    tools = [
        pngcrush.pngcrush,
        optipng.optipng,
        advpng.advpng,
        pngout.pngout,
        deflopt.deflopt
    ]
