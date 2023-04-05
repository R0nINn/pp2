import pygame
import sys
from pygame.locals import*
import time,random

# initializing
pygame.init()

# FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, WHITE)

# setting up screen
w = 400
h = 600
SCORE = 0
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Racer')

background = pygame.image.load('racer/materials/AnimatedStreet.png')


# creating class for Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racer\materials\Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,w-40) , 0)
    def move(self):
        self.rect.move_ip(0,10)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30,w-30) , 0)

# creating class for Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racer\materials\Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 0 :
            if pressed[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < w :
            if pressed[K_RIGHT]:
                self.rect.move_ip(5,0)

P1 = Player()
E1 = Enemy()

# Creating group of sprites
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    scores = font_small.render(str(SCORE),True,BLACK)
    screen.blit(scores,(10,10))
    screen.fill(WHITE)
    
    # #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    
    # to check for collision
    if pygame.sprite.spritecollideany(P1,enemies):
        screen.fill(BLACK)
        screen.blit(game_over,(30,250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(3)
        pygame.quit()
        sys.exit()
                
    pygame.display.update()
    FramePerSec.tick(FPS)  