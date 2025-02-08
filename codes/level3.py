import pygame
from pygame.locals import *
import sys
import puzzles
import Sprites
import genai_texts
import os
import random
import level2
import protag

def page3(screen, WIDTH, HEIGHT):
    # background
    background = Sprites.StoneBackground(WIDTH, HEIGHT) # Adjust path if needed
    foreground = Sprites.ForeGround(screen, WIDTH, HEIGHT)

    # Initialize puzzle scene
    player = protag.Player(20, 75)

    key = puzzles.Puzzle1(200, 100)
    escapeDoor = key.door(300, 300)
    escapeDoor.draw(screen)
    key.draw(screen)

    running = True

    while running:
        player.speed = 10
        # Different background color for the new page
        background.draw(screen)
        escapeDoor.draw(screen)
        # draw player
        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH, HEIGHT)  # Move player
        player.draw(screen) 
         # Draw player (must be AFTER filling the screen)

        foreground.draw()
        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        pygame.time.Clock().tick(60)
