import pygame
from pygame.locals import *
import bullet

import loader
import math
import random

ENEMY_IMAGE = pygame.transform.smoothscale(loader.load_image("enemy.png"), (50, 50))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.image = ENEMY_IMAGE
        self.rect = self.image.get_rect()
        
        self.rect.center = (random.randint(0, screen.get_width()), random.randint(50, screen.get_height() / 2))
        self.screen = screen
        
        self.horzVel = random.randint(-10, 10)

    def update(self):
        self.rect.centerx = self.rect.centerx + self.horzVel

        if (self.rect.centerx > self.screen.get_width()):
            self.horzVel = -self.horzVel
            self.rect.centerx = self.screen.get_width()
        if (self.rect.centerx < 0):
            self.horzVel = -self.horzVel
            self.rect.centerx = 0
