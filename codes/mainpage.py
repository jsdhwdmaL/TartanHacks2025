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

# Generate puzzles
PUZZLE1 = genai_texts.generate_riddle1()

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
background = Sprites.StoneBackground(WIDTH, HEIGHT) # Adjust path if needed

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

<<<<<<< HEAD
    rock.draw(screen)
    player.collision(keys, rock, WIDTH, HEIGHT)
=======
        rock.draw(screen)
        player.collision(keys, WIDTH, HEIGHT, rock)
>>>>>>> 9051b3fce8384376c7ad697ef1bfcecc37248942

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
