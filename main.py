import pygame, sys

FPS = 60

pygame.init()
pygame.display.set_mode ((800,600))
pygame.display.set_caption("НУ И ДУРА")
clock = pygame.time.Clock()

mario = pygame.image.load("images/mario.png")

pygame.display.update()


run = True
while run:
    clock.tick(FPS)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    pygame.display.update()