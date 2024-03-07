# Demo #1a,2a,3a: A Collection Of Useful Sprite Classes

import pygame
import random


class Circle(pygame.sprite.Sprite):
    '''Our Circle class inherits from the Sprite class'''

    def __init__(self):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and rect attributes for the circle
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25, 0)
        self.rect = self.image.get_rect()

    def update(self):
        # Move the center of the circle to where the mouse is pointing
        self.rect.center = pygame.mouse.get_pos()


class Label(pygame.sprite.Sprite):
    def __init__(self, message, x_y_center):
        pygame.sprite.Sprite.__init__(self)
        self.__font = pygame.font.SysFont("None", 30)
        self.__text = message
        self.__center = x_y_center

    def set_text(self, message):
        self.__text = message

    def update(self):
        self.image = self.__font.render(self.__text, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.__center


class Brick(pygame.sprite.Sprite):
    '''Our Bricks class inherits from the Sprite class'''

    def __init__(self, screen):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and rect attributes for the bricks
        self.image = pygame.image.load("bricks.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())
