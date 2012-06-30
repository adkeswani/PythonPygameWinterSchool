#Initialising pygame
import pygame
from pygame.locals import *
import math
import loader

pygame.init()
pygame.display.set_mode((1024, 768))

screen = pygame.display.get_surface()

background = pygame.Surface((screen.get_width(), screen.get_height())).convert()
background.fill((0,0,0))
screen.blit(background, (0,0))
pygame.display.flip()

#Transforming surfaces
image = loader.load_image("ship0.png")
image = pygame.transform.smoothscale(image, (100, 100))

clock = pygame.time.Clock()

exited = False
while not exited:
    clock.tick(30)

    screen.blit(background, (0,0))

    #Displaying image
    screen.blit(image, (0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True
