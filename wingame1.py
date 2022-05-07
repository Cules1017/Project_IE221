import pygame, sys
from button import Button
from pygame import mixer
# from turtle import Screen
from game import *

pygame.init()

SCREEN = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("wingame")
mixer.music.load('asset/sound/mneu.mp3')
mixer.music.play(-1)
BG =  pygame.image.load("asset/BomberEndGame/wingame.png")
the = pygame.image.load("asset/BomberEndGame/Player 1 Wins.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font/font.ttf", size)
# def lan():
#     while True:
#         LAN_MOUSE_POS = pygame.mouse.get_pos()

#         SCREEN.fill("black")

#         LAN_TEXT = get_font(30).render("This is the LAN screen.", True, "White")
#         LAN_RECT = LAN_TEXT.get_rect(center=(640, 260))
#         SCREEN.blit(LAN_TEXT, LAN_RECT)

#         LAN_OKE = Button(image=None, pos=(640, 460), 
#                             text_input="OKE", font=get_font(30), base_color="White", hovering_color="Green")

#         LAN_OKE.changeColor(LAN_MOUSE_POS)
#         LAN_OKE.update(SCREEN)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if LAN_OKE.checkForInput(LAN_MOUSE_POS):
#                     main_menu()

#         pygame.display.update()  
# def play():
#     Game1=GameOnePL_PC()
#     Game1.startgame()
#     while True:
#         # PLAY_MOUSE_POS = pygame.mouse.get_pos()

#         # SCREEN.fill("black")

#         # PLAY_TEXT = get_font(30).render("This is the PLAY screen.", True, "White")
#         # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
#         # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

#         # PLAY_BACK = Button(image=None, pos=(640, 460), 
#         #                     text_input="BACK", font=get_font(30), base_color="White", hovering_color="Green")

#         # PLAY_BACK.changeColor(PLAY_MOUSE_POS)
#         # PLAY_BACK.update(SCREEN)
#         Game1.ingameLOGIC()
#         Game1.drawWindow(SCREEN)
#         if Game1.checkWin():
#             print("Gọi Màn hình Win Game")
#         if Game1.checkGameOver():
#             print("Gọi màn hình Game OVer")

#         # for event in pygame.event.get():
#         #     if event.type == pygame.QUIT:
#         #         pygame.quit()
#         #         sys.exit()
#             # if event.type == pygame.MOUSEBUTTONDOWN:
#             #     if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
#             #         main_menu()

#         #pygame.display.update()

# def options():
    
#     while True:
       
#         OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
     
#         SCREEN.fill("white")

#         OPTIONS_TEXT = get_font(30).render("This is the OPTIONS screen.", True, "Black")
#         OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
#         SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

#         OPTIONS_BACK = Button(image=None, pos=(640, 460), 
#                             text_input="BACK", font=get_font(30), base_color="Black", hovering_color="Green")

#         OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
#         OPTIONS_BACK.update(SCREEN)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
#                     main_menu()

#         pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(the, (400, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("  ", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(655, 100))

        # LAN_BUTTON = Button(image=pygame.image.load("asset/menu/but.png"), pos=(640, 250), 
        #                     text_input="PLAY&LAN", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        # PLAY_BUTTON = Button(image=pygame.image.load("asset/menu/but.png"), pos=(640, 370), 
        #                     text_input="PLAY", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        # OPTIONS_BUTTON = Button(image=pygame.image.load("asset/menu/but.png"), pos=(640, 490), 
        #                     text_input="OPTIONS", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("asset/BomberEndGame/Enter to Continue.jpg"), pos=(640, 610), 
                            text_input="   ", font=get_font(30), base_color="#CCFFFF", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # for button in [LAN_BUTTON,PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        for button in [QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
            #     if LAN_BUTTON.checkForInput(MENU_MOUSE_POS):
            #        lan()
            #     if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
            #         play()
            #     if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
            #         options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()