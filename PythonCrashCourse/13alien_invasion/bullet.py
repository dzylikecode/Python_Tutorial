import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Manage the launch of a bullet by ship"""
    def __init__(self, ai_settings, screen, ship):
        """create a new bullet in the position of a ship"""
        super(Bullet, self).__init__()
        self.screen = screen
        # create a new rect representing the bullet at (0, 0),
        # and then place it in the right place
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Use the decimal to store the location of the bullets
        self.y = float(ship.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moving up the bullet"""
        # update the decimal representing the position of the bullet
        self.y -= self.speed_factor
        # update the rect which is the real position of the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw on the screen shot"""
        pygame.draw.rect(self.screen, self.color, self.rect)
