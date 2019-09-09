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

def player_input(events_list, board):
    for event in events_list:
        if event.type == KEYDOWN:
            if event.key == K_KP7:
                board.play('x', [0, 0])
            if event.key == K_KP8:
                board.play('x', [0, 1])
            if event.key == K_KP9:
                board.play('x', [0, 2])
            if event.key == K_KP4:
                board.play('x', [1, 0])
            if event.key == K_KP5:
                board.play('x', [1, 1])
            if event.key == K_KP6:
                board.play('x', [1, 2])
            if event.key == K_KP1:
                board.play('x', [2, 0])
            if event.key == K_KP2:
                board.play('x', [2, 1])
            if event.key == K_KP3:
                board.play('x', [2, 2])


SCREEN_SIZE = [300, 300]
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

    #display
    main_window.fill(BACKGROUND_COLOR)
    board.update()
    pygame.display.flip()

    if board.finished:
        pygame.time.delay(1000)
        board = Board()

    #game logic
    if board.current_player == 'o':
        best_next = MCMove(board).get_next_move()
        board.play('o', best_next)
    else:
        player_input(events, board)
    
    #delay for visual
    pygame.time.delay(100)

    
pygame.quit()

