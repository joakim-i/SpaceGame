import sys, pygame
from Background import ScrollingBG
import GUI
from Particles import Effect
from Renderer import Renderer

pygame.init()
FPS = 60
clock = pygame.time.Clock()
screen_size = screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode(screen_size)
scrollingBG = ScrollingBG(screen_size, 100, screen)
mainMenu = GUI.MainMenu(screen)

while 1:
    clock.tick(FPS)

    ##### EVENTS #####
    events = pygame.event.get()
    for event in events:
        # Check regardless of mainMenu
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainMenu.setActive(not mainMenu.isActive())

        # Only check if mainMenu is closed!
        if not mainMenu.isActive():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Effect.explosion(pygame.mouse.get_pos(), 300, 0.03, 7)
                Effect.testEffect(pygame.mouse.get_pos())
                #Effect.bullet_hit(pygame.mouse.get_pos(), 20, (1,1))

        # Only check if mainMenu is Open!
        if mainMenu.isActive():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mainMenu.update(pygame.mouse.get_pos(), True)

    ##### PRE-DRAW UPDATE #####
    # Regardless of mainMenu
    Effect.update()

    # Update only if mainMenu is closed!
    if not mainMenu.isActive():
        scrollingBG.update()

    # Update only if mainMenu is open!
    if mainMenu.isActive():
        mainMenu.update(pygame.mouse.get_pos())

    ##### DRAWING #####
    # Draw regardless of mainMenu
    screen.fill((0, 0, 0))
    Renderer.draw_background(screen)
    Renderer.draw_decorations(screen)
    Renderer.draw_particles(screen)
    Renderer.draw_bullets(screen)
    Renderer.draw_enemies(screen)
    Renderer.draw_player(screen)


    testsurf = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
    pygame.draw.circle(testsurf, (255, 0, 0), (50, 50), 40)
    testsurf2 = pygame.Surface((100, 100), pygame.SRCALPHA, 32)
    pygame.draw.circle(testsurf2, (0, 255, 0), (80, 50), 20)
    testsurf.blit(testsurf2, (0,0), special_flags=pygame.BLEND_RGB_ADD)
    screen.blit(testsurf, (100,100), special_flags=pygame.BLEND_RGBA_ADD)



    # Draw only if mainMenu is closed!
    if not mainMenu.isActive():
        Renderer.draw_UI(screen)

    # Draw only if mainMenu is open!
    if mainMenu.isActive():
        Renderer.draw_main_menu(screen)

    # Display update, must be last!
    pygame.display.update()

