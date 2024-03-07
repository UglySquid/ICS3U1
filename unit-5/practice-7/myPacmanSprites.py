"""
Author: Christine Wei
Date: May 19, 2023,
Description: Sprites Module
"""

import pygame
import random


class Cherry(pygame.sprite.Sprite):
    """ Our Cherry class inherits from the Sprite class"""

    def __init__(self, screen):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and rect attributes for the bricks
        self.image = pygame.image.load("cherries.gif")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())
        self.dx = random.randrange(-10, 10)
        self.dy = random.randrange(-10, 10)
        self.__screen = screen


class Pacman(pygame.sprite.Sprite):
    """ Our Cherry class inherits from the Sprite class"""

    def __init__(self, screen):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and rect attributes for the bricks
        self.__right = pygame.image.load("pacman-right.gif")
        self.__left = pygame.image.load("pacman-left.gif")
        self.__up = pygame.image.load("pacman-up.gif")
        self.__down = pygame.image.load("pacman-down.gif")

        self.image = self.__right

        self.rect = self.image.get_rect()
        self.rect.centerx = (int(screen.get_width())/2)
        self.rect.centery = (int(screen.get_height())/2)
        self.__dx = 5
        self.__dy = 0
        self.__screen = screen

    def go_left(self):
        self.image = self.__left
        self.__dx = -5
        self.__dy = 0
        self.rect.left += self.__dx
        self.rect.top += self.__dy

    def go_right(self):
        self.image = self.__right
        self.__dx = 5
        self.__dy = 0
        self.rect.left += self.__dx
        self.rect.top += self.__dy

    def go_up(self):
        self.image = self.__up
        self.__dx = 0
        self.__dy = -5
        self.rect.left += self.__dx
        self.rect.top += self.__dy

    def go_down(self):
        self.image = self.__down
        self.__dx = 0
        self.__dy = 5
        self.rect.left += self.__dx
        self.rect.top += self.__dy

    def update(self):
        if (self.image == self.__right) and (self.rect.centerx > self.__screen.get_width()):
            self.rect.centerx = 0
        if (self.image == self.__left) and (self.rect.centerx < 0):
            self.rect.centerx = self.__screen.get_width()
        if (self.image == self.__up) and (self.rect.centery < 0):
            self.rect.centery = self.__screen.get_height()
        if (self.image == self.__down) and (self.rect.centery > self.__screen.get_height()):
            self.rect.centery = 0
