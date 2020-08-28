import sys
import pygame
from pygame.locals import *
from Projectile import *


pygame.init()

clock = pygame.time.Clock()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
screencolor = (0, 0, 0)

Bullets = []
bulletcooldown = 12
cooldowncounter = 0


while 1:
    clock.tick(60)
    screen.fill(screencolor)
    if cooldowncounter > 0:
        cooldowncounter -= 1

    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if (pressed[K_SPACE] and cooldowncounter == 0):
        cooldowncounter = bulletcooldown
        Bullets.append(Projectile(640, 700, 0, -2))

    for Bullet in Bullets:
        Bullet.draw(screen)
        Bullet.move()
    pygame.display.flip()
