import pygame
from data import *

def main_menu():
    pygame.init()
    pygame.display.set_caption("Hungry Python")
    WIDTH = 500
    HEIGHT = 600
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    font_captions = pygame.font.SysFont('Arial', 20, bold=True)

    is_main_menu = True
    img = pygame.image.load('images/background.png').convert_alpha()

    while is_main_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        screen.fill((200, 200, 200))
        screen.blit(img, (0,0))
            
        pygame.display.flip()
    
    return()
