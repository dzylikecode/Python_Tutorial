import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
    """
    the basic framework of the game
    """
    # initialize the game
    pygame.init()
    # get the settings
    ai_settings = Settings()
    # create a group used to store the bullet
    bullets = Group()
    # create the screen object
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # create a ship object
    ship = Ship(ai_settings, screen)
    # create an alien object
    alien = Alien(ai_settings, screen)
    # game main body
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        # update the state of the ship
        ship.update()
        gf.update_bullets(bullets)
        # print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets, alien)


if __name__ == "__main__":
    run_game()
