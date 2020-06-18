
from PIL import Image
import os, sys

path = "0_raw/"
dirs = os.listdir( path )
dest = "1_resized/"

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(dest + item, 'JPEG', quality=90)

resize()