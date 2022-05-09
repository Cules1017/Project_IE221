from msilib.schema import Class
from select import select
import pygame
import sys
from boomman import *
from mapgame import *
from pygame import mixer
from enemy import*
from baner import*
from AutoPlay import*
import random
from serve import *
from client import*
from button import*

map1=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,0,0,2,0,0,3,0,4,0,0,2,0,0,1],
    [1,0,2,4,2,0,0,0,2,0,3,0,0,0,0,0,0,2,0,2,1],
    [1,0,2,2,2,0,2,0,2,0,0,3,0,0,0,2,2,4,0,2,1],
    [1,9,9,0,0,0,0,2,0,2,2,2,0,9,0,0,0,0,0,2,1],
    [1,0,2,2,0,0,0,9,0,2,0,2,0,0,0,3,2,2,0,0,1],
    [1,0,2,0,0,0,3,0,0,2,2,2,2,0,0,4,0,0,0,0,1],
    [1,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,1],
    [1,0,0,0,0,0,2,0,0,0,2,0,2,0,0,0,0,0,0,0,1],
    [1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,2,0,0,4,0,1],
    [1,0,2,0,0,4,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
map2=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1],
    [1,0,0,0,0,0,0,9,0,0,0,0,0,0,0,9,0,0,0,0,1],
    [1,0,2,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,4,0,1],
    [1,0,0,4,0,2,0,0,0,0,4,0,0,0,0,2,0,0,0,0,1],
    [1,0,4,0,0,2,0,0,2,2,2,2,2,0,0,9,0,0,0,0,1],
    [1,0,0,4,0,0,0,0,2,0,4,0,2,0,0,9,0,0,3,0,1],
    [1,0,0,4,0,2,0,0,2,2,2,2,2,0,0,2,0,0,0,0,1],
    [1,0,0,0,0,2,0,0,0,0,4,0,0,0,0,2,0,0,0,0,1],
    [1,0,0,4,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1],
    [1,0,0,0,0,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
class game():
    def __init__(self):
        self.Player1=None
        self.Player2=None
        self.Player3=None
        self.Player4=None
        self.map=[map1,map2]
        # self.Panel_Pl1=BanerInfo(self.Player1,self.map)
        # self.Panel_Pl2=BanerInfoBot(self.Player2,self.map)
        # self.Panel_Pl3=BanerInfoBot(self.Player3,self.map)
        # self.Panel_Pl4=BanerInfoBot(self.Player3,self.map)
        # self.Panel_Pl3.y+=100
        # self.Panel_Pl4.y+=100
        
        self.GameOver=False
        self.pointWin=100
        self.mapGame=Mapgame()
        self.mapGame.filemap=self.map
                    
class Kill_mons(game):
    def __init__(self):
        super().__init__()
        self.Player1=Player(50,50)
        self.Panel_Pl1=BanerInfo(self.Player1,self.map)
        self.mapGame=Mapgame()
        i=random.randint(0,1)
        self.mapGame.filemap=self.map[i]
        self.Panel_Pl2=None
        self.Panel_Pl3=None
        self.Panel_Pl4=None
        self.pointWin=10 #10
    def ingameLOGIC(self):

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYUP:
                if self.Player1.action!=5:
                    self.Player1.action=0
            if event.type==pygame.KEYDOWN:
                self.Player1.put_boom(event)
        self.Player1.move(self.mapGame)
        self.Player1.update(0.0009)
        if self.Player1.checkdie():
            self.Player1.speed=0
            
    def checkWin(self):
        if self.pointWin<=self.Player1.point:
            return True
    def checkGameOver(self):
        if self.pointWin>self.Player1.point and self.Player1.boom_real==0:
            return True
        if self.Player1.checkdie():
            return True
    def startgame(self):
        self.mapGame.render_enemy()
    def drawWindow(self,screen):
        screen.fill((125,155,255))
        self.mapGame.draw(screen)
        self.Player1.draw(screen)
        self.mapGame.draw_enemy(screen,self.mapGame)
        self.Panel_Pl1.draw(screen)
        self.Panel_Pl1.update(self.Player1)
        pygame.display.flip()
        pygame.display.update()
class GameOnePL_PC(game):
    def __init__(self):
        super().__init__()
        self.Player1=Player(50,50)
        self.Player2=autoplay(950,50)
        self.Player3=autoPlay1(50,600)
        self.Player4=autoPlay2(950,600)
        self.Panel_Pl1=BanerInfo(self.Player1,self.map)
        self.Panel_Pl2=BanerInfoBot(self.Player2,self.map)
        self.Panel_Pl3=BanerInfoBot(self.Player3,self.map)
        self.Panel_Pl3.y+=130
        self.Panel_Pl4=BanerInfoBot(self.Player4,self.map)
        self.Panel_Pl4.y+=260
        self.pointWin=10
        self.msg=''
        self.mapGame=Mapgame()
        i=random.randint(0,1)
        self.mapGame.filemap=self.map[i]
    def ingameLOGIC(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYUP:
                if self.Player1.action!=5:
                    self.Player1.action=0
            if event.type==pygame.KEYDOWN:
                self.Player1.put_boom(event)
        #Player 1
        self.Player1.move(self.mapGame,self.Player2,self.Player3,self.Player4)
        self.Player1.update(0.01)
        #Player 2
        self.Player2.automove(self.mapGame,self.Player1,self.Player3,self.Player4)
        self.Player2.update(0.01)
        #Player 3
        self.Player3.automove(self.mapGame,self.Player2,self.Player1,self.Player4)
        self.Player3.update(0.01)
        #Player 4
        self.Player4.automove(self.mapGame,self.Player2,self.Player3,self.Player1)
        self.Player4.update(0.01)
        if self.Player1.checkdie():
            self.Player1.speed=0
            
    def checkWin(self):
        if self.pointWin<=self.Player1.point:
            return True
        
    def checkGameOver(self):
        if self.Player2.checkdie():
            
            self.Player2.kill()
        if self.Player3.checkdie():
            
            self.Player3.kill()
        if self.Player4.checkdie():
            
            self.Player4.kill()
        if self.pointWin>self.Player1.point and self.Player1.boom_real==0:
            self.msg='Not enough pass points'
            return True
        if self.Player1.checkdie():
            self.msg='YOU DIE'
            return True
        if self.pointWin<=self.Player2.point:
            self.msg=self.Player2.name+' WinGame'
            return True
        if self.pointWin<=self.Player3.point:
            self.msg=self.Player3.name+' WinGame'
            return True
        if self.pointWin<=self.Player4.point:
            self.msg=self.Player4.name+' WinGame'
            return True
    def startgame(self):
        self.mapGame.render_enemy()
    def drawWindow(self,screen):
        screen.fill((125,155,255))
        self.mapGame.draw(screen)
        self.Player1.draw(screen)
        for Playeri in [self.Player2,self.Player3,self.Player4]:
            if Playeri.heath>0:
                Playeri.draw(screen)
            elif Playeri.heath<=0:
                Playeri.X=0
                Playeri.Y=0
                Playeri.rect.topleft= [0,0]
                Playeri.heath=0
                Playeri.boom_num=0
                Playeri.boom_real=0
        self.mapGame.draw_enemy(screen,self.mapGame)
        self.Panel_Pl1.draw(screen)
        self.Panel_Pl1.update(self.Player1)
        self.Panel_Pl2.draw(screen)
        self.Panel_Pl2.update(self.Player2)
        self.Panel_Pl3.draw(screen)
        self.Panel_Pl3.update(self.Player3)
        self.Panel_Pl4.draw(screen)
        self.Panel_Pl4.update(self.Player4)
        pygame.display.flip()
        pygame.display.update()


class GameTwoPL(game):
    def __init__(self):
        super().__init__()
        self.Player1=Player(50,50)
        self.Player2=PlayerTwo(950,50)
        self.Player3=autoPlay1(50,600)
        self.Player4=autoplay(950,600)
        self.Panel_Pl1=BanerInfo(self.Player1,self.map)
        self.Panel_Pl2=BanerInfoBot(self.Player2,self.map)
        self.Panel_Pl3=BanerInfoBot(self.Player3,self.map)
        self.Panel_Pl3.y+=130
        self.Panel_Pl4=BanerInfoBot(self.Player4,self.map)
        self.Panel_Pl4.y+=260
        self.pointWin=1
        self.msg=''
        self.mapGame=Mapgame()
        i=random.randint(0,1)
        self.mapGame.filemap=self.map[i]
    def ingameLOGIC(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYUP:
                if self.Player1.action!=5:
                    self.Player1.action=0
                if self.Player2.action!=5:
                    self.Player2.action=0
            if event.type==pygame.KEYDOWN:
                self.Player1.put_boom(event)
                self.Player2.put_boom(event)
        #Player 1
        self.Player1.move(self.mapGame,self.Player2,self.Player3,self.Player4)
        self.Player1.update(0.01)
        #Player 2
        self.Player2.move(self.mapGame,self.Player1,self.Player3,self.Player4)
        self.Player2.update(0.01)
        #Player 3
        self.Player3.automove(self.mapGame,self.Player2,self.Player1,self.Player4)
        self.Player3.update(0.01)
        #Player 4
        self.Player4.automove(self.mapGame,self.Player2,self.Player3,self.Player1)
        self.Player4.update(0.01)
        if self.Player1.checkdie():
            self.Player1.speed=0
            
    def checkWin(self):
        if self.pointWin<=self.Player1.point:
            self.msg=self.Player1.name+"WIN GAME"
            return True
        if self.pointWin<=self.Player2.point:
            self.msg=self.Player2.name+"WIN GAME"
            return True
        
        
    def checkGameOver(self):
        if self.pointWin<=self.Player3.point:
            self.msg=self.Player3.name+"WIN GAME"
            return True
        if self.pointWin<=self.Player4.point:
            self.msg=self.Player1.name+"WIN GAME"
            return True
        if self.pointWin>self.Player1.point and self.Player1.boom_real==0:
            return True
        if self.pointWin>self.Player2.point and self.Player2.boom_real==0:
            return True
        if self.Player1.checkdie() and self.Player2.checkdie():
            return True
        if self.Player3.checkdie():
            self.Player3.kill()
        if self.Player4.checkdie():
            self.Player4.kill()
    def startgame(self):
        self.mapGame.render_enemy()
    def drawWindow(self,screen):
        screen.fill((125,155,255))
        self.mapGame.draw(screen)
        self.Player1.draw(screen)
        self.Player2.draw(screen)
        self.Player3.draw(screen)
        self.Player4.draw(screen)
        self.mapGame.draw_enemy(screen,self.mapGame)
        self.Panel_Pl1.draw(screen)
        self.Panel_Pl1.update(self.Player1)
        self.Panel_Pl2.draw(screen)
        self.Panel_Pl2.update(self.Player2)
        self.Panel_Pl3.draw(screen)
        self.Panel_Pl3.update(self.Player3)
        self.Panel_Pl4.draw(screen)
        self.Panel_Pl4.update(self.Player4)
        pygame.display.flip()
        pygame.display.update()

class PlayLan(game):
    def __init__(self):
        super().__init__()
        self.player=Player(50,600)
        self.ortherplayer=PlayerLan(950,600,0)
        self.Panel_Pl1=BanerInfo(self.player,self.mapGame)
        self.Panel_Pl2=BanerInfoBot(self.ortherplayer,self.mapGame)
        self.Panel_Pl2.y+=200
        self.pointWin=100
        self.mapGame=Mapgame()
        self.mapGame.filemap=map1
        self.HOST='Host'
        self.PORT=5
        self.isclient='isClient '
        self.Connected=False  
        self.msgconnect="Watting for connecting..."
        self.server=Server()
        self.server.AddSubscribersForLockBrokenEvent(self.handleLan)
    def createClient(self):
        self.client=Client(self.HOST,int(self.PORT))
        self.client.AddSubscribersForLockBrokenEvent(self.handleLan)   
    def Connect(self):    
        if self.isclient:
            self.client.ConnectToServer()
        else:
            self.player=Player(950,600)
            self.ortherplayer=PlayerLan(50,600,0)
            self.server.startServer()
    def handleLan(self):
        if( self.server.Datagame.move_i==1 and   self.ortherplayer.X>=60):
             self.ortherplayer.walk_Left_Right(-0.25)
             self.ortherplayer.action=3
        elif( self.server.Datagame.move_i==2 and  self.ortherplayer.X<=950):
             self.ortherplayer.walk_Left_Right(0.25)
             self.ortherplayer.action=4
        elif( self.server.Datagame.move_i==3 and  self.ortherplayer.Y>=55):
             self.ortherplayer.walk_TopBottom(-0.25)
             self.ortherplayer.action=1
        elif( self.server.Datagame.move_i==4 and  self.ortherplayer.Y<=605):
             self.ortherplayer.walk_TopBottom(0.25)
             self.ortherplayer.action=2
        if( self.server.Datagame.put_boom==1):
             self.ortherplayer.put_boom()
        if( self.client.Datagame.move_i==1 and   self.ortherplayer.X>=60):
             self.ortherplayer.walk_Left_Right(-0.25)
             self.ortherplayer.action=3
        elif( self.client.Datagame.move_i==2 and  self.ortherplayer.X<=950):
             self.ortherplayer.walk_Left_Right(0.25)
             self.ortherplayer.action=4
        elif( self.client.Datagame.move_i==3 and  self.ortherplayer.Y>=55):
             self.ortherplayer.walk_TopBottom(-0.25)
             self.ortherplayer.action=1
        elif( self.client.Datagame.move_i==4 and  self.ortherplayer.Y<=605):
             self.ortherplayer.walk_TopBottom(0.25)
             self.ortherplayer.action=2
        if( self.client.Datagame.put_boom==1):
             self.ortherplayer.put_boom()
        if( self.client.Datagame.put_boom==5):
            self.msgconnect="Connected to Server..."
            print(self.msgconnect)

    def ingameLOGIC(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYUP:
                if self.player.action!=5:
                    self.player.action=0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if len(self.player.boom)<=self.player.boom_num:
                        if self.isclient:
                            self.client.sendData(Data=SocketData(5,1))
                        else:
                            self.server.sendData(Data=SocketData(5,1))
                        self.player.put_boom(event)
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]:
            if self.isclient:
                self.client.sendData(Data=SocketData(1,0))
            else:
                self.server.sendData(Data=SocketData(1,0))
        elif keys[pygame.K_RIGHT]:
            if self.isclient:
                self.client.sendData(Data=SocketData(2,0))
            else:
                self.server.sendData(Data=SocketData(2,0))
        elif keys[pygame.K_UP]:
            if self.isclient:
                self.client.sendData(Data=SocketData(3,0))
            else:
                self.server.sendData(Data=SocketData(3,0))
        elif keys[pygame.K_DOWN]:
            if self.isclient:
                self.client.sendData(Data=SocketData(4,0))
            else:
                self.server.sendData(Data=SocketData(4,0))
        self.player.move(self.mapGame,self.ortherplayer)
        self.ortherplayer.move(self.mapGame,self.player)
        self.player.update(0.01)
        self.ortherplayer.update(0.01)
            
    def checkWin(self):
        pass
    def checkGameOver(self):
        if self.pointWin>self.player.point and self.player.boom_real==0:
            return True
        if self.player.checkdie():
            return True
    def startgame(self):
        self.mapGame.render_enemy()
    def drawWindow(self,screen):
        screen.fill((125,155,255))
        self.mapGame.draw(screen)
        self.player.draw(screen)
        self.ortherplayer.draw(screen)
        self.mapGame.draw_enemy(screen,self.mapGame)
        self.Panel_Pl1.draw(screen)
        self.Panel_Pl1.update(self.player)
        self.Panel_Pl2.draw(screen)
        self.Panel_Pl2.update(self.ortherplayer)       
        pygame.display.flip()
        pygame.display.update()