"""
Author: Christine Wei
Date: May 16, 2023,
Description: Bricks Image Sprite
"""

# I - Import and Initialize
import newSprites
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))


def main():
    """This function defines the 'mainline logic' for our game."""

    # Display
    pygame.display.set_caption("Lots Of Bricks")

    # Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # Create 10 random bricks
    bricks = []
    for i in range(10):
        bricks.append(newSprites.Brick(screen))

    allSprites = pygame.sprite.Group(bricks)

    # ACTION

    # Assign
    keepGoing = True
    clock = pygame.time.Clock()

    # Loop
    while keepGoing:

        # Time
        clock.tick(30)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()

    # Close the game window
    pygame.quit()


# Call the main function
main()
