import pygame
from pygame.locals import *

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/player.png")
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 3

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, screen):
        # print("Image loaded successfully!", self.image)
        screen.blit(self.image, self.rect)

print("Adi is here")
print('CAN U GUYS SEE THIS')