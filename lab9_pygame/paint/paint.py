import pygame,sys
from pygame import*

pygame.init()

fps = 300
FramePerSec = pygame.time.Clock()

brush_size = 0
active_color = 'white'
painting = []

WIDTH = 800
HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))

def draw_menu():
    pygame.draw.rect(DISPLAYSURF,'gray',[0,0,WIDTH,70])
    brush = pygame.draw.rect(DISPLAYSURF,'black',[10,10,50,50])
    pygame.draw.circle(DISPLAYSURF,'white',(35,35),7)
    
    blue = pygame.draw.rect(DISPLAYSURF,(0,0,255),[WIDTH-35,10,25,25])
    red = pygame.draw.rect(DISPLAYSURF,(255,0,0),[WIDTH-60,10,25,25])
    green = pygame.draw.rect(DISPLAYSURF,(0,255,0),[WIDTH-35,35,25,25])
    black = pygame.draw.rect(DISPLAYSURF,(0,0,0),[WIDTH-60,35,25,25])

    rgb_list = [(0,0,255),(255,0,0),(0,255,0),(0,0,0)]
    
    color_list = [blue, red, green, black]
    return brush,color_list,rgb_list

def drawing(painting):
    for i in range(len(painting)):
        pygame.draw.circle(DISPLAYSURF,painting[i][0],painting[i][1],painting[i][2])
    
pygame.display.set_caption('Paint!')

while True:
    
    mouse_pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    
    if left_click and mouse_pos[1] > 70:
        painting.append((active_color,mouse_pos,brush_size))
        
    drawing(painting)
    
    if mouse_pos[1] > 70:
        pygame.draw.circle(DISPLAYSURF,active_color, mouse_pos , brush_size)
    
    brush,colors,rgbs = draw_menu()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if brush.collidepoint(event.pos):
                brush_size = 10
        
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
    
    pygame.display.update()
    FramePerSec.tick(fps)
    DISPLAYSURF.fill('white')