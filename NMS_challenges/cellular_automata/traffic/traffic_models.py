import pygame
from pygame.locals import *
import random

class Cell(pygame.sprite.Sprite):
    def __init__(self, square_size, column_idx, row_idx, living=False):
        super(Cell, self).__init__()
        
        startx = square_size * column_idx
        starty = square_size * row_idx

        self.START_LOC = [startx, starty]

        self.column_idx = column_idx 
        self.row_idx = row_idx

        red = random.randint(10, 50)
        blue = random.randint(60, 250)
        self.color = [red, abs(red-blue), blue]
        self.size = [square_size, square_size]
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.color)
        
        self.rect = self.surface.get_rect()
        self.rect.move_ip(self.START_LOC)

        self.alive = living

    def update(self):
        self.update_states()
        self.draw()

    def draw(self):
        main_window = pygame.display.get_surface()
        main_window.blit(self.surface, self.rect)

    def update_states(self):
        if self.alive:
            self.surface.fill(self.color)
        else:
            self.surface.fill([0, 0, 0])


class Stoplight(Cell):
    def __init__(self, square_size, column_idx, row_idx):
        super().__init__(square_size, column_idx, row_idx)

        self.SWITCH_FRAMES = random.randint(15, 40) # frames before switch
        self.switch_ticks = 0
        self.signal_state = 'red'
    
    def toggle_signal(self):
        if self.signal_state == 'red':
            self.signal_state = 'green'
        else:
            self.signal_state = 'red'

    def update(self):
        self.update_states()
        self.draw()
    
    def update_states(self):
        self.switch_ticks += 1
        if self.switch_ticks > self.SWITCH_FRAMES:
            self.switch_ticks = 0
            self.toggle_signal()

        if self.signal_state == 'red':
            self.surface.fill([240, 10, 5])
        elif self.signal_state == 'green':
            self.surface.fill([5, 240, 10])
        else:
            self.surface.fill([240, 240, 60])


class Lane:
    def __init__(self, cell_size, lane_idx, num_active, direction):
        
        self.direction = direction
        self.grid_lane_idx = lane_idx
        if self.direction == 1:
            self.row_idx = lane_idx
        else:
            self.col_idx = lane_idx
        self.num_active = num_active
        
        self.SCREEN_SIZE = pygame.display.get_surface().get_size()
        self.CELL_SIZE = cell_size

        self.total_columns = self.SCREEN_SIZE[0] // self.CELL_SIZE
        self.total_rows = self.SCREEN_SIZE[1] // self.CELL_SIZE
        
        self.intersection_idxs = [] #fill with cell idx's, bool occupied for each intersection
        self.moving = 0
        self.build_cells()

    def build_cells(self):
        #initialize full row of dead cells
        self.cells = []

        if self.direction == 1:
            for col_idx in range(self.total_columns):
                self.cells.append(Cell(self.CELL_SIZE, col_idx, self.row_idx))
        else:
            for row_idx in range(self.total_rows):
                self.cells.append(Cell(self.CELL_SIZE, self.col_idx, row_idx))

        #add stoplights, decrease stoplights to add as initial cars increases
        self.stoplights = []
        if self.direction == 1:
            for _ in range(self.total_columns // self.num_active + 1):
                light_idx = random.randrange(self.total_columns)
                self.stoplights.append(Stoplight(self.CELL_SIZE, light_idx, self.row_idx))
        else:
            for _ in range(self.total_rows // self.num_active + 1):
                light_idx = random.randrange(self.total_rows)
                self.stoplights.append(Stoplight(self.CELL_SIZE, self.col_idx, light_idx))

        for cell_idx in range(self.num_active):
            self.cells[cell_idx].alive = True

    @property
    def traffic_flow(self):
        density = self.num_active / len(self.cells)
        average_velocity = self.moving / self.num_active
        return density * average_velocity

    def redlight(self, cell_idx):
        """return true if passed cell_idx is on a red light"""
        stoplight_active = False
        if self.direction == 1:
            for stoplight in self.stoplights:
                if cell_idx == stoplight.column_idx:
                    if stoplight.signal_state == 'red':
                        stoplight_active = True
        else:
            for stoplight in self.stoplights:
                if cell_idx == stoplight.row_idx:
                    if stoplight.signal_state == 'red':
                        stoplight_active = True

        return stoplight_active

    def occupied_intersection(self, cell_idx):
        """return true if passed cell_idx is in an occupied intersection"""
        if cell_idx in self.intersection_idxs:
            #return intersection state at matching intersection index
            return self.intersection_idxs.index(cell_idx)[1]
        return False


    def update_flow(self):
        """update cells to activate on next step, return number of moving vehicles"""
        current_states = list([cell.alive for cell in self.cells])
        kill_cells, activate_cells = [], []

        for idx, cell in enumerate(self.cells):
            #wrap display
            if idx < len(self.cells) - 1:
                forward_neighbor = idx + 1
            else:
                forward_neighbor = 0

            #move forward only if space available, and not red and not occupied
            if current_states[idx] and not current_states[forward_neighbor]:
                if not self.redlight(forward_neighbor) and not self.occupied_intersection(forward_neighbor):
                    kill_cells.append(idx)
                    activate_cells.append(forward_neighbor)
        
        for cell_idx in kill_cells:
            self.cells[cell_idx].alive = False

        for cell_idx in activate_cells:
            self.cells[cell_idx].alive = True

        self.moving = len(activate_cells)

    def update(self):
        self.update_flow()

        #update cells
        for cell in self.cells:
            cell.update()
        for stoplight in self.stoplights:
            stoplight.update()
        
    def __str__(self):
        return f'Lane {self.row_idx}, Flow: {self.traffic_flow:.4f}'
    
    def __repr__(self):
        if self.direction == 1:
            return f'{self.row_idx} of {self.total_rows}'
        else:
            return f'{self.col_idx} of {self.total_columns}'


class Grid:
    def __init__(self, cell_size, spacing):
        self.SCREEN_SIZE = pygame.display.get_surface().get_size()
        self.CELL_SIZE = cell_size
        self.SPACING = spacing
        
        self.lanes = []
        self.lanes_vert = []
        self.build_lanes()
        self.set_intersections()

    def build_lanes(self):
        total_rows = self.SCREEN_SIZE[1] // self.CELL_SIZE
        total_cols = self.SCREEN_SIZE[0] // self.CELL_SIZE
        for lane_row in list(range(0, total_rows))[::self.SPACING]:
            self.lanes.append(Lane(self.CELL_SIZE, lane_row, total_cols // self.SPACING, 1))

        for lane_col in list(range(0, total_cols))[::self.SPACING]:
            self.lanes_vert.append(Lane(self.CELL_SIZE, lane_col, total_rows // self.SPACING, 0))
    
    def update_intersections(self):
        for lane in self.lanes:
            for intersecting, state in lane.intersection_idxs:
                


    def update(self):
        for lane in self.lanes:
            lane.update()

        for lane in self.lanes_vert:
            lane.update()

        update_intersections()
            
    def set_intersections(self):
        #set location of each intersection, along each lane in grid
        for lane in self.lanes:
            lane.intersection_idxs = [[intersecting_lane.grid_lane_idx for intersecting_lane in self.lanes_vert], False]
        for lane in self.lanes_vert:
            lane.intersection_idxs = [[intersecting_lane.grid_lane_idx for intersecting_lane in self.lanes], False]


