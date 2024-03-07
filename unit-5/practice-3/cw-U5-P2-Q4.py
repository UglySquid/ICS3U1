"""
Author: Christine Wei
Date: May 11, 2023,
Description: Christine's Self Portrait
"""

import pygame
import pygame.draw
pygame.init()

face = pygame.image.load("portrait.png")
my_font = pygame.font.SysFont("Arial", 100)


def main():
    """This function defines the 'mainline logic' for our game."""
    # D - Display configuration
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Christine's Self Portrait")

    # E - Entities (just background for now)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    text = my_font.render("Christine Wei!", 1, (0, 0, 0))

    # A - Action (broken into ALTER steps)
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True

    # L - Loop
    while keepGoing:
        # T - Timer to set frame rate
        clock.tick(30)

        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        # R - Refresh display
        screen.blit(background, (0, 0))
        screen.blit(face, (0, 0))
        screen.blit(text, (50, 50))

        pygame.display.update()

    # Save the background surface as a PNG file
    pygame.image.save(screen, "new-portrait.gif")

    # Close the game window
    pygame.quit()


# Call the main function
main()
