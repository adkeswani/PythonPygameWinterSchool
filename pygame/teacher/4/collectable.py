import pygame
from pygame.locals import *
import bullet

import loader
import math
import random

COLLECTABLE_IMAGE = pygame.transform.smoothscale(loader.load_image("star.png"), (25, 25))

class Collectable(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = COLLECTABLE_IMAGE
        self.rect = self.image.get_rect()
        
        self.rect.center = (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))
        self.screen = screen
        
        self.vel = [random.randint(-10, 10), random.randint(-10, 10)]

    def update(self):
        self.rect.centerx = self.rect.centerx + self.vel[0]
        self.rect.centery = self.rect.centery + self.vel[1]

        if (self.rect.centerx > self.screen.get_width()):
            self.vel[0] = -self.vel[0]
            self.rect.centerx = self.screen.get_width()
        if (self.rect.centerx < 0):
            self.vel[0] = -self.vel[0]
            self.rect.centerx = 0

        if (self.rect.centery > self.screen.get_height()):
            self.vel[1] = -self.vel[1]
            self.rect.centery = self.screen.get_height()
        if (self.rect.centery < 0):
            self.vel[1] = -self.vel[1]
            self.rect.centery = 0

    def kill(self):
        print "Death!"
        super(Collectable, self).kill()
        #pygame.sprite.Sprite.kill(self)
