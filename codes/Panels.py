import pygame
from pygame.locals import *
import protag

tileWidth, tileHeight = 50, 50
class WoodenTile:
     def __init__(self, x, y):
        self.image = pygame.image.load("assets/wooden.png")

        self.image = pygame.transform.scale(self.image, (tileWidth, tileHeight))

        self.rect = self.image.get_rect(topleft=(x, y))

     def draw(self, screen):
        # print("Image loaded successfully!", self.image)
        screen.blit(self.image, self.rect)

class WoodenTileBackground:
     def __init__(self, width, height):
        self.image = pygame.image.load("assets/woodenBackground.png")

        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect(topleft=(0, 0))

     def draw(self, screen):
        # print("Image loaded successfully!", self.image)
        screen.blit(self.image, self.rect)

