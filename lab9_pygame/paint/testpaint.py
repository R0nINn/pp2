import pygame

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode((800, 600))

# Set the caption of the window
pygame.display.set_caption("Draw Shapes")

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set the default shape to draw
shape = "rectangle"

# Set the default position of the shape
position = (0, 0)

# Set the default size of the shape
size = (0, 0)

# Set the default color of the shape
color = black

# Set the default thickness of the shape
thickness = 1

# Create a variable to keep the game running
running = True

# Main game loop
while running:
    # Loop through all the events
    for event in pygame.event.get():
        # Check if the user has closed the window
        if event.type == pygame.QUIT:
            running = False

        # Check if the user has pressed a key
        if event.type == pygame.KEYDOWN:
            # Check if the user has pressed the 'r' key to draw a rectangle
            if event.key == pygame.K_r:
                shape = "rectangle"
                print("Rectangle mode activated")
            # Check if the user has pressed the 'c' key to draw a circle
            elif event.key == pygame.K_c:
                shape = "circle"
                print("Circle mode activated")

        # Check if the user has pressed the left mouse button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the position of the mouse
            position = event.pos

        # Check if the user has released the left mouse button
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Get the size of the shape
            size = (event.pos[0] - position[0], event.pos[1] - position[1])
            # Draw the shape on the screen
            if shape == "rectangle":
                pygame.draw.rect(screen, color, (position, size), thickness)
            elif shape == "circle":
                pygame.draw.circle(screen, color, position, max(abs(size[0]), abs(size[1])), thickness)

    # Fill the screen with white
    screen.fill(white)

    # Draw the shape on the screen
    if shape == "rectangle":
        pygame.draw.rect(screen, color, (position, size), thickness)
    elif shape == "circle":
        pygame.draw.circle(screen, color, position, max(abs(size[0]), abs(size[1])), thickness)

    # Update the display
    pygame.display.update()

    
# Quit Pygame
pygame.quit()