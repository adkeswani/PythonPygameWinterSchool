import pygame
from pygame.locals import *

import loader
import math

bulletImage = pygame.transform.smoothscale(loader.load_image("bullet.png"), (5, 20))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.rotate(bulletImage, angle)

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.vel = (5 * math.cos((angle + 90) * math.pi / 180.0), -5 * math.sin((angle + 90) * math.pi / 180.0))

    def update(self):
        self.rect.center = (self.rect.center[0] + self.vel[0], self.rect.center[1] + self.vel[1])
