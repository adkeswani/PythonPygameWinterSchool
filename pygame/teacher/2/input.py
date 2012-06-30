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

currVel = [0.0, 0.0]
currPos = [0.0, 0.0]
ACCELERATION = 1.0
DECELERATION_FACTOR = 0.95
MAX_VELOCITY = 10.0

exited = False
while not exited:
    clock.tick(30)

    screen.blit(background, (0,0))

    #Displaying image
    screen.blit(image, currPos)
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        currVel[1] = currVel[1] - ACCELERATION
    if keys[K_DOWN]:
        currVel[1] = currVel[1] + ACCELERATION
    if keys[K_LEFT]:
        currVel[0] = currVel[0] - ACCELERATION
    if keys[K_RIGHT]:
        currVel[0] = currVel[0] + ACCELERATION

    currPos[0] = currPos[0] + currVel[0]
    currPos[1] = currPos[1] + currVel[1]

    currVel[0] = currVel[0] * DECELERATION_FACTOR
    currVel[1] = currVel[1] * DECELERATION_FACTOR

    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True
