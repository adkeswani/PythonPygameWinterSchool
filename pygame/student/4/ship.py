import pygame
from pygame.locals import *
import bullet

import loader
import math

class Ship(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.smoothscale(loader.load_image("ship.png"), (50, 50))

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.bullets = pygame.sprite.RenderUpdates()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.rect.top = self.rect.top - 5
        if keys[K_DOWN]:
            self.rect.top = self.rect.top + 5
        if keys[K_LEFT]:
            self.rect.left = self.rect.left - 5
        if keys[K_RIGHT]:
            self.rect.left = self.rect.left + 5
        if keys[K_SPACE]:
            self.bullets.add(bullet.Bullet(self.rect.midtop))
