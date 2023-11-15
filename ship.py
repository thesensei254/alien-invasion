import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initailize ship and set positions"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and its rect
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()

        # start each ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at it's current position"""
        self.screen.blit(self.image, self.rect)
