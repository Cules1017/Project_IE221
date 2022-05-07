from msilib.schema import Class
import pygame
import sys
from boomman import *
from mapgame import *
from pygame import mixer
from enemy import*
from baner import*
from AutoPlay import*
import random

map1=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,0,0,2,0,0,3,0,4,0,0,2,0,0,1],
    [1,0,2,4,2,0,0,0,2,0,3,0,0,0,0,0,0,2,0,2,1],
    [1,0,2,2,2,0,2,0,2,0,0,3,0,0,0,2,2,4,0,2,1],
    [1,0,0,0,0,0,0,2,0,2,2,2,0,0,0,0,0,0,0,2,1],
    [1,0,2,2,0,0,0,0,0,2,0,2,0,0,0,3,2,2,0,0,1],
    [1,0,2,0,0,0,3,0,0,2,2,2,2,0,0,4,0,0,0,0,1],
    [1,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,1],
    [1,0,0,0,0,0,2,0,0,0,2,0,2,0,0,0,0,0,0,0,1],
    [1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,2,0,0,4,0,1],
    [1,0,2,0,0,4,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
class game():
    def __init__(self):
        self.Player1=None
        self.Player2=None
        self.Player3=None
        self.Player4=None
        
        self.map=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,0,0,2,0,0,3,0,4,0,0,0,0,0,1],
    [1,0,0,4,2,0,0,0,2,0,3,0,0,0,0,0,0,2,0,2,1],
    [1,0,0,2,2,0,2,0,2,0,0,3,0,0,0,2,2,4,0,2,1],
    [1,0,0,0,0,0,0,2,0,2,2,2,0,0,0,0,0,0,0,2,1],
    [1,0,2,2,0,0,0,0,0,2,0,2,0,0,0,3,2,2,0,0,1],
    [1,0,2,0,0,0,3,0,0,2,2,2,2,0,0,4,0,0,0,0,1],
    [1,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,1],
    [1,0,0,0,0,0,2,0,0,0,2,0,2,0,0,0,0,0,0,0,1],
    [1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,2,0,0,4,0,1],
    [1,0,2,0,0,4,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
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
        self.mapGame.filemap=self.map
        self.Panel_Pl2=None
        self.Panel_Pl3=None
        self.Panel_Pl4=None
        self.pointWin=10
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
        self.Player1.update(0.01)
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
        self.Panel_Pl3.y+=150
        self.Panel_Pl4=BanerInfoBot(self.Player4,self.map)
        self.Panel_Pl4.y+=250
        self.pointWin=100
        self.mapGame=Mapgame()
        self.mapGame.filemap=map1
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
        if self.pointWin<=self.Player2.point:
            return True
        if self.pointWin<=self.Player3.point:
            return True
        if self.pointWin<=self.Player4.point:
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
        self.pointWin=100
        self.mapGame=Mapgame()
        self.mapGame.filemap=map1
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
            return True
        if self.pointWin<=self.Player2.point:
            return True
        if self.pointWin<=self.Player3.point:
            return True
        if self.pointWin<=self.Player4.point:
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

