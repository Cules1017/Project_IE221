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



menu.add.selector('VOLUME', [('BIG', 1), ('NORMAL', 2), ('SMALL', 3)], onchange=set_difficulty)
menu.add.selector('Soundtrack', [('ON', 1), ('OFF', 2)], onchange=set_difficulty)
menu.add.button('QUIT', pygame_menu.events.EXIT)

menu.mainloop(surface)