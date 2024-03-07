"""
Author: Christine Wei
Date: May 11, 2023,
Description: Music sound effects modified version
"""

# I - Import and Initialize
import pygame
pygame.init()
pygame.mixer.init()


def main():
    """This function defines the 'mainline logic' for our game."""

    # Display
    screen = pygame.display.set_mode ((640, 480))
    pygame.display.set_caption("move a my_image")

    # Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0)) # yellow background
    boing = pygame.mixer.Sound("boing.wav")
    boing.set_volume(0.5)

    # Image that will replace red my_image
    my_image = pygame.image.load("grandpa.jpg")

    # set up some my_image variables
    my_image_x = 0
    my_image_y = 50
    my_image_dir = 5

    # ACTION
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
                pygame.mixer.music.fadeout(2000)
                keepGoing = False

        # modify my_image value
        my_image_x += my_image_dir

        # check boundaries and change direction if needed
        if (my_image_x < 0) or (my_image_x > screen.get_width()-20):
            boing.play()
            my_image_dir = -my_image_dir

        # Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(my_image, (my_image_x, my_image_y))
        pygame.display.flip()

    # Close the game window
    pygame.quit()


# Call the main function
main()
