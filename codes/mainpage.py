import pygame
from pygame.locals import *
import sys
import protag
import puzzles
import Panels
import level1

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("GameName")

# Create Player Instance
player = protag.Player(20, 75)

# Create puzzle1 instance
key = puzzles.Puzzle1(200, 100)
key.draw(screen)
#key = level1.Puzzle1()
rock = Panels.Rock(240, 240)
rock.draw(screen)
# background
background_main = pygame.image.load("assets/wooden.png")
background_main = pygame.transform.scale(background_main, (WIDTH, HEIGHT))  # Resize it into 800*600
background = Panels.WoodenTileBackground(WIDTH, HEIGHT) # Adjust path if needed

background.draw(screen)
running = True
while running:
    # Deep sea blue ship background
    screen.blit(background_main, (0, 0))  # (0,0) means top-left corner
    # screen.fill((255, 255, 255))

    background.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # draw player
    keys = pygame.key.get_pressed()
    player.move(keys, WIDTH, HEIGHT)  # Move player
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

"""
if key.playerHasKey == False:
        
if key.playerHasKey == True:
        screen.blit(background_main, (0, 0))
"""