import os, pygame, sys
from pygame.locals import *

def load_image(name, colorkey=None):
    fullname = os.path.join(sys.path[0], 'images', name)

    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message

    if colorkey is not None:
        image = image.convert()
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey)
    else:
        image.convert_alpha()

    return image

def load_sound(name):
    class NoneSound:
        def play(self): pass

    if not pygame.mixer:
        return NoneSound()

    fullname = os.path.join(sys.path[0], 'sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname 
        raise SystemExit, message

    return sound

def load_font(name, size):
    fullname = os.path.join(sys.path[0], 'fonts', name)
    try:
        font = pygame.font.Font(fullname, size)
    except pygame.error, message:
        print 'Cannot load font:', fullname
        raise SystemExit, message

    return font
    
