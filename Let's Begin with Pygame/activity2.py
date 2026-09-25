import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("bgpygame.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

image = pygame.image.load("penguin.png").convert_alpha()
image = pygame.transform.scale(image, (300, 300))

image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(image, image_rect)

    pygame.display.flip()

pygame.quit()