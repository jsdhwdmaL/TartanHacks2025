import pygame
from pygame.locals import *

class door:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/closed-door.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def checkTouch(self, player):
        #rect
        collided = self.rect.colliderect(player.rect) #check if collided with player
        #make the door disappear and chane 
        if player.haskey1 and collided:
            self.image = None
            player.hitDoor = True
            #now the scene should change
