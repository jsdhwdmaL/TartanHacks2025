import pygame
from pygame.locals import *
import sys
import protag
import puzzles
import Sprites
import level2
import fade_scene

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("LiquidLabyrinth")

# Create Player Instance
player = protag.Player(20, 75)

# Create puzzle1 instance
key = puzzles.Puzzle1(200, 100)
key.draw(screen)
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
        if (player.haskey1 == True and (keys[pygame.K_a] or keys[pygame.K_d]
                                      | keys[pygame.K_w] or keys[pygame.K_d])):
            scene1 = pygame.image.load("assets/woodenBackground.png")
            scene1 = pygame.transform.scale(scene1, (WIDTH, HEIGHT))
            fade_scene.fade_to_next_scene(screen, clock, scene1)
            scene = 2

    if (player.haskey1 == True):
        player.speed = 0

    if scene == 1:
        background.draw(screen)
    
    else:
        player.speed = 0
        level2.page2(screen, player, WIDTH, HEIGHT)

    # draw player
    keys = pygame.key.get_pressed()
    player.move(keys, WIDTH, HEIGHT)  # Move player
    player.draw(screen)  # Draw player (must be AFTER filling the screen)

    rock.draw(screen)
     # checks if player is touching obstacle, and prevents it from moving. 
    collided = player.rect.colliderect(rock.rect) #check if collided with player
    if(collided):
        player.speed = 0
    else:
        player.speed = 3
    # draw key
    key.draw(screen)
    key.checkTouch(player)

    foreground.draw()
    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(80)


pygame.quit()
