#Initialising pygame
import pygame
from pygame.locals import *
import loader

pygame.init()
pygame.display.set_mode((0,0))

import ship
import collectable
import enemy

screen = pygame.display.get_surface()

background = pygame.transform.smoothscale(loader.load_image("background.png"), (screen.get_width(), screen.get_height()))
screen.blit(background, (0,0))
pygame.display.flip()

clock = pygame.time.Clock()

shipSprite = ship.Ship((screen.get_height() / 2, screen.get_width() / 2))

exited = False

collectables = pygame.sprite.RenderUpdates()
for i in range(0,10):
    collectables.add(collectable.Collectable(screen))

enemies = pygame.sprite.RenderUpdates()
for i in range(0,5):
    enemies.add(enemy.Enemy(screen))

while not exited:
    clock.tick(50)

    #Clear off previous frame, keeping track of what's changed
    rects = [screen.blit(background, shipSprite.rect, shipSprite.rect)]

    #Bullets
    shipSprite.bullets.clear(screen, background)
    shipSprite.bullets.update()
    rects.extend(shipSprite.bullets.draw(screen))

    #Collectables
    collectables.clear(screen, background)
    collectables.update()
    rects.extend(collectables.draw(screen))

    #Enemies
    enemies.clear(screen, background)
    enemies.update()
    rects.extend(enemies.draw(screen))

    shipSprite.update()

    #Draw new frame onto the screen, keeping track of what's changed
    rects.append(screen.blit(shipSprite.image, shipSprite.rect))

    #Display the parts of the screen that have changed
    pygame.display.update(rects)

    pygame.sprite.spritecollide(shipSprite, collectables, True)
    pygame.sprite.groupcollide(enemies, shipSprite.bullets, True, True)

    for event in pygame.event.get():
        if event.type == QUIT:
            exited = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            exited = True
