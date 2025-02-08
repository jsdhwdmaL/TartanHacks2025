import pygame
from pygame.locals import *

playerheight, playerwidth = 70,80

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/mermaid_forward.png")
        self.image = pygame.transform.scale(self.image, (playerheight, playerwidth))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 3
        self.horizontal_regular = pygame.transform.flip(self.image, False, False)
        self.horizontal_flip = pygame.transform.flip(self.image, True, False)
        self.haskey1 = False
        self.idleCount = 0
        self.original_image = "forward"
        self.isFlipped = False        self.hitDoor = False

    def move(self, keys, width, height):
        if ((keys[pygame.K_a]) and (self.rect.x >= 0)):
            self.idleCount = 0
            self.rect.x -= self.speed
            self.image = self.horizontal_regular
        if ((keys[pygame.K_d]) and (self.rect.x <= (width - playerwidth))):
            self.idleCount = 0
            self.rect.x += self.speed
            self.image = self.horizontal_flip
        if ((keys[pygame.K_w]) and (self.rect.y >= 0)):
            self.idleCount = 0
            self.rect.y -= self.speed
            self.image = pygame.image.load("assets/mermaid_backward.png")
            self.image = pygame.transform.scale(self.image, (playerheight, playerwidth))
            self.original_image = "backward"
        if ((keys[pygame.K_s]) and (self.rect.y <= (height - playerheight))):
            self.idleCount = 0
            self.rect.y += self.speed
            self.image = pygame.image.load("assets/mermaid_forward.png")
            self.image = pygame.transform.scale(self.image, (playerheight, playerwidth))
            self.original_image = "forward"
        else: #idling
            self.idleCount += 1
            if(self.idleCount == 25) and (self.original_image == "forward"):
                self.idleCount = 0
                self.original_image = "idle"
                self.image = pygame.image.load("assets/mermaid_idle.png")
                self.image = pygame.transform.scale(self.image, (playerheight, playerwidth))
            if(self.idleCount == 25) and (self.original_image == "backward"):
                self.idleCount = 0
                self.original_image = "idle_backward"
                self.image = pygame.image.load("assets/mermaid_idle_backward.png")
                self.image = pygame.transform.scale(self.image, (playerheight, playerwidth))
            if(self.idleCount == 25) and (self.original_image == "idle"):
                self.idleCount = 0
                self.original_image = "forward"
                self.image = pygame.image.load("assets/mermaid_forward.png")
                self.image = pygame.transform.scale(self.image, (playerheight, playerwidth))
            if(self.idleCount == 25) and (self.original_image == "idle_backward"):
                self.idleCount = 0
                self.original_image = "backward"
                self.image = pygame.image.load("assets/mermaid_backward.png")
                self.image = pygame.transform.scale(self.image, (playerheight, playerwidth))





    def draw(self, screen):
        # print("Image loaded successfully!", self.image)
        screen.blit(self.image, self.rect)
