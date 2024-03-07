"""
Author: Christine Wei
Date: May 16, 2023,
Description: Sprites library
"""

import pygame
import random


class Circle(pygame.sprite.Sprite):
    """Our Circle class inherits from the Sprite class"""
    def __init__(self, red_val, blue_val, green_val):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and rect attributes for the circle
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, (red_val, green_val, blue_val), (25, 25), 25, 0)
        self.rect = self.image.get_rect()

    def update(self):
        # Move the center of the circle to where the mouse is pointing
        self.rect.center = pygame.mouse.get_pos()


class Label(pygame.sprite.Sprite):
    """Our Label class inherits from the Sprite class"""
    def __init__(self, message, x_y_center, colour, font_name, size):
        pygame.sprite.Sprite.__init__(self)
        self.__font = pygame.font.SysFont(font_name, size)
        self.__text = message
        self.__center = x_y_center
        self.__colour = colour

    def set_text(self, message):
        self.__text = message

    def update(self):
        self.image = self.__font.render(self.__text, True, self.__colour)
        self.rect = self.image.get_rect()
        self.rect.center = self.__center


class Brick(pygame.sprite.Sprite):
    """ Our Bricks class inherits from the Sprite class"""

    def __init__(self, screen):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and rect attributes for the bricks
        self.image = pygame.image.load("bricks.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())
        self.dx = random.randrange(-10, 10)
        self.dy = random.randrange(-10, 10)
        self.__screen = screen

    def update(self):
        self.rect.left += self.dx
        self.rect.top += self.dy

        if (self.rect.left < 0) or (self.rect.right > self.__screen.get_width()):
            self.dx = -self.dx
        if (self.rect.top < 0) or (self.rect.bottom > self.__screen.get_height()):
            self.dy = -self.dy

