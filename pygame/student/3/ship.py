import pygame
from pygame.locals import *

import loader
import math

class Ship(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.smoothscale(loader.load_image("ship.png"), (50, 50))

        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.rect.x = self.rect.x + 1
