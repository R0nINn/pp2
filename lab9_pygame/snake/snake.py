import pygame,sys
import time,random
from pygame.locals import*

pygame.init()
# fps
FPS = 5
FramePerSec = pygame.time.Clock()

# colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (230,200,0)

# info
SCORE = 0

# setting up screen
w,h = 800,800
BLOCK_size = 50
surf = pygame.display.set_mode((w,h))
pygame.display.set_caption('snakehenze')

# fonts
font = pygame.font.SysFont('Verdana',60)


# creating cnake class
class Snake():
    def __init__(self):
        self.x, self.y = BLOCK_size , BLOCK_size
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x , self.y , BLOCK_size , BLOCK_size)
        self.body = [pygame.Rect(self.x-BLOCK_size , self.y , BLOCK_size , BLOCK_size)]
        self.dead = False
    def update(self):
        global apple
        
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, w) or self.head.y not in range(0, h):
                self.dead = True
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x , self.body[i].y = self.body[i+1].x , self.body[i+1].y
        self.head.x += self.xdir*BLOCK_size
        self.head.y += self.ydir*BLOCK_size
        self.body.remove(self.head)              
        
# creating apple class
class Apple():
    def __init__(self):
        self.foodx = int(random.randint(0,w)//50)*50
        self.foody = int(random.randint(0,h)//50)*50
        self.rect = pygame.Rect(self.foodx,self.foody,BLOCK_size,BLOCK_size)
    def update(self):
        pygame.draw.rect(surf,RED,self.rect)
class GoldApple():
    def __init__(self):
        self.foodx = int(random.randint(0,w)//50)*50
        self.foody = int(random.randint(0,h)//50)*50
        self.rect = pygame.Rect(self.foodx,self.foody,BLOCK_size,BLOCK_size)
        self.weight = random.randint(5,10)
    def update(self):
        pygame.draw.rect(surf,'yellow',self.rect)

# function to  draw grid
def Drawgrid():
    for x in range(0,w,BLOCK_size):
        for y in range(0,h,BLOCK_size):
            rect = pygame.Rect(x,y,BLOCK_size,BLOCK_size)
            pygame.draw.rect(surf,(134,136,138),rect,1)

Drawgrid()

snake = Snake()
apple = Apple()
gold = GoldApple()

apples = (apple,gold)
choice = random.choice(apples)
new_food = pygame.USEREVENT + 0
pygame.time.set_timer(new_food ,10000)
weight_minus = pygame.USEREVENT + 1
pygame.time.set_timer(weight_minus,2000)

food_in_body = False
if (apple.foodx and apple.foody in snake.body):
    food_in_body = True

while True:  
    if snake.dead == True:
        pygame.quit()
        sys.exit()
    
    while food_in_body:
        choice.update()
    
    for event in pygame.event.get():
        if event.type == new_food:
            choice = random.choice(apples)
            choice.update()
        if event.type == weight_minus:
            gold.weight -= 1
            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snake.xdir!= 1:
                    snake.xdir = -1
                snake.ydir = 0
        
            elif event.key == pygame.K_RIGHT:
                if snake.xdir!=-1:
                    snake.xdir = 1
                snake.ydir = 0
        
            elif event.key == pygame.K_DOWN:
                if snake.ydir !=-1:    
                    snake.ydir = 1
                snake.xdir = 0
        
            elif event.key == pygame.K_UP:
                if snake.ydir!=1:    
                    snake.ydir = -1
                snake.xdir = 0
    
    snake.update()
    surf.fill(BLACK)
    Drawgrid()
    choice.update()
    
    scoreboard = font.render(str(SCORE),True,WHITE)
    surf.blit(scoreboard,(10,10))

# to draw snake's boady and head
    pygame.draw.rect(surf,GREEN,snake.head)
    for square in snake.body:
        pygame.draw.rect(surf,GREEN,square)

# cheching for eating a food
    if snake.head.x ==apple.foodx and snake.head.y ==apple.foody:
        snake.body.append(pygame.Rect(square.x,square.y,BLOCK_size,BLOCK_size))
        SCORE+=1
        choice = random.choice(apples)
        pygame.time.set_timer(new_food ,10000)
        if ((len(snake.body)))%3==0:
            FPS = FPS + 2
    if snake.head.x ==gold.foodx and snake.head.y ==gold.foody:
        snake.body.append(pygame.Rect(square.x,square.y,BLOCK_size,BLOCK_size))
        SCORE+=gold.weight
        choice = random.choice(apples)
        pygame.time.set_timer(new_food ,10000)
        if ((len(snake.body)))%3==0:
            FPS = FPS + 2
    
       
    pygame.display.update()
    FramePerSec.tick(FPS)   