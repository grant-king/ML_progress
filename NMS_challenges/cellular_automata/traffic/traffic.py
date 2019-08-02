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

SCREEN_SIZE = [1280, 720]
CELL_SIZE = 30
BACKGROUND_COLOR = [0, 3, 1]

pygame.init()
main_window = pygame.display.set_mode(SCREEN_SIZE)
main_window.fill(BACKGROUND_COLOR)

lane = Lane(CELL_SIZE, 5, 1, 5)

running = True
clock = pygame.time.Clock()
draw_cell = 0

while running:
    events = pygame.event.get()
    clock.tick(10)
    print()
    running = listen_quit(events)

    #interaction logic

    #update and draw
    for cell in lane.cells:
        cell.update(events)

    pygame.display.flip()

pygame.quit()
