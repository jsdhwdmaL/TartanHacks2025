import pygame
from pygame.locals import *
import sys
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
def drawBackground(screen, width, height):
        for x in range(0, width, tileWidth):
            for y in range(0, height, tileHeight):
                wood = WoodenTile(x,y)
                wood.draw(screen)

