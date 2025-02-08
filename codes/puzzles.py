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
        if not self.playerHasKey:
            screen.blit(self.image, self.rect)

    def checkTouch(self, player):
        #rect
        collided = self.rect.colliderect(player.rect) #check if collided with player
        #make the key disappear
        if collided:
            self.playerHasKey = True
            self.image = None

        #now the player should move to the chest or the other target to solve this puzzle

print("puzzle 1 has ran")