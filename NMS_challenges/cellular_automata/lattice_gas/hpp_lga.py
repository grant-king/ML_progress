from lga_models import *

def listen_quit(events_list):
    for event in events_list:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
            elif event.type == QUIT:
                return False
    return True

def increase_tick(events_list):
    global tick
    for event in events_list:
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                tick += 1
                print(tick)

SCREEN_SIZE = [1920, 1080]
LATTICE_SEPARATION = 50 #distance btw verticies
BACKGROUND_COLOR = [255, 255, 255]

pygame.init()
main_window = pygame.display.set_mode(SCREEN_SIZE)
main_window.fill(BACKGROUND_COLOR)



running = True
clock = pygame.time.Clock()
tick = 10

while running:
    clock.tick(tick)
    events = pygame.event.get()
    running = listen_quit(events)
    increase_tick(events)

    pygame.display.flip()

pygame.quit()