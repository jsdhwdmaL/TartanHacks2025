import pygame
from pygame.locals import *
import sys

def new_page(screen):
    running = True
    while running:
        screen.fill((50, 0, 0))  # Different background color for the new page

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        pygame.time.Clock().tick(60)