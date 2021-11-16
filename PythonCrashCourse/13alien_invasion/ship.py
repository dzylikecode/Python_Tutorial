"""
初始化船
"""

import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """initialize ship with the given screen """
        self.screen = screen
        self.ai_settings = ai_settings
        # load the image of the ship
        file_name = 'images/ship.bmp'
        try:
            self.image = pygame.image.load(file_name)
        except FileNotFoundError as e:
            print("Could not load file {}".format(file_name))
            exit()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Every ship in the middle of the bottom of the screen
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        # store floating point number  in the shuttle's property
        self.center = float(self.rect.centerx)
        # flag of the movement
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the position of the ship according to the current state"""
        # Add the border judgment
        screen_right = self.screen_rect.right
        screen_left = self.screen_rect.left
        left = self.rect.left
        right = self.rect.right
        if self.moving_right and right < screen_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and left > screen_left:
            self.center -= self.ai_settings.ship_speed_factor
        # update the object 'rect' according to the variable 'self.center'
        self.rect.centerx = self.center

    def blitme(self):
        """blit the ship in the specified location"""
        self.screen.blit(self.image, self.rect)
