from main_menu import main_menu
# Размеры поля
BLOCK_SIZE = 30

#Настройки игры
is_dynamic_speed, is_border_teleport,is_spawn_stones,block_num = main_menu()
field_size = BLOCK_SIZE*block_num

#Цвета клеток
L_GREEN = (134, 228, 20)
D_GREEN = (129, 217, 19)
RED = (181, 55, 55, 128)
SCORE_BROWN = (95, 60, 29)
#Цвет бэкграунда
BACKGOUND = (158, 218, 219)
