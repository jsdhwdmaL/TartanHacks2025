import pygame
from pygame.locals import *
import sys
import protag
import puzzles
import Sprites
import level2
import fade_scene
import door
import genai_texts

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("LiquidLabyrinth")

# Generate puzzles PLEASE REMOVE THIS
# PUZZLE1 = genai_texts.generate_riddle1()
PUZZLE1 = "HELLO HOLDER"

# Create Player Instance
player = protag.Player(20, 75)

# Create puzzle1 instance
key = puzzles.Puzzle1(200, 100)
escapeDoor = key.door(400,300)
key.draw(screen)
escapeDoor.draw(screen)
#key = level1.Puzzle1()
rock = Sprites.Rock(240, 240)
rock.draw(screen)
# background
background = Sprites.WoodenTileBackground(WIDTH, HEIGHT) # Adjust path if needed

foreground = Sprites.ForeGround(screen)

scene = 1
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (player.hitDoor and scene == 1):
            scene1 = pygame.image.load("assets/woodenBackground.png")
            scene1 = pygame.transform.scale(scene1, (WIDTH, HEIGHT))
            fade_scene.fade_to_next_scene(screen, clock, scene1)
            scene = 2

        #check if scene == 2 and riddle has been solved
        #then moved to scene 3

    if (player.hitDoor):
        player.speed = 0

    if scene == 1:
        background.draw(screen)
        key.draw(screen)
        escapeDoor.draw(screen)
        # draw player
        keys = pygame.key.get_pressed()
        player.move(keys, WIDTH, HEIGHT)  # Move player
        player.draw(screen)  # Draw player (must be AFTER filling the screen)

        rock.draw(screen)
        player.collision(rock, keys, WIDTH, HEIGHT)

        # draw key and door
        key.draw(screen)
        escapeDoor.draw(screen)

        if player.haskey1:
            escapeDoor.checkTouch(player)
        else:
            key.checkTouch(player)

    else:
        player.speed = 0
        level2.page2(screen, player, PUZZLE1, WIDTH, HEIGHT)


    foreground.draw()
    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(80)


pygame.quit()
