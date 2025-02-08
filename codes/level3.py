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
import protag

def page3(screen, player, WIDTH, HEIGHT):
    # background
    background = Sprites.StoneBackground(WIDTH, HEIGHT) # Adjust path if needed
    foreground = Sprites.ForeGround(screen)

    foreground = Sprites.ForeGround(screen)
    player = protag.Player(20, 75)
    pot = Sprites.Pot(100, 200)
    key = puzzles.Puzzle1(200, 100)
    escapeDoor = key.door(300, 300)
    escapeDoor.draw(screen)
    key.draw(screen)

    running = True
   
    scene = 3

    while running:
        player.speed = 10
        # Different background color for the new page
        scene1 = background.draw(screen)

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
            if solved == True:
                fade_scene.fade_to_next_scene(screen, pygame.time.Clock(), scene1)
                scene = 4

        if scene == 4:
            ending.page_end(screen, player, WIDTH, HEIGHT)

        # door
        escapeDoor.draw(screen)

        # draw player
        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH, HEIGHT)  # Move player
        player.draw(screen)

        
       
        

        # Display feedback
        
        # elif (not solved and submitted):
        #     unsolved_surface = font.render("Oops! Try again!", True, (255, 255, 0))
        #     screen.blit(unsolved_surface, (random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)))

        foreground.draw()
        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 frames per second
        pygame.time.Clock().tick(60)
