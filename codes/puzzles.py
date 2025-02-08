import pygame
from pygame.locals import *

class Puzzle1:
    def __init__(self):
        self.image = pygame.image.load("assets/key.png")
        self.x = 380
        self.y = 300
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.playerHasKey = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def checkTouch(self, player):
        #rect
        collide = pygame.Rect.collidepoint() #check if collided with player
        #make the key disappear
        #now the player should move to the chest or the other target to solve this puzzle

