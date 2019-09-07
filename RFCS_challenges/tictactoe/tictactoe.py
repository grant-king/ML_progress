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

board = Board()

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    events = pygame.event.get()
    #event handlers
    running = listen_quit(events)

    main_window.fill(BACKGROUND_COLOR)
    
    board.update()
    pygame.display.flip()

    #delay for visual
    pygame.time.delay(750)

    
    
pygame.quit()

