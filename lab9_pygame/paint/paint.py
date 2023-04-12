import pygame,sys
from pygame import*

pygame.init()

# Fps
fps = 120
FramePerSec = pygame.time.Clock()

# default values before starting drawing
brush_size = 0
active_color = 'white'
painting = []
size = (0,0)
position = (0,0)
shape = ''

# screen info
WIDTH = 800
HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))

# function for menu to get brush and colors for drawing
def draw_menu():
    
    # drawing menu
    pygame.draw.rect(DISPLAYSURF,'gray',[0,0,WIDTH,70])
    pygame.draw.line(DISPLAYSURF,'black',[0,70],[WIDTH,70])
    
    brush = pygame.draw.rect(DISPLAYSURF,'black',[10,10,50,50])
    pygame.draw.circle(DISPLAYSURF,'white',(35,35),7)
    
    circle_select = pygame.draw.rect(DISPLAYSURF,'black',[62,10,50,50])
    pygame.draw.circle(DISPLAYSURF,'white',(87,35),17,2)
    
    rectangle_select = pygame.draw.rect(DISPLAYSURF,'black',[114,10,50,50])
    pygame.draw.rect(DISPLAYSURF,'white',[122,18,34,34])
    
    # menu for colors
    blue = pygame.draw.rect(DISPLAYSURF,(0,0,255),[WIDTH-35,10,25,25])
    red = pygame.draw.rect(DISPLAYSURF,(255,0,0),[WIDTH-60,10,25,25])
    green = pygame.draw.rect(DISPLAYSURF,(0,255,0),[WIDTH-35,35,25,25])
    black = pygame.draw.rect(DISPLAYSURF,(0,0,0),[WIDTH-60,35,25,25])
    white = pygame.draw.rect(DISPLAYSURF,(255,255,255),[WIDTH-85,10,25,25])
    yellow = pygame.draw.rect(DISPLAYSURF,(255,255,30),[WIDTH-85,35,25,25])
    pygame.draw.rect(DISPLAYSURF,'black',[WIDTH-86,9,77,52],1)
    rgb_list = [(0,0,255),(255,0,0),(0,255,0),(0,0,0),(255,255,255),(255,255,30)]
    
    color_list = [blue, red, green, black,white,yellow]
    return brush,color_list,rgb_list,circle_select,rectangle_select

# function for painting
def drawing(painting):
    for i in range(len(painting)):
        pygame.draw.circle(DISPLAYSURF,painting[i][0],painting[i][1],painting[i][2])
    
pygame.display.set_caption('Paint!')

while True:
    
    # getting position of mouse
    mouse_pos = pygame.mouse.get_pos()
    # check for left click of the mouse
    left_click = pygame.mouse.get_pressed()[0]
    
    # check if user hit left click and pos of mouse in drawing area then getting values to draw
    if left_click and mouse_pos[1] > 70:
        painting.append((active_color,mouse_pos,brush_size))
    # draw after getting values   
    drawing(painting)
    
    # to draw only in user menu
    if mouse_pos[1] > 70:
        pygame.draw.circle(DISPLAYSURF,active_color, mouse_pos , brush_size)
    # to get exactly same returned values,in correct order
    brush,colors,rgbs,circle,rectangle = draw_menu()
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
         # Check if the user has pressed the left mouse button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse_pos[1] > 70:
            # Get the position of the mouse
            position = event.pos

        # Check if the user has released the left mouse button
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Get the size of the shape
            size = (event.pos[0] - position[0], event.pos[1] - position[1]) 
    # to check that user selected brush
        if event.type == pygame.MOUSEBUTTONDOWN:
            if brush.collidepoint(event.pos):
                brush_size = 10
                shape = ''
            if circle.collidepoint(event.pos):
                brush_size = 0
                shape = 'circle'
            if rectangle.collidepoint(event.pos):
                brush_size = 0
                shape = 'rectangle'
    # to check that user selected what color he/she wanted    
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
       
        # Draw the shape on the screen
            # if shape == "rectangle":
            #     pygame.draw.rect(DISPLAYSURF, active_color, (position, size), 1)
            # elif shape == "circle":
            #     pygame.draw.circle(DISPLAYSURF, active_color, position, max(abs(size[0]), abs(size[1])), 1)
        
    # Draw the shape on the screen
    if shape == "rectangle":
        pygame.draw.rect(DISPLAYSURF, active_color, (position, size), 1)
    elif shape == "circle":
        pygame.draw.circle(DISPLAYSURF, active_color, position, max(abs(size[0]), abs(size[1])), 1)
    
    pygame.display.update()
    FramePerSec.tick(fps)
    DISPLAYSURF.fill('white')