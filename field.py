import pygame
#Цвета клеток
L_GREEN = (134, 228, 20)
D_GREEN = (129, 217, 19)
#Цвет бэкграунда
BACKGOUND = (158, 218, 219)

#Размер блока
block_size = 30
#Размер экрана
screen_size_width = 500
screen_size_height = 700
size = [screen_size_width, screen_size_height]
#Кол-во клеток на игровом поле
field_size = 12

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hungry Python")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(BACKGOUND)

    for row in range(field_size):
        for column in range(field_size):
            if ((column + row) % 2 == 0):
                pygame.draw.rect(screen, L_GREEN, [((screen_size_width/2)-(block_size*field_size)/2) + column*block_size, ((screen_size_height/2)-(block_size*field_size)/2)+row*block_size, block_size, block_size])
            else:
                pygame.draw.rect(screen, D_GREEN, [((screen_size_width/2)-(block_size*field_size)/2) + column*block_size, ((screen_size_height/2)-(block_size*field_size)/2)+row*block_size, block_size, block_size])

    pygame.display.flip()
