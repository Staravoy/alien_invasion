import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас, що представляє одного прибульця флоту"""
    def __init__(self, ai_game):
        """Ініціалізувати прибульця та задати його початкове розташування"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alian image and set its rect attribute.
        self.image = pygame.image.load('images/bomb.svg')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of th screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)