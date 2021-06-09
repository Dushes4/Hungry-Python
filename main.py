import pygame
import Items
from data import *
import time

pygame.init()
screen = pygame.display.set_mode([field_size, field_size + 75])

pygame.display.set_caption("Hungry Python")
board = pygame.image.load("images/Board.png").convert_alpha()
plate = pygame.image.load("images/score_plate.png").convert_alpha()
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

    # Создание забора
    for column in range(block_num):
        screen.blit(board, (0 + column * BLOCK_SIZE, 0))

    # Создание таблички
    screen.blit(plate, (field_size / 2 - 47, 25))
    
    clock.tick(fps)
    pygame.display.flip()
