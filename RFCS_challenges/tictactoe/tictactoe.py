from ttt_models import *

def listen_quit(events_list):
    #listen for quit
    for event in events_list:
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
        elif event.type == QUIT:
            return False
    return True

SCREEN_SIZE = [900, 900]
BACKGROUND_COLOR = [245, 240, 250]

pygame.init()
main_window = pygame.display.set_mode(SCREEN_SIZE)

grid = Grid()
grid.play('x', [0, 1])
grid.play('x', [1, 1])
grid.play('o', [2, 1])

running = True
clock = pygame.time.Clock()

while running:
    events = pygame.event.get()
    clock.tick(60)
    main_window.fill(BACKGROUND_COLOR)
    #event handlers
    running = listen_quit(events)
    
    
    grid.draw()
    pygame.display.flip()

pygame.quit()