#Unused

from pygame.key import get_pressed, locals
from pygame.version import PygameVersion


class EventManager():
    inputs = get_pressed()

    ##### EVENTS #####
    events = PygameVersion.event.get()
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

#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_SPACE:
#                    Projectile((player1.x, player1.y), 0, -8)
        
        # Only check if mainMenu is Open!
        if mainMenu.isActive():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mainMenu.update(pygame.mouse.get_pos(), True)