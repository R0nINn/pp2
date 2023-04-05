import pygame
from pygame.locals import *
import sys
import time
import random

pygame.init()

game_over = False

frame_per_sec = pygame.time.Clock()
FPS = 10

# colors
RED = (255,20,20)
BLUE = (20,20,255)
GREEN = (3,200,5)
BLACK = (0,0,0)
ORANGE = (255,165,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

# info(score level and speed)
LVL = 1
SCORE = 0
SPEED = 10

# font = pygame.font.SysFont("comicsansms",20)
# text_score = font.render('your score:' + str(SCORE),True,(GREEN))

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SNAKEHENSE")
rect = screen.get_rect()

# coordinates of snake and food
x = 40
y = 40
x_changed = 0
y_changed = 0

foodx = round(random.randint(0,screen_width-x)/10)*10
foody = round(random.randint(0,screen_height-y)/10)*10

body_list = [(x,y)]

# GAME_OVER screen
word = pygame.font.SysFont("comicsansms",70)
def end(word,color):
    message = font.render(word,True,color)
    screen.fill(BLACK)
    screen.blit(message,[350,260])
    

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over =True
            
            
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > rect.top :
            if y_changed!=SPEED:
                y_changed = -SPEED 
                x_changed = 0    
        if pressed[pygame.K_DOWN] and y < rect.bottom:
            if y_changed!=SPEED:
                y_changed = +SPEED   
                x_changed = 0    
        if pressed[pygame.K_LEFT] and x > rect.left :
            if x_changed!=SPEED:
                x_changed = -SPEED       
                y_changed = 0
        if pressed[pygame.K_RIGHT] and x < rect.right : 
            if x_changed!=SPEED:
                x_changed = +SPEED
                y_changed = 0
        
    if x > rect.width or x < 0 or y > rect.height or y < 0 :
        game_over = True
    
    x+=x_changed
    y+=y_changed

# update score
    font = pygame.font.SysFont("comicsansms",20)
    text_score = font.render('your score:' + str(SCORE),True,(GREEN))
# when u eat food to append +1 for body
    body_list.append((x,y))
    if x == foodx and y == foody :
        SCORE+=1
        while ((foodx,foody) in body_list):
            foodx = round(random.randint(0,screen_width-x)/10)*10
            foody = round(random.randint(0,screen_height-y)/10)*10
    else:
        del body_list[0]
    
    screen.fill(ORANGE)
    
    
    pygame.draw.rect(screen,BLUE,pygame.Rect(foodx,foody,10,10))
    for i,j in body_list:
        pygame.draw.rect(screen,WHITE,pygame.Rect(i,j,10,10))
    screen.blit(text_score,(5,5))
    pygame.display.update()
    frame_per_sec.tick(FPS)

end("GAME OVER",WHITE)
pygame.display.update()
time.sleep(3)
pygame.quit()
sys.exit