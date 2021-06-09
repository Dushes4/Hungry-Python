from random import randrange
from data import *
import pygame


class item:

    def __init__(self, inp_surface, input_type):
        self.surface = inp_surface
        self.type = input_type
        self.x = randrange(BLOCK_SIZE, field_size - BLOCK_SIZE, BLOCK_SIZE)
        self.y = randrange(BLOCK_SIZE + 75, field_size - BLOCK_SIZE, BLOCK_SIZE)

    def create_new(self):
        if self.type == "apple":
            img = pygame.image.load('images/apple.png').convert_alpha()
            self.surface.blit(img, (self.x, self.y))
        if self.type == "stone":
            img = pygame.image.load('images/rock.png').convert_alpha()
            self.surface.blit(img, (self.x, self.y))

    def generate(self):
        self.x = randrange(BLOCK_SIZE, field_size-BLOCK_SIZE, BLOCK_SIZE)
        self.y = randrange(BLOCK_SIZE+75, field_size - BLOCK_SIZE, BLOCK_SIZE)
