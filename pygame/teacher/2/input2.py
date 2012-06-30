#Initialising pygame
import pygame
from pygame.locals import *
import math
import loader
import random

pygame.init()
pygame.display.set_mode((1024, 768))

screen = pygame.display.get_surface()

background = pygame.Surface((screen.get_width(), screen.get_height())).convert()
background.fill((0,0,0))
screen.blit(background, (0,0))
pygame.display.flip()

#Transforming surfaces
image = loader.load_image("ship0.png")
image = pygame.transform.smoothscale(image, (50, 50))

images = [[image, (0, 0), (0, 0)]]
cooldown = 0

clock = pygame.time.Clock()

exited = False
while not exited:
    clock.tick(30)

    screen.blit(background, (0,0))

    mousePos = pygame.mouse.get_pos()

    #Displaying image
    for i in images:
        screen.blit(i[0], i[1])
        i[1] = (i[1][0] + i[2][0], i[1][1] + i[2][1])

    if pygame.mouse.get_pressed()[2] and (cooldown == 0):
        images.append([image.copy(), mousePos, (random.randint(-5,5), random.randint(-5,5))])
        cooldown = 100
    elif cooldown > 0:
        cooldown = cooldown - 1

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True
