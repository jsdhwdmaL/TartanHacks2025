import pygame
from pygame.locals import *
import sys
import protag
import puzzles
import Panels
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
rock = Panels.Rock(240, 240)
rock.draw(screen)
# background
background = Panels.WoodenTileBackground(WIDTH, HEIGHT) # Adjust path if needed

running = True
stage = 1

while running:
    if stage == 1:
        background.draw(screen)
    elif stage == 2:
        level2.page2(screen, player, WIDTH, HEIGHT)

    for event in pygame.event.get():
        if (player.haskey1 == True):
            scene1 = pygame.image.load("assets/woodenBackground.png")
            scene1 = pygame.transform.scale(scene1, (WIDTH, HEIGHT))
            fade_scene.fade_to_next_scene(screen, clock, scene1)
            stage = 2
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw player
    keys = pygame.key.get_pressed()
    player.move(keys)  # Move player
    player.draw(screen)  # Draw player (must be AFTER filling the screen)

    rock.draw(screen)
    # draw key
    key.draw(screen)
    key.checkTouch(player)

    transparent_surface = pygame.Surface((800, 600), pygame.SRCALPHA)
    transparent_surface.fill((0, 0, 40, 128))  # RGBA: 50% transparent blue
    screen.blit(transparent_surface, (0, 0))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)


pygame.quit()
