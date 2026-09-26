import pygame

pygame.init()

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Drawing Circles")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(WHITE)

    # Solid circle: surface, color, center(x, y), radius
    pygame.draw.circle(window, GREEN, (300, 300), 50)

    # Outlined circle: surface, color, center(x, y), radius, line_width
    pygame.draw.circle(window, GREEN, (100, 100), 50, 3)

    pygame.display.flip()


pygame.quit()