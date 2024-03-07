"""
Author: Christine Wei
Date: May 11, 2023,
Description: Music sound effects modified version with background music
"""

# I - Import and Initialize
import pygame
pygame.init()
pygame.mixer.init()


class Box(pygame.sprite.Sprite):
    """Our Box class inherits from the Sprite class"""

    def __init__(self, colour, center_x_y, display):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image attribute for our Box sprite
        self.image = pygame.Surface((25, 25))
        self.image = self.image.convert()
        self.image.fill(colour)

        # Set the rect attribute for our Box sprite
        self.rect = self.image.get_rect()
        self.rect.left = center_x_y[0]
        self.rect.top = center_x_y[1]
        self.__directiony = 10
        self.__directionx = 10

    def update(self, display):
        self.rect.left += self.__directionx
        self.rect.top += self.__directiony
        if (self.rect.left < 0) or (self.rect.right > display.get_width()):
            self.__directionx = -self.__directionx
        if (self.rect.top < 0) or (self.rect.bottom > display.get_height()):
            self.__directiony = -self.__directiony


def main():
    """This function defines the 'mainline logic' for our game."""

    # Display
    screen = pygame.display.set_mode ((640, 480))
    pygame.display.set_caption("move a my_image")

    # Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0)) # yellow background
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
    boing = pygame.mixer.Sound("boing.wav")
    boing.set_volume(0.5)

    # Image that will replace red my_image
    my_image = pygame.image.load("grandpa.jpg")
    box1 = Box((0, 255, 255), (0, 0), screen)
    box2 = Box((70, 70, 255), (screen.get_width()-25, screen.get_height()-25), screen)
    box3 = Box((255, 70, 0), (0, screen.get_height()-25), screen)
    allSprites = pygame.sprite.Group(box1, box2, box3)

    # set up some my_image variables
    my_image_x = 0
    my_image_y = 0
    my_image_dir_x = 5
    my_image_dir_y = 5

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
        my_image_x += my_image_dir_x
        my_image_y += my_image_dir_y

        # check boundaries and change direction if needed
        if (my_image_x < 0) or (my_image_x > screen.get_width()-450):
            boing.play()
            my_image_dir_x = -my_image_dir_x

        if (my_image_y < 0) or (my_image_x > screen.get_height()-318):
            boing.play()
            my_image_dir_y = -my_image_dir_y

        # Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(my_image, (my_image_x, my_image_y))
        allSprites.clear(screen, background)
        allSprites.update(screen)
        allSprites.draw(screen)
        pygame.display.flip()

    # Close the game window
    pygame.quit()


# Call the main function
main()
