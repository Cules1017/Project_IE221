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

menu = pygame_menu.Menu('OPTIONS', 1280, 700,
                        theme=pygame_menu.themes.THEME_BLUE)


menu.add.selector('LEVEL', [('EASY', 1), ('MEDIUM', 2), ('DIFFICULT', 3)], onchange=set_difficulty)
menu.add.selector('MAP', [('KỶ BĂNG HÀ', 1), ('SA MẠC CÁT', 2), ('VÙNG ĐẤT CHẾT', 3),('CAO NGUYÊN',4)], onchange=set_difficulty)
menu.add.selector('SOUND', [('ON', 1), ('OFF', 2)], onchange=set_difficulty)
menu.add.button('QUIT', pygame_menu.events.EXIT)

menu.mainloop(surface)