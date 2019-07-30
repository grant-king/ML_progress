from ca_models import *

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
BACKGROUND_COLOR = [0, 3, 1]

pygame.init()
main_window = pygame.display.set_mode(SCREEN_SIZE)
main_window.fill(BACKGROUND_COLOR)

#populate array with enough cell objects to fill screen
cells = [[Cell(x_idx*50, y_idx*50, random.choice([True, False])) for x_idx in range(SCREEN_SIZE[0] // 50)] for y_idx in range(SCREEN_SIZE[1] // 50)]

running = True
clock = pygame.time.Clock()
clear_tick = 0

while running:
    events = pygame.event.get()
    clock.tick(5)
    
    running = listen_quit(events)

    for row in cells:
        for cell in row:
            cell.update(events)

    pygame.display.flip()

pygame.quit()
