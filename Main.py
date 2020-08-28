import sys, pygame
from pygame.locals import *


pygame.init()

clock = pygame.time.Clock()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
screencolor = (0,0,0)

while 1:
    clock.tick(60)
    screen.fill(screencolor)

    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if pressed[K_SPACE]:
        screencolor = (100,0,0)
    else:
            screencolor = (0,0,0)


    pygame.display.flip()
