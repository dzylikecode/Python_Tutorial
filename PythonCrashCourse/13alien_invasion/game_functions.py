import sys
import pygame
from bullet import Bullet


def check_events_keydown(event, ai_settings, screen, ship, bullets):
    """Response to a keyboard press"""
    if event.key == pygame.K_RIGHT:
        # Inform ship that we're about to move to the right
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        # create a new bullet, and append it to the group
        # Before creating, check the number of bullet first
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Launch a bullet if not reaching upper limit"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_events_keyup(event, ship):
    """Response to a keyboard up"""
    if event.key == pygame.K_RIGHT:
        # Stop motion to the right
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """monitor keyboard events and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_events_keyup(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """update the screen, and switch to the new screen"""
    # fill the screen with background color
    screen.fill(ai_settings.bg_color)
    # Redraw all the bullets behind the spaceship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # exchange the screen contents
    pygame.display.flip()


def update_bullets(bullets):
    """update the position of bullets, delete the bullet had disappeared"""
    bullets.update()
    # Remove the bullet had disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
