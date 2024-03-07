"""
Author: Christine Wei
Date: May 11, 2023,
Description: Christine's Self Portrait
"""

import pygame
import pygame.draw
pygame.init()

# Set colours
white = (255, 255, 255)
black = (0, 0, 0)
skin_tone = (241, 194, 125)
dark_skin_tone = (221, 174, 105)
lip_color = (194, 109, 89)


def main():
    """This function defines the 'mainline logic' for our game."""
    # D - Display configuration
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Christine's Self Portrait")

    # E - Entities (just background for now)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    # A - Action (broken into ALTER steps)
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True

    # blit Background to surface
    screen.blit(background, (0, 0))

    # L - Loop
    while keepGoing:
        # T - Timer to set frame rate
        clock.tick(30)

        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        draw_me(screen)

        # R - Refresh display
        pygame.display.update()

    # Close the game window
    pygame.quit()


def draw_me(surface):
    # Ears
    pygame.draw.polygon(surface, dark_skin_tone, ((225, 400), (200, 400), (150, 375), (125, 400), (175, 475), (225, 475)))
    pygame.draw.polygon(surface, dark_skin_tone, ((475, 400), (500, 400), (550, 375), (575, 400), (525, 475), (475, 475)))

    # Neck
    pygame.draw.polygon(surface, dark_skin_tone, ((275, 575), (250, 700), (450, 700), (425, 575)))

    # Hair behind
    pygame.draw.polygon(surface, black, ((200, 475), (175, 550), (250, 550), (225, 475)))
    pygame.draw.polygon(surface, black, ((500, 475), (525, 550), (450, 550), (450, 475)))

    # Face
    pygame.draw.polygon(surface, skin_tone, ((175, 300), (525, 300), (475, 550), (375, 600), (325, 600), (225, 550)))

    # Hair
    pygame.draw.polygon(surface, black, (
                    (350, 225), (300, 200), (150, 250), (125, 325), (150, 375), (200, 400), (350, 300)))
    pygame.draw.polygon(surface, black, (
                    (350, 225), (400, 200), (550, 250), (575, 325), (550, 375), (500, 400), (350, 300)))

    # Eyes
    pygame.draw.circle(surface, black, (275, 450), 25, 0)
    pygame.draw.circle(surface, black, (425, 450), 25, 0)

    # Mouth
    pygame.draw.polygon(surface, lip_color, ((275, 525), (425, 525), (375, 550), (325, 550)))


# Call the main function
main()
