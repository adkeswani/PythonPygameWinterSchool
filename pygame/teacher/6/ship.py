import pygame
from pygame.locals import *
import bullet

import loader
import math

SHIP_IMAGE = pygame.transform.smoothscale(loader.load_image("ship.png"), (50, 50))
BULLET_SOUND = loader.load_sound("bullet.wav")

class Ship(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = SHIP_IMAGE

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.bullets = pygame.sprite.RenderUpdates()
        self.reload = 0

        self.angle = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.rect.center = (self.rect.center[0] + 5 * math.cos((self.angle + 90) * math.pi / 180.0), self.rect.center[1] - 5 * math.sin((self.angle + 90) * math.pi / 180.0))
        if keys[K_DOWN]:
            self.rect.center = (self.rect.center[0] - 5 * math.cos((self.angle + 90) * math.pi / 180.0), self.rect.center[1] + 5 * math.sin((self.angle + 90) * math.pi / 180.0))
        if keys[K_LEFT]:
            self.angle = self.angle + 3
            self.image = pygame.transform.rotate(SHIP_IMAGE, self.angle)
            center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = center
        if keys[K_RIGHT]:
            self.angle = self.angle - 3
            self.image = pygame.transform.rotate(SHIP_IMAGE, self.angle)
            center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = center
        if keys[K_SPACE] and self.reload == 0:
            BULLET_SOUND.play()
            self.bullets.add(bullet.Bullet(self.rect.center, self.angle))
            self.reload = 20

        if self.reload > 0:
            self.reload = self.reload - 1
