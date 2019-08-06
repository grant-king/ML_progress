from traffic_models import *

def listen_quit(events_list):
    #listen for quit
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
CELL_SIZE = 15
BACKGROUND_COLOR = [10, 10, 20]

pygame.init()
main_window = pygame.display.set_mode(SCREEN_SIZE)
main_window.fill(BACKGROUND_COLOR)

grid = Grid(CELL_SIZE, 9)

running = True
clock = pygame.time.Clock()
tick = 11
print_tick = 0

while running:
    clock.tick(tick)
    events = pygame.event.get()

    running = listen_quit(events)
    increase_tick(events)

    grid.update()

    pygame.display.flip()

pygame.quit()
