import pygame

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load Scene Backgrounds
scene1 = pygame.image.load("assets/woodenBackground.png")  # First scene
scene2 = pygame.image.load("assets/rock.png")  # Second scene
scene1 = pygame.transform.scale(scene1, (WIDTH, HEIGHT))
scene2 = pygame.transform.scale(scene2, (WIDTH, HEIGHT))

# Create a Transparent Surface for Fading
fade_surface = pygame.Surface((WIDTH, HEIGHT))
fade_surface.fill((0, 0, 0))  # Black fade by default

def fade_to_next_scene():
    for alpha in range(0, 256, 5):  # Increase alpha from 0 to 255
        fade_surface.set_alpha(alpha)  # Set transparency
        screen.blit(scene1, (0, 0))  # Keep the first scene visible
        screen.blit(fade_surface, (0, 0))  # Apply fade effect
        pygame.display.flip()
        clock.tick(30)  # Control fade speed

running = True
scene = 1  # Track current scene

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            fade_to_next_scene()  # Trigger fade on SPACE key
            scene = 2  # Switch to next scene

    # Render Current Scene
    if scene == 1:
        screen.blit(scene1, (0, 0))
    else:
        screen.blit(scene2, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()