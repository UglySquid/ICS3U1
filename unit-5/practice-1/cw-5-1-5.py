"""
Author: Christine Wei
Date: May 10, 2023,
Description: Yellow background with red square moving from right to left of the screen
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

# yellow background
background.fill((255, 255, 0))

# make a red 25 x 25 box
box = pygame.Surface((25, 25))
box = box.convert()
box.fill((255, 0, 0))

# set up some box variables
box_x = 640
box_y = 200


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

    # modify box value
    box_x -= 5

    # check boundaries
    if box_x < 0:
        box_x = 640

    # Refresh screen
    screen.blit(background, (0, 0))
    screen.blit(box, (box_x, box_y))
    pygame.display.flip()

# Close the game window
pygame.quit()