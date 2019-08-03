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

lanes = []
total_rows = SCREEN_SIZE[1] // CELL_SIZE
for lane_row in list(range(0, total_rows))[::2]:
    lanes.append(Lane(CELL_SIZE, lane_row, 25))

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(5)
    print()
    events = pygame.event.get()

    running = listen_quit(events)

    for lane in lanes:
        lane.update()

    pygame.display.flip()

pygame.quit()
