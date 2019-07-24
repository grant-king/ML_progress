from sim_models import *


def listen_quit(events_list):
    #listen for quit
    for event in events_list:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
        elif event.type == QUIT:
            return False
    return True

SCREEN_SIZE = [1400, 700]
BACKGROUND_COLOR = [0, 0, 0]

pygame.init()
main_window = pygame.display.set_mode(SCREEN_SIZE)

particles = [Particle() for item in range(1000)]

running = True
clock = pygame.time.Clock()
spawn_tick = 0

while running:
    events = pygame.event.get()
    #clock.tick(300)
    #main_window.fill(BACKGROUND_COLOR)
    running = listen_quit(events)

    for particle in particles:
        particle.update(events)

    pygame.display.flip()

pygame.quit()
