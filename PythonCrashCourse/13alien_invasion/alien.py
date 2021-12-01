import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """represent an alien"""
    def __init__(self, ai_settings, screen):
        """initialize the alien, and set its position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # load image of alien, and set its attribution "rect"
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # each alien was put in the upper left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store the accurate position of the alien
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien at the specified location"""
        self.screen.blit(self.image, self.rect)