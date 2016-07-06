from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps

from PIL.ImageFont import *
from PIL.ImageDraw import *


im = Image.open("c:/deneme.jpg")
print( im.format, im.size, im.mode)
ImageOps.autocontrast(im)
im.show()


