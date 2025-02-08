import pygame
from pygame.locals import *
import sys
import puzzles
import Sprites
import genai_texts
import os
import random

def page2(screen, player, puzzle, WIDTH, HEIGHT):
    # background
    font = pygame.font.Font(None, 36)
    background = Sprites.WoodenTileBackground(WIDTH, HEIGHT) # Adjust path if needed

    # Initialize puzzle scene
    puzzle_text = puzzle
    player_input = ""
    solved = False
    foreground = Sprites.ForeGround(screen)
    running = True
    submitted = False

    while running:
        # Different background color for the new page
        background.draw(screen)

        # run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Submit answer
                    submitted = True
                    if "fish" in player_input.lower():  # Example condition (Replace with AI-checking logic)
                        solved = True
                elif event.key == pygame.K_BACKSPACE:
                    player_input = player_input[:-1]  # Delete last character
                else:
                    player_input += event.unicode  # Add typed character

        # keys
        keys = pygame.key.get_pressed()

        # Render puzzle text
        text_surface = font.render(puzzle_text, True, (255, 255, 255))
        screen.blit(text_surface, (50, 200))

        # Render player input
        input_surface = font.render("Your Answer: " + player_input, True, (0, 255, 0))
        screen.blit(input_surface, (50, 300))

        # Display feedback
        if solved:
            solved_surface = font.render("Correct! You solved the puzzle!", True, (255, 255, 0))
            screen.blit(solved_surface, (50, 400))
        elif (not solved and submitted):
            unsolved_surface = font.render("Oops! Try again!", True, (255, 255, 0))
            screen.blit(unsolved_surface, (random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)))
        # draw key
        # key.draw(screen)
        # key.checkTouch(player)
        foreground.draw()
        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        pygame.time.Clock().tick(60)
