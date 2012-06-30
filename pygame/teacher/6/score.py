import pygame
from pygame.locals import *
import bullet

import loader
import math

SCORE_FONT = loader.load_font("digit.ttf", 50)

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.score = 0
        self.image = SCORE_FONT.render(str(self.score), True, (255, 255, 255))

        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    def update(self):
        self.image = SCORE_FONT.render(str(self.score), True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.score = self.score + 1
