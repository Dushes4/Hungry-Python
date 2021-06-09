from collections import deque
import pygame
from data import *
import Items

n = field_size

class Snake:
    FIFO = deque()

    def __init__(self, screen, apple, stones, fst_xy, snd_xy, trd_xy, direction, dx=0, dy=-1):
        self.FIFO.append(fst_xy)
        self.FIFO.append(snd_xy)
        self.FIFO.append(trd_xy)
        self.direction = direction
        self.dx = dx
        self.dy = dy
        self.screen = screen
        self.apple = apple
        self.stones = stones

    def put_new_head(self):
        if (is_border_teleport):
            self.FIFO.appendleft([(self.FIFO[0][0] + self.dx) % block_num, (self.FIFO[0][1] + self.dy) % block_num])
        else:
            self.FIFO.appendleft([self.FIFO[0][0] + self.dx, self.FIFO[0][1] + self.dy])

    def move_old_tail(self):
        self.FIFO.pop()

    def get_length(self):
        return len(self.FIFO)

    def move(self):
        self.put_new_head()
        if not(self.FIFO[0][0]*BLOCK_SIZE == self.apple.x and self.FIFO[0][1]*BLOCK_SIZE+75 == self.apple.y):
            self.move_old_tail()
        if self.FIFO[0][0] * BLOCK_SIZE == self.apple.x and self.FIFO[0][1] * BLOCK_SIZE + 75 == self.apple.y:
            self.apple.generate()
            if is_spawn_stones:
                self.stones.append(Items.item(self.screen, "stone"))
        [stone.create_new() for stone in self.stones]
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if self.direction != 'down':
                self.dx, self.dy = 0, -1
                self.direction = 'up'
        elif key[pygame.K_s]:
            if self.direction != 'up':
                self.dx, self.dy = 0, 1
                self.direction = 'down'
        elif key[pygame.K_a]:
            if self.direction != 'right':
                self.dx, self.dy = -1, 0
                self.direction = 'left'
        elif key[pygame.K_d]:
            if self.direction != 'left':
                self.dx, self.dy = 1, 0
                self.direction = 'right'

    def draw(self):
        for block in self.FIFO:
            [pygame.draw.rect(self.screen, pygame.Color('blue'), (block[0]*BLOCK_SIZE, block[1]*BLOCK_SIZE + 75, BLOCK_SIZE-1, BLOCK_SIZE-1)) for block in self.FIFO]
            pygame.draw.rect(self.screen, pygame.Color('yellow'),
                             (self.FIFO[0][0] * BLOCK_SIZE, self.FIFO[0][1]* BLOCK_SIZE + 75, BLOCK_SIZE - 1, BLOCK_SIZE - 1))
