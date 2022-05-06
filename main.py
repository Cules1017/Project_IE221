import pygame, sys
from button import Button
from pygame import mixer
from pygame import movie
from game import *
pygame.init()

SCREEN = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Menu")
mixer.music.load('asset/sound/mneu.mp3')
mixer.music.play(-1)
BG = pygame.image.load("asset/menu/taigameboom.png")
the=  pygame.image.load("asset/menu/td.png")
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font/font.ttf", size)
def name():
    while True:
        NAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        NAME_TEXT = get_font(30).render("This is the NAME screen.", True, "White")
        NAME_RECT = NAME_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(NAME_TEXT, NAME_RECT)

        NAME_OKE = Button(image=None, pos=(640, 460), 
                            text_input="OKE", font=get_font(30), base_color="White", hovering_color="Green")

        NAME_OKE.changeColor(NAME_MOUSE_POS)
        NAME_OKE.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NAME_OKE.checkForInput(NAME_MOUSE_POS):
                    main_menu()

        pygame.display.update()  
def play():
    Game1=GameOnePL_PC()
    Game1.startgame()
    while True:
        # PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # SCREEN.fill("black")

        # PLAY_TEXT = get_font(30).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # PLAY_BACK = Button(image=None, pos=(640, 460), 
        #                     text_input="BACK", font=get_font(30), base_color="White", hovering_color="Green")

        # PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        # PLAY_BACK.update(SCREEN)
        Game1.ingameLOGIC()
        Game1.drawWindow(SCREEN)
        if Game1.checkWin():
            print("Gọi Màn hình Win Game")
        if Game1.checkGameOver():
            print("Gọi màn hình Game OVer")

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
            #         main_menu()

        #pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(30).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(the, (40, -140))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("BOOMMAN GAME", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(655, 100))

        NAME_BUTTON = Button(image=pygame.image.load("asset/menu/but.png"), pos=(640, 250), 
                            text_input="NAME", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        PLAY_BUTTON = Button(image=pygame.image.load("asset/menu/but.png"), pos=(640, 370), 
                            text_input="PLAY", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("asset/menu/but.png"), pos=(640, 490), 
                            text_input="OPTIONS", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("asset/menu/but.png"), pos=(640, 610), 
                            text_input="QUIT", font=get_font(30), base_color="#CCFFFF", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [NAME_BUTTON,PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NAME_BUTTON.checkForInput(MENU_MOUSE_POS):
                    name()
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()