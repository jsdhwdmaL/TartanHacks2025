import pygame
from pygame.locals import *
import sys
import puzzles
import Sprites
import google.generativeai as genai
import os

API_KEY = "AIzaSyCvEAFPwUCTRIl-BdsyCOeoZZFODf6rdKY"
genai.configure(api_key=API_KEY)

# Function to get AI-generated puzzle (riddle)
def generate_riddle():
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content("Create a puzzle for the player based on underwater themes, and the answer must be fish.")
    return response.text

def page2(screen, player, WIDTH, HEIGHT):
    # background
    font = pygame.font.Font(None, 36)
    background = Sprites.WoodenTileBackground(WIDTH, HEIGHT) # Adjust path if needed

    # Initialize puzzle scene
    puzzle_text = generate_riddle()
    player_input = ""
    solved = False
    foreground = Sprites.ForeGround(screen)
    running = True
    while running:
        # Different background color for the new page
        foreground.draw()

        # run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Submit answer
                    if "fish" in player_input.lower():  # Example condition (Replace with AI-checking logic)
                        solved = True
                elif event.key == pygame.K_BACKSPACE:
                    player_input = player_input[:-1]  # Delete last character
                else:
                    player_input += event.unicode  # Add typed character

        # draw player
        keys = pygame.key.get_pressed()
        player.speed = 4
        player.move(keys, WIDTH, HEIGHT)  # Move player
        player.draw(screen)  # Draw player (must be AFTER filling the screen)

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
        # draw key
        # key.draw(screen)
        # key.checkTouch(player)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        pygame.time.Clock().tick(60)
