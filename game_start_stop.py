import pygame
import random

# Initialise Pygame, pygame is a set of Python module designed for writing games.
pygame.init()

# Set up the display (use set_mode to get a Surface)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Super Game")

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with white
    screen.fill((255, 255, 255))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
