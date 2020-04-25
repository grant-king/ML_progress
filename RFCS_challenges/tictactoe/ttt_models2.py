class BoardDrawing:
    def __init__(self, board):
        self.board = board

        self.cell_size = self.board.cells[0][0].size
        self.size = [self.cell_size[0] * self.board.COLS, self.cell_size[1] * self.board.ROWS]
        self.surface = pygame.Surface(self.size)
        self.rect = self.surface.get_rect()
        
        self.generate_overlay()

    def draw(self):
        main_window = pygame.display.get_surface()

        #draw cells and contents
        for cell_row in self.cells:
            for cell in cell_row:
                cell.draw(self.surface)
        
        #add overlay
        self.surface.blit(self.border_overlay, self.rect)

        #draw composite on main display
        main_window.blit(self.surface, self.rect)

    def generate_overlay(self):
        overlay_color = [100, 100, 100]
        overlay_surface = pygame.Surface(self.size)
        overlay_surface.set_colorkey([0, 0, 0])
        line_width = 10

        vert_line_separation = self.size[0] // self.COLS
        horiz_line_separation = self.size[1] // self.ROWS
        
        for row in range(1, self.ROWS):
            start_pos = [0, row*horiz_line_separation]
            end_pos = [self.size[0], row*horiz_line_separation]
            pygame.draw.line(overlay_surface, overlay_color, start_pos, end_pos, line_width)

        for col in range(1, self.COLS):
            start_pos = [col*vert_line_separation, 0]
            end_pos = [col*vert_line_separation, self.size[1]]
            pygame.draw.line(overlay_surface, overlay_color, start_pos, end_pos, line_width)

        self.border_overlay = overlay_surface


