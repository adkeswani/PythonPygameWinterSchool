import pygame
import math
from pygame.locals import *

BACKGROUND_COLOUR = (0, 0, 0)

pygame.init()
pygame.display.set_mode((0,0))
screen = pygame.display.get_surface()

background = pygame.Surface((screen.get_height(), screen.get_width())).convert()
background.fill(BACKGROUND_COLOUR)
screen.blit(background, (0,0))
pygame.display.flip()

clock = pygame.time.Clock()

surfaces = []
frequency = 0.3
for i in range(0,32):
    r = math.sin(frequency * i + 0) * 127 + 128;
    g = math.sin(frequency * i + 2 * math.pi / 3) * 127 + 128;
    b = math.sin(frequency * i + 4 * math.pi / 3) * 127 + 128;

    surf = pygame.Surface((80, 80)).convert()
    surf.fill((r,g,b))
    surfaces.append(surf)

exited = False
curr = 0
while not exited:
    clock.tick(30)

    screen.blit(background, (0,0))
    
    for i in range(0, 32):
        screen.blit(surfaces[(i + curr) % 32], ((i % 8) * 100, (i / 8) * 100))
    curr = (curr + 1) % 32

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True

#frequency = 0.3
#for loop, 32 times
#red = math.sin(frequency * i + 0) * 127 + 128;
#green = math.sin(frequency * i + 2 * math.pi / 3) * 127 + 128;
#blue = math.sin(frequency * i + 4 * math.pi / 3) * 127 + 128;
