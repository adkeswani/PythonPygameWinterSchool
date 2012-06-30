import pygame
from pygame.locals import *

import loader

bulletImage = pygame.transform.smoothscale(loader.load_image("bullet.png"), (5, 20))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = bulletImage

        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.rect.y = self.rect.y - 10
        if self.rect.y < 50:
            self.kill()
