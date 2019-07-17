from skidship_models import *


def listen_quit(events_list):
    #listen for quit
    for event in events_list:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
        elif event.type == QUIT:
            return False
    return True

SCREEN_SIZE = [900, 600]
BACKGROUND_COLOR = [245, 240, 250]

pygame.init()
main_window = pygame.display.set_mode(SCREEN_SIZE)

#initialize game objects

#initialize sprites and groups

running = True
clock = pygame.time.Clock()

while running:
    events = pygame.event.get()
    clock.tick(60)
    main_window.fill(BACKGROUND_COLOR)

    running = listen_quit(events)

    pygame.display.flip()
