from ast import While
from sqlite3 import connect
import pygame, sys
from button import Button
from pygame import mixer
# from pygame import movie
from game import *

import pygame_menu
pygame.init()
vollum=30
P='26.156.239.113'
IP=111
FPS=30
clock=pygame.time.Clock()
SCREEN = pygame.display.set_mode((1280, 700))
pygame.display.set_caption("Menu")
mixer.music.load('asset/sound/mneu.mp3')
mixer.music.play(-1)
mixer.music.set_volume(vollum)
BG = pygame.image.load("asset/menu/taigameboom.gif")
BGwin =pygame.transform.scale(pygame.image.load("asset/banner/win.jpg"),(1280, 700))  
the=  pygame.image.load("asset/menu/td.gif")
Gov=pygame.transform.scale(pygame.image.load('asset/banner/GOV.jpg'),(1280, 700))
Game=PlayLan()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font/font.ttf", size)
def lan():
    while True:
        LAN_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        LAN_TEXT = get_font(30).render("This is the LAN screen.", True, "White")
        LAN_RECT = LAN_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LAN_TEXT, LAN_RECT)

        LAN_OKE = Button(image=None, pos=(640, 460), 
                            text_input="OKE", font=get_font(30), base_color="White", hovering_color="Green")

        LAN_OKE.changeColor(LAN_MOUSE_POS)
        LAN_OKE.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LAN_OKE.checkForInput(LAN_MOUSE_POS):
                    main_menu()

        pygame.display.update()  
