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

SCREEN_SIZE = [1500, 600]
BACKGROUND_COLOR = [242, 240, 250]

pygame.init()
main_window = pygame.display.set_mode(SCREEN_SIZE)

ship = Ship()
rock_group = pygame.sprite.Group()

running = True
clock = pygame.time.Clock()
spawn_tick = 0

while running:
    events = pygame.event.get()
    clock.tick(60)
    main_window.fill(BACKGROUND_COLOR)
    running = listen_quit(events)

    ship.update(events)

    for rock in rock_group:
        rock.update(events)

    if spawn_tick > 300:
        rock = Rock()
        rock_group.add(rock)
        spawn_tick = 0
    spawn_tick += 1

    pygame.display.flip()

pygame.quit()
