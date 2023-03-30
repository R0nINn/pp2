import pygame

pygame.init()

w = 1000
h = 700

screen = pygame.display.set_mode((w , h))
rectangle = screen.get_rect()
done = False

x = 150
y = 150
radius = 30

fps = pygame.time.Clock()

while not done:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > rectangle.top + radius : y-=4
    if pressed[pygame.K_DOWN] and y < rectangle.bottom - radius : y+=4
    if pressed[pygame.K_LEFT] and x > rectangle.left + radius : x-=4
    if pressed[pygame.K_RIGHT]and x <rectangle.right -radius : x+=4
    
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),center=(x,y),radius=(radius),width=(2))
    fps.tick (120)
    
    pygame.display.update()
    

    
