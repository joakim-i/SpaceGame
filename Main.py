import sys, pygame
from Background import ScrollingBG
pygame.init()

clock = pygame.time.Clock()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
scrollingBG = ScrollingBG(size, 60, screen)

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((0, 0, 0))
    scrollingBG.Scroll()
    pygame.display.flip()
