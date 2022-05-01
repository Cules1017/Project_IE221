import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1280, 700))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Boomberman', 1280, 700,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Tên Của Bạn:', default='John Doe')
menu.add.selector('Chế Độ Game:', [('Đánh quái', 1), ('Chơi với máy', 2), ('Chơi với người', 3)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)