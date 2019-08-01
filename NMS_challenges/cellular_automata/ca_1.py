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
CELL_SIZE = 30
BACKGROUND_COLOR = [0, 3, 1]

pygame.init()
main_window = pygame.display.set_mode(SCREEN_SIZE)
main_window.fill(BACKGROUND_COLOR)

grid = Grid(CELL_SIZE)

running = True
clock = pygame.time.Clock()
draw_cell = 0

while running:
    events = pygame.event.get()
    clock.tick(10)
    print()
    running = listen_quit(events)

    #interaction logic
    for cell in grid.cells:
        cidx, ridx = cell.column_idx, cell.row_idx
        try:
            #north, ne, e, se, s, sw, w, nw
            neighbors = [
                grid.get_cell(cidx, ridx - 1).alive,
                grid.get_cell(cidx + 1, ridx - 1).alive,
                grid.get_cell(cidx + 1, ridx).alive,
                grid.get_cell(cidx + 1, ridx + 1).alive,
                grid.get_cell(cidx, ridx + 1).alive,
                grid.get_cell(cidx - 1, ridx + 1).alive,
                grid.get_cell(cidx - 1, ridx).alive,
                grid.get_cell(cidx - 1, ridx - 1).alive,
                ]
            neighborhood = sum(neighbors)
            if cell.alive:
                if neighborhood < 2 or neighborhood > 3:
                    cell.alive = False
            else:
                if neighborhood == 3:
                    cell.alive = True
        except:
            pass

    #update and draw
    for cell in grid.cells:
        cell.update(events)

    pygame.display.flip()

pygame.quit()
