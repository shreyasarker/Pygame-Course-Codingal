# Write a Python program to create an empty Pygame window.

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 500))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()