import pygame
from data import *
import time

pygame.init()
screen = pygame.display.set_mode([field_size, field_size + 75])

pygame.display.set_caption("Hungry Python")
clock = pygame.time.Clock()
fps = 5

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(BACKGOUND)

    # Создание игрового поля
    for row in range(block_num):
        for column in range(block_num):
            if ((column + row) % 2 == 0):
                pygame.draw.rect(screen, L_GREEN,
                                 [0 + column * BLOCK_SIZE, 75 + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])
            else:
                pygame.draw.rect(screen, D_GREEN,
                                 [0 + column * BLOCK_SIZE, 75 + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE])


    clock.tick(fps)
    pygame.display.flip()
