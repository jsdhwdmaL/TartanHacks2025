import pygame
from pygame.locals import *
import sys
import puzzles
import Sprites
import genai_texts
import os
import random
import level2
import ending
import fade_scene

def page3(screen, player, WIDTH, HEIGHT):
    # background
    font = pygame.font.Font(None, 60)
    background = Sprites.WoodenTileBackground(WIDTH, HEIGHT) # Adjust path if needed

    # Initialize puzzle scene
    puzzle_text = "do we need puzzle for this??"
    lines = level2.wrap_text(puzzle_text, font, WIDTH - 20)
    player_input = ""
    solved = False
    foreground = Sprites.ForeGround(screen)
    running = True
    submitted = False
    scene = 3

    while running:
        # Different background color for the new page
        scene1 = background.draw(screen)

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
            if solved == True:
                fade_scene.fade_to_next_scene(screen, pygame.time.Clock(), scene1)
                scene = 4

        if scene == 4:
            ending.page_end(screen, player, WIDTH, HEIGHT)

        # keys
        keys = pygame.key.get_pressed()

        # Render puzzle text
        y_offset = 50  # Start position for the text
        for line in lines:
            rendered_text = font.render(line, True, (255, 255, 255))  # Black text
            screen.blit(rendered_text, (30, y_offset))  # Draw at position (10, y_offset)
            y_offset += rendered_text.get_height()  # Move to the next line

        # Render player input
        input_surface = font.render("Your Answer: " + player_input, True, (0, 255, 0))
        screen.blit(input_surface, (50, 300))

        # Display feedback
        if solved:
            solved_surface = font.render("Congrats! You escaped!", True, (255, 255, 0))
            screen.blit(solved_surface, (100, 300))
        # elif (not solved and submitted):
        #     unsolved_surface = font.render("Oops! Try again!", True, (255, 255, 0))
        #     screen.blit(unsolved_surface, (random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)))

        foreground.draw()
        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        pygame.time.Clock().tick(60)
