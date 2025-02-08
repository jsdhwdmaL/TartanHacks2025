import pygame
from pygame.locals import *
import sys
import protag
import Panels
import level1

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("GameName")

# Create Player Instance
player = protag.Player(400, 300)

# Create puzzle1 instance
#key = level1.Puzzle1()

# background
background = Panels.WoodenTileBackground(WIDTH, HEIGHT) # Adjust path if needed

background.draw(screen)
running = True
while running:
    # Deep sea blue ship background
    background.draw(screen)
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

