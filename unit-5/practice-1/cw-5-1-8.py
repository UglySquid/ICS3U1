"""
Author: Christine Wei
Date: May 10, 2023,
Description: White background with 4 square moving from all four directions
"""

# Initialize
import pygame
pygame.init()

# Display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("move a box")

# Entities
background = pygame.Surface(screen.get_size())
background = background.convert()

# White background
background.fill((255, 255, 255))

# make a green 25 x 25 box
box_green = pygame.Surface((25, 25))
box_green = box_green.convert()
box_green.fill((0, 255, 0))

# make a pink 25 x 25 box
box_pink = pygame.Surface((25, 25))
box_pink = box_pink.convert()
box_pink.fill((255, 192, 203))

# make a red 25 x 25 box
box_red = pygame.Surface((25, 25))
box_red = box_red.convert()
box_red.fill((255, 0, 0))

# make a blue 25 x 25 box
box_blue = pygame.Surface((25, 25))
box_blue = box_blue.convert()
box_blue.fill((0, 0, 255))

# set up some green box variables
box_green_x = screen.get_width()/2
box_green_y = 0

# set up some pink box variables
box_pink_x = screen.get_width()
box_pink_y = screen.get_height()/2

# set up some red box variables
box_red_x = screen.get_width()/2
box_red_y = screen.get_height()

# set up some blue box variables
box_blue_x = 0
box_blue_y = screen.get_height()/2


# ACTION: ALTER
# Assign
clock = pygame.time.Clock()
keepGoing = True
# Loop
while keepGoing:
    # Time
    clock.tick(30)
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    # modify green box value
    box_green_y += 5
    # check green boundaries
    if box_green_y > screen.get_height():
        box_green_y = 0

    # modify pink box value
    box_pink_x -= 5
    # check pink box boundaries
    if box_pink_x < 0:
        box_pink_x = screen.get_width()

    # modify red box value
    box_red_y -= 5
    # check red box boundaries
    if box_red_y < 0:
        box_red_y = screen.get_height()

    # modify blue box value
    box_blue_x += 5
    # check blue box boundaries
    if box_blue_x > screen.get_width():
        box_blue_x = 0

    # Refresh screen
    screen.blit(background, (0, 0))
    screen.blit(box_green, (box_green_x, box_green_y))
    screen.blit(box_pink, (box_pink_x, box_pink_y))
    screen.blit(box_red, (box_red_x, box_red_y))
    screen.blit(box_blue, (box_blue_x, box_blue_y))
    pygame.display.flip()

# Close the game window
pygame.quit()