def Twoplay():
    music= random.randint(0, 2)
    mixer.music.load('asset/sound/'+str(music)+'bg.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(vollum)
    Game1=GameTwoPL()
    Game1.startgame()
    while True:
       
        Game1.ingameLOGIC()
        Game1.drawWindow(SCREEN)
        if Game1.checkWin():
            EndGame(Game1.win,Game1.msg)
        if Game1.checkGameOver():
            EndGame(Game1.win,Game1.msg)
def Oneplay():
    music= random.randint(0, 2)
    mixer.music.load('asset/sound/'+str(music)+'bg.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(vollum)
    Game1=GameOnePL_PC()
    Game1.startgame()
    while True:
       
        Game1.ingameLOGIC()
        Game1.drawWindow(SCREEN)
        if Game1.checkWin():
            Wingame(2,Game1.msg)
        if Game1.checkGameOver():
            GameOver(2,Game1.msg)
def Campaign():
    music= random.randint(0, 2)
    mixer.music.load('asset/sound/'+str(music)+'bg.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(vollum)
    Game1=Kill_mons()
    Game1.startgame()
    while True:

        Game1.ingameLOGIC()
        Game1.drawWindow(SCREEN)
        if Game1.checkWin():
            Wingame(1,"")
        if Game1.checkGameOver():
            GameOver(1,"")
def GameOver(i,msg):
    mixer.music.load('asset/sound/GOV.mp3')
    mixer.music.play()
    mixer.music.set_volume(vollum)
    while True:
        SCREEN.fill((125,155,255))
        SCREEN.blit(Gov, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render(msg, True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(655, 100))
        QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("asset/menu/but.gif"),(300,100)), pos=(500, 610), 
                            text_input="Back", font=get_font(19), base_color="#CCFFFF", hovering_color="White")
        AGAIN_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("asset/menu/but.gif"),(300,100)), pos=(800, 610), 
                            text_input="Play AGain", font=get_font(19), base_color="#CCFFFF", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for button in [QUIT_BUTTON,AGAIN_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                if AGAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if i==1:
                        Campaign()
                    elif i==2:
                        Oneplay()
                    elif i==3:
                        Twoplay()
        pygame.display.update()
def EndGame(i,msg):
    mixer.music.load('asset/sound/WIN.mp3')
    mixer.music.play()
    mixer.music.set_volume(50)
    BGEG =  pygame.image.load("asset/BomberEndGame/wingame.gif").convert_alpha()
    the=pygame.image.load("asset/BomberEndGame/Draw.gif").convert_alpha()
    if i==1:
        the = pygame.image.load("asset/BomberEndGame/Player 1 Wins.gif").convert_alpha()
    elif i==2:
        the = pygame.image.load("asset/BomberEndGame/Player 4 Wins.gif").convert_alpha()
    while True:
        SCREEN.fill((125,155,255))
        SCREEN.blit(BGEG, (0, 0))
        if i==1 or i==2:
            SCREEN.blit(the, (400, 0))
            MENU_TEXT = get_font(50).render(msg, True, "#111111")
            MENU_RECT = MENU_TEXT.get_rect(center=(655, 300))
        else:
            SCREEN.blit(the, (400, 200))
            MENU_TEXT = get_font(50).render(msg, True, "#111111")
            MENU_RECT = MENU_TEXT.get_rect(center=(655, 100))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("asset/menu/but.gif"),(300,100)), pos=(500, 610), 
                            text_input="Back", font=get_font(19), base_color="#CCFFFF", hovering_color="White")
        AGAIN_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("asset/menu/but.gif"),(300,100)), pos=(800, 610), 
                            text_input="Play AGain", font=get_font(19), base_color="#CCFFFF", hovering_color="White")
        for button in [QUIT_BUTTON,AGAIN_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                if AGAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Twoplay()
        pygame.display.update()
def Wingame(i,msg):
    mixer.music.load('asset/sound/WIN.mp3')
    mixer.music.play()
    mixer.music.set_volume(vollum)
    while True:
        SCREEN.fill((125,155,255))
        SCREEN.blit(BGwin, (0, 0))
        MENU_TEXT = get_font(50).render(msg, True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(655, 100))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        QUIT_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("asset/menu/but.gif"),(300,100)), pos=(500, 610), 
                            text_input="Back", font=get_font(19), base_color="#CCFFFF", hovering_color="White")
        AGAIN_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("asset/menu/but.gif"),(300,100)), pos=(800, 610), 
                            text_input="Play AGain", font=get_font(19), base_color="#CCFFFF", hovering_color="White")
        for button in [QUIT_BUTTON,AGAIN_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                if AGAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if i==1:
                        Campaign()
                    elif i==2:
                        Oneplay()
                    elif i==3:
                        Twoplay()
        pygame.display.update()

def ONvolume(value,s):
    global vollum
    if value[1]==1:
        vollum=0
    else:
        vollum=30
    mixer.music.set_volume(vollum)
def options():
    SCREEN = pygame.display.set_mode((1280, 700))
    menu = pygame_menu.Menu('OPTIONS', 1280, 700,
                    theme=pygame_menu.themes.THEME_BLUE)
    menu.add.selector('Soundtrack', [('ON', 1), ('OFF', 2)], onchange=ONvolume)
    menu.add.button('QUIT', main_menu)
    menu.mainloop(SCREEN)

def sellectMode():
    BG = pygame.image.load("asset/menu/taigameboom.gif")
    the=  pygame.image.load("asset/menu/td.gif")
    while True:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(the, (40, -140))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("Sellect Mode", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(655, 100))

        
        Campaign_BUTTON = Button(image=pygame.image.load("asset/menu/but.gif"), pos=(640, 250), 
                            text_input="Campaign", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        OnePlay_BUTTON = Button(image=pygame.image.load("asset/menu/but.gif"), pos=(640, 370), 
                            text_input="1 player", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        TwoPlay_BUTTON = Button(image=pygame.image.load("asset/menu/but.gif"), pos=(640, 490), 
                            text_input="2 player", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        Back_BUTTON = Button(image=pygame.image.load("asset/menu/but.gif"), pos=(640, 610), 
                            text_input="Back", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [Campaign_BUTTON,OnePlay_BUTTON, TwoPlay_BUTTON,Back_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Campaign_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Campaign()
                if OnePlay_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Oneplay()
                if TwoPlay_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Twoplay()
                if Back_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
        pygame.display.update()
def StartRoomLan():
    Game.isclient=False
    Game.server.PORT=random.randint(3000,9000)
    # SCREEN = pygame.display.set_mode((1280, 700))
    menu = pygame_menu.Menu('Watting for connecting...', 1280, 700,
                        theme=pygame_menu.themes.THEME_BLUE)
    Game.server.OnConnect+=ConnectedClient
    Game.Connect()
    menu.add.label(Game.msgconnect)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    Game.HOST=ip_address
    menu.add.button('Reload', ReadyGame)
    menu.add.label("IP ADDRESS:"+ip_address)
    menu.add.label("PORT:"+str(Game.server.PORT))
    menu.add.button('Back', sellectLan)

    

    menu.mainloop(SCREEN)
def ReadyGame():
    menu = pygame_menu.Menu(Game.msgconnect, 1280, 700,
                        theme=pygame_menu.themes.THEME_BLUE)
    Game.server.OnConnect+=ConnectedClient
    if not Game.isclient:
        Game.Connect()
    menu.add.label(Game.msgconnect)
    menu.add.label("IP ADDRESS:"+Game.HOST)
    menu.add.label("PORT:"+str(Game.server.PORT))
    
    if(Game.Connected):
        menu.add.button('Play',sendMsGPL)
    else:
        menu.add.button('Reload', ReadyGame)
    menu.add.button('Back', sellectLan)
    menu.mainloop(SCREEN)
def sendMsGPL():
    Game.startgame()
    while True:
       
        Game.ingameLOGIC()
        Game.drawWindow(SCREEN)
        if Game.checkWin():
            EndGame(Game.win,Game.msg)
        if Game.checkGameOver():
            EndGame(Game.win,Game.msg)
def createRoom():
    # SCREEN = pygame.display.set_mode((1280, 700))
    menu = pygame_menu.Menu('Create ROOM', 1280, 700,
                        theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button("Create Room",StartRoomLan)
    menu.add.button('Back', sellectLan)
    

    menu.mainloop(SCREEN)
def handleInputIP(value):
    Game.HOST=value
    print(IP)
def handleInputHOST(value):
    Game.PORT=value
    print(P)
def JoinRoomLan():
    Game.isclient=True
    SCREEN = pygame.display.set_mode((1280, 700))
    menu = pygame_menu.Menu('Watting for connecting...', 1280, 700,
                        theme=pygame_menu.themes.THEME_BLUE)
    Game.createClient()
    Game.client.OnConnect+=ConnectedClient
    Game.Connect()
    menu.add.label(Game.msgconnect)
    menu.add.button('Reload', ReadyGame)
    menu.add.label("IP ADDRESS:"+str(Game.HOST))
    menu.add.label("PORT:"+str(Game.PORT))
    menu.add.button('Back', sellectLan)

    menu.mainloop(SCREEN)
def ConnectedClient():
    Game.Connected=True


def JoinRoom():
    SCREEN = pygame.display.set_mode((1280, 700))
    menu = pygame_menu.Menu('JOIN ROOM', 1280, 700,
                        theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input("IP Server:",onchange=handleInputIP)
    menu.add.text_input("PORT:",onchange=handleInputHOST)
    menu.add.button("CONNECT TO SERVER",JoinRoomLan)
    menu.add.button('Back', sellectLan)

    menu.mainloop(SCREEN)
def sellectLan():
    BG = pygame.image.load("asset/menu/taigameboom.gif")
    the=  pygame.image.load("asset/menu/td.gif")
    while True:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(the, (40, -140))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("Create room", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(655, 100))

        
        ROOMCreate_BUTTON = Button(image=pygame.image.load("asset/menu/but.gif"), pos=(640, 250), 
                            text_input="Create", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        Join_BUTTON = Button(image=pygame.image.load("asset/menu/but.gif"), pos=(640, 370), 
                            text_input="Join", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        Back_BUTTON = Button(image=pygame.image.load("asset/menu/but.gif"), pos=(640, 610), 
                            text_input="Back", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [ROOMCreate_BUTTON,Join_BUTTON,Back_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ROOMCreate_BUTTON.checkForInput(MENU_MOUSE_POS):
                    createRoom()
                if Join_BUTTON.checkForInput(MENU_MOUSE_POS):
                    JoinRoom()
                if Back_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
        pygame.display.update()
def main_menu():
    
    clock.tick(FPS)
    while True:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(the, (40, -140))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("BOOMMAN GAME", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(655, 100))

        LAN_BUTTON = Button(image=pygame.image.load("asset/menu/but.gif"), pos=(640, 250), 
                            text_input="PLAY&LAN", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        PLAY_BUTTON = Button(image=pygame.image.load("asset/menu/but.gif"), pos=(640, 370), 
                            text_input="PLAY", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("asset/menu/but.gif"), pos=(640, 490), 
                            text_input="OPTIONS", font=get_font(30), base_color="#CCFFFF", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("asset/menu/but.gif"), pos=(640, 610), 
                            text_input="QUIT", font=get_font(30), base_color="#CCFFFF", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [LAN_BUTTON,PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LAN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sellectLan()
                    #sendMsGPL()
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    sellectMode()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()

main_menu()