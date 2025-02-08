import pygame
from pygame.locals import *
import sys
import protag
import background

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("GameName")

# Create Player Instance
player = protag.Player(400, 300)

# background
background_main = pygame.image.load("assets/wooden.png")  # Adjust path if needed
background_main = pygame.transform.scale(background_main, (WIDTH, HEIGHT))  # Resize if necessary

running = True
while running:
    # Deep sea blue ship background
    screen.blit(background_main, (0, 0))  # (0,0) means top-left corner

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw player
    keys = pygame.key.get_pressed()
    player.move(keys)  # Move player
    player.draw(screen)  # Draw player (must be AFTER filling the screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)


pygame.quit()

