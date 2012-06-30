#Initialising pygame
import pygame
from pygame.locals import *
import math

pygame.init()
pygame.display.set_mode((0, 0))

#Surfaces
screen = pygame.display.get_surface()

background = pygame.Surface((screen.get_width(), screen.get_height())).convert()
background.fill((0,0,0))
screen.blit(background, (0,0))
pygame.display.flip()

blueSquare = pygame.Surface((100, 100))
blueSquare.fill((0,0,170))

#Frame rate
clock = pygame.time.Clock()

exited = False
while not exited:
    clock.tick(30)

    screen.blit(blueSquare, (0,0))
    pygame.display.flip()

    #Events
    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True

#frequency = 0.3
#l = []
#for i in range(0,32)
    #red = math.sin(frequency * i + 0) * 127 + 128;
    #green = math.sin(frequency * i + 2 * math.pi / 3) * 127 + 128;
    #blue = math.sin(frequency * i + 4 * math.pi / 3) * 127 + 128;
    #l.append((red, green, blue))
