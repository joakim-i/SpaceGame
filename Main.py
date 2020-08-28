import sys, pygame
pygame.init()

clock = pygame.time.Clock()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

while 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((100, 0, 0))
    pygame.display.flip()
