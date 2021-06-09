import pygame
import Items
from data import *
from snake import *
import time

pygame.init()
screen = pygame.display.set_mode([field_size, field_size + 75])

pygame.display.set_caption("Hungry Python")
apple1 = Items.item(screen, "apple")
stones = []
board = pygame.image.load("images/Board.png").convert_alpha()
plate = pygame.image.load("images/score_plate.png").convert_alpha()
snake = Snake(screen, apple1, stones, [6,6], [6,7], [6,8], 'up')
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26)
gameover_score = pygame.font.SysFont('Arial', 50)
fps = 5
prev_len = 3
death_sound_times = 1

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

    # Создание пожилой таблички
    screen.blit(plate, (field_size / 2 - 47, 25))

    # Обновление рекорда
    render_score = font_score.render(str(snake.get_length() - 3), 1, pygame.Color('black'))
    screen.blit(render_score, (field_size / 2 - (len(str(snake.get_length() - 3))*6), 28))

    # Создание Яблока
    apple1.create_new()

    # Отрисовка и движение змеи
    snake.draw()

    if snake.is_alive():
        snake.move()
    else:
        if death_sound_times == 1:
            death_sound_times = 0

    if is_dynamic_speed and snake.get_length() > prev_len:
        fps += 0.4
        prev_len = snake.get_length()


    clock.tick(fps)

    pygame.display.flip()
