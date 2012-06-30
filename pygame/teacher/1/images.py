#Initialising pygame
import pygame
from pygame.locals import *
import math
import loader

pygame.init()
pygame.display.set_mode((1024, 768))

screen = pygame.display.get_surface()

#background = pygame.Surface((screen.get_width(), screen.get_height())).convert()
#background.fill((0,0,0))

background = loader.load_image("background.png")
background = pygame.transform.smoothscale(background, (screen.get_width(), screen.get_height()))

screen.blit(background, (0,0))
pygame.display.flip()

#Transforming surfaces
image = loader.load_image("ship0.png")
image = pygame.transform.smoothscale(image, (100, 100))

image2 = loader.load_image("ship1.png", (255, 0, 150))
#image2 = loader.load_image("ship1.png", -1)

image3 = loader.load_image("ship1.png", (255, 0, 150))

#Surface alpha
image.set_alpha(100)
image2.set_alpha(50)

currRotation = 0

clock = pygame.time.Clock()

exited = False
while not exited:
    clock.tick(30)

    screen.blit(background, (0,0))

    #Bad rotation
    image3 = pygame.transform.rotate(image3, 1)

    #Better rotation
    image4 = pygame.transform.rotate(image, currRotation)
    currRotation = currRotation + 1

    #Displaying image
    screen.blit(image, (0,0))
    screen.blit(image2, (100,0))
    screen.blit(image3, (200,0))
    screen.blit(image4, (300,0))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True
