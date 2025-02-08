import pygame
from pygame.locals import *

playerheight, playerwidth = 70,80

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/mermaid_forward.png")
        self.image = pygame.transform.scale(self.image, (playerheight, playerwidth))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 4
        self.horizontal_regular = pygame.transform.flip(self.image, False, False)
        self.horizontal_flip = pygame.transform.flip(self.image, True, False)
    def move(self, keys):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.rect.x -= self.speed
            self.image = self.horizontal_regular
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.image = self.horizontal_flip
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.image = pygame.image.load("assets/mermaid_backward.png")
            self.image = pygame.transform.scale(self.image, (playerheight, playerwidth))
            
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            self.image = pygame.image.load("assets/mermaid_forward.png")
            self.image = pygame.transform.scale(self.image, (playerheight, playerwidth))
           


    def draw(self, screen):
        # print("Image loaded successfully!", self.image)
        screen.blit(self.image, self.rect)

print("Adi is here")
print('CAN U GUYS SEE THIS')