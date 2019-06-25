import pygame
from pygame.locals import *

class Button(pygame.sprite.Sprite):
    def __init__(self):
        super(Button, self).__init__()
        self.surface = pygame.Surface((50, 50))
        self.surface.fill((255, 255, 255))
        self.rect_location = self.surface.get_rect()

def draw_time(milis):
    global window

    if pygame.font:
        font = pygame.font.Font(None, 160)
        message = f'{milis // 1000}.{str(milis % 1000)[0]}'
        text = font.render(message, True, (0, 255, 40))
    
        window.blit(text, [20, 20]) 

def draw_button():
    global window
    button = Button()
    
    window.blit(button.surface, [20, 150])

def handler_stop(milis):
    print(f'Spacebar pressed at {milis}')

total_milis = 0
pygame.init()
window = pygame.display.set_mode((500, 225))

pygame.display.set_caption("Stopwatch Game")
clock = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                handler_stop(total_milis)
        elif event.type == pygame.QUIT:
            running = False
        
    
    clock.tick(100)
    
    total_milis += clock.get_time()
    window.fill((0, 0, 0))
    draw_time(total_milis)
    draw_button()
    pygame.display.flip()

pygame.quit()
    