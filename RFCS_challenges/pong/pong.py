import pygame
from pygame.locals import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, player_int):
        super(Player, self).__init__()
        self.max_y = pygame.display.Info().current_h
        self.max_x = pygame.display.Info().current_w

        self.surface = pygame.image.load('paddle.png').convert()
        self.surface.set_colorkey((255, 255, 255))
        self.position = self.surface.get_rect(center=(x_pos, 100))
        self.player_int = player_int
        self.score = 0
        
    def update(self, pressed_keys):
        self.control(pressed_keys)
        self.contain()
    
    def control(self, pressed_keys):
        if self.player_int == 2:
            if pressed_keys[K_UP]:
                self.position.move_ip(0, -5)
            if pressed_keys[K_DOWN]:
                self.position.move_ip(0, 5)
        if self.player_int == 1:
            if pressed_keys[K_w]:
                self.position.move_ip(0, -5)
            if pressed_keys[K_s]:
                self.position.move_ip(0, 5)

    def contain(self):    
        if self.position.midtop[1] < 0:
            self.position.move_ip(0, 10)
        if self.position.midbottom[1] > self.max_y:
            self.position.move_ip(0, -10)
    
    def score_handler(self):
        self.score += 1

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.max_y = pygame.display.Info().current_h
        self.max_x = pygame.display.Info().current_w

        self.surface = pygame.image.load('circle.png').convert()
        self.surface.set_colorkey((255, 255, 255))
        self.position = self.surface.get_rect(center=(self.max_x/2, self.max_y/2))
        self.velocity = [random.randint(-11, 11), random.randint(-11, -1)]

    def update(self, pressed_keys):
        self.control(pressed_keys)
        self.contain()
        self.position.move_ip(self.velocity)
    
    def control(self, pressed_keys):
        if pressed_keys[K_KP_PLUS]:
            self.velocity[0] += 1
        if pressed_keys[K_KP_MINUS]:
            self.velocity[0] += -1

    def contain(self):
        if self.position.midleft[0] < 0 or self.position.midright[0] > self.max_x:
            self.velocity[0] = -self.velocity[0]
        if self.position.midtop[1] < 0 or self.position.midbottom[1] > self.max_y:
            self.velocity[1] = -self.velocity[1] 

    def bounce_handler(self):
            self.velocity[0] = -self.velocity[0]                

    def respawn(self):
        self.__init__()

def listen_quit():
    #listen for quit
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
        elif event.type == QUIT:
            return False
    return True

def draw_scores(player1, player2):
    main_window = pygame.display.get_surface()
    
    font = pygame.font.Font(None, 150)
    message = f'{player1.score}  to  {player2.score}'
    text = font.render(message, True, (255, 255, 0))

    main_window.blit(text, [main_window.get_rect().width/2-150, 50])

def watch_score(player1, player2, ball):
    if ball.position.midleft[0] < 0:
        player1.score_handler()
        ball.respawn()
        
    if ball.position.midright[0] > main_window.get_width():
        player2.score_handler()
        ball.respawn()

pygame.init()
main_window = pygame.display.set_mode((1200, 900))

player1 = Player(30, 1)
player2 = Player(1180, 2)
ball = Ball()
all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2, ball)

running = True
clock = pygame.time.Clock()

while running:
    
    running = listen_quit()
    clock.tick(60)

    pressed_keys = pygame.key.get_pressed()
    main_window.fill((0, 0, 0))

    #bounce off of paddle
    paddle_collision = ball.position.collidelist([player1.position, player2.position])
    if paddle_collision >= 0:
        ball.bounce_handler()

    for entity in all_sprites:
        entity.update(pressed_keys)
        main_window.blit(entity.surface, entity.position)
    
    watch_score(player1, player2, ball)
    draw_scores(player1, player2)
    pygame.display.flip()

    