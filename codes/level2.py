import pygame
from pygame.locals import *
import sys
import puzzles
import Sprites
print("no")
def page2(screen, player, WIDTH, HEIGHT):
    # background
    background = Sprites.WoodenTileBackground(WIDTH, HEIGHT) # Adjust path if needed

    running = True
    while running:
        # Different background color for the new page
        screen.fill((50, 0, 0))

        # run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # draw player
        keys = pygame.key.get_pressed()
        player.speed = 4
        player.move(keys, WIDTH, HEIGHT)  # Move player
        player.draw(screen)  # Draw player (must be AFTER filling the screen)

        # draw key
        # key.draw(screen)
        # key.checkTouch(player)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        pygame.time.Clock().tick(60)
