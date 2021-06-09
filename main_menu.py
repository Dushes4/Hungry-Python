import pygame
from data import *
import checkbox

def main_menu():
    pygame.init()
    pygame.display.set_caption("Hungry Python")
    WIDTH = 500
    HEIGHT = 600
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    check_stones = checkbox.Checkbox(screen, 365, 185, 1)
    check_speed = checkbox.Checkbox(screen, 365, 235, 2)
    check_teleport = checkbox.Checkbox(screen, 365, 285, 3)
    small = checkbox.Checkbox(screen, 122, 380, 4)
    middle = checkbox.Checkbox(screen, 238, 380, 5)
    big = checkbox.Checkbox(screen, 349, 380, 6)
    start_button = checkbox.Checkbox(screen, 150, 500, 7, beg_size_x=200,beg_size_y=50)
    font_captions = pygame.font.SysFont('Arial', 20, bold=True)

    is_main_menu = True
    img = pygame.image.load('images/background.png').convert_alpha()

    while is_main_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            check_stones.update_checkbox(event)
            check_speed.update_checkbox(event)
            check_teleport.update_checkbox(event)
            small.update_checkbox(event)
            middle.update_checkbox(event)
            big.update_checkbox(event)
            start_button.update_checkbox(event)

            screen.fill((200, 200, 200))
            screen.blit(img, (0,0))
            check_stones.render_checkbox()
            check_speed.render_checkbox()
            check_teleport.render_checkbox()
            small.render_checkbox()
            middle.render_checkbox()
            big.render_checkbox()
            start_button.render_checkbox()

            render_telep = font_captions.render('Начать игру', 1, pygame.Color('black'))
            screen.blit(render_telep, (190, 515))

            pygame.display.flip()
            if start_button.is_checked():
                is_main_menu = False
                pygame.display.quit()
    is_dynamic_speed = check_speed.is_checked()
    is_border_teleport = check_teleport.is_checked()
    is_spawn_stones = check_stones.is_checked()
    block_num = 12*small.is_checked() + 16*middle.is_checked() + 20*big.is_checked()
    return(is_dynamic_speed, is_border_teleport,is_spawn_stones,block_num)
