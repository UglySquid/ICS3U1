# Demo #1b: Mouse-Controlled Circle Sprite Demo

# I - Import and Initialize
import pygame
import newSprites

pygame.init()
screen = pygame.display.set_mode((640, 480))


def main():
    """This function defines the 'mainline logic' for our game."""

    # Display
    pygame.display.set_caption("Move the circle with the mouse!")

    # Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # Create a Circle sprite object
    circle = newSprites.Circle(50, 250, 150)
    allSprites = pygame.sprite.Group(circle)

    # ACTION

    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True

    # Hide the mouse pointer
    pygame.mouse.set_visible(False)

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

    # Un-hide mouse pointer
    pygame.mouse.set_visible(True)

    # Close the game window
    pygame.quit()


# Call the main function
main()
