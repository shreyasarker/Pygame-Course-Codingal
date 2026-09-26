import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Key Events")

x, y = 220, 220
color = "white"

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 1. KEYDOWN: Triggers once when a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 20
                color = "blue"
            elif event.key == pygame.K_RIGHT:
                x += 20
                color = "yellow"
            elif event.key == pygame.K_UP:
                y -= 20
                color = "red"
            elif event.key == pygame.K_DOWN:
                y += 20
                color = "green"

        # 2. KEYUP: Triggers once when a key is released
        if event.type == pygame.KEYUP:
            color = "white"

    screen.fill("black")
    pygame.draw.rect(screen, color, (x, y, 60, 60))
    pygame.display.flip()


pygame.quit()