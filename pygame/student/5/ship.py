import pygame
from pygame.locals import *
import bullet

import loader
import math

SHIP_IMAGE = pygame.transform.smoothscale(loader.load_image("ship.png"), (50, 50))

class Ship(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = SHIP_IMAGE

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.bullets = pygame.sprite.RenderUpdates()

        self.angle = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.rect.top = self.rect.top - 5
        if keys[K_DOWN]:
            self.rect.top = self.rect.top + 5
        if keys[K_SPACE]:
            self.bullets.add(bullet.Bullet(self.rect.midtop))

        center = self.rect.center
        self.image = pygame.transform.rotate(SHIP_IMAGE, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = center
        
        self.angle = self.angle + 1
