from optimizer.optimizer import optimizer
from optimizer.tool import *

class png(optimizer):

    ext = '.png'

    tools = [pngcrush, optipng, advpng, pngout, deflopt]
