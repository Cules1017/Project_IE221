from barrier import *
from enemy import*
import pygame

class Mapgame():
    def __init__(self):
        self.filemap=None
        #TYPE 0: nền có thể di chuyển qua
        #TYPE 1: Vật thể cứng không thể di chuyển qua, có thể phá hủy theo heath
        #TYPE 2: Vật thể cứng kh thể di chuyển không thể phá hủy
        #type 3: Quái vật di chuyển làm  mất máu của player di chuyển trái phải
        #type 4: Quái vật di chuyển làm  mất máu của player di chuyển trên xuống
        self.Barri0=[]
        self.Barri1=[]
        self.Barri2=[]
        self.fireLR=[]
        self.fireBT=[]
    def render_enemy(self):
        for row in range(len(self.filemap)):
            for col in range(len(self.filemap[row])):
                if(self.filemap[row][col]==3):
                    temp=fire_LR(col*50,row*50)
                    self.fireLR.append(temp)
                elif(self.filemap[row][col]==4):
                    temp=fire_TB(col*50,row*50)
                    self.fireBT.append(temp)
    def draw_enemy(self,screen,map):
        for i in self.fireLR:
            i.draw(screen,map)
        for e in self.fireBT:
            e.draw(screen,map)
    def draw(self,screen):
        self.Barri0=[]
        self.Barri1=[]
        self.Barri2=[]
        for row in range(len(self.filemap)):
            for col in range(len(self.filemap[row])):
                if(self.filemap[row][col]==0 or self.filemap[row][col]==3 or self.filemap[row][col]==4):
                    temp0=Sandgrey_bg(col*50,row*50)
                    temp0.draw(screen,col,row)
                    self.Barri0.append(temp0)
                elif(self.filemap[row][col]==1):
                    temp1=Stone(col*50,row*50)
                    temp1.draw(screen,col,row)
                    self.Barri1.append(temp1)
                elif(self.filemap[row][col]==2):
                    temp2=Brick(col*50,row*50)
                    temp2.draw(screen,col,row)
                    self.Barri2.append(temp2)
                # elif(self.filemap[row][col]==3):
                #     temp0=Sandgrey_bg(col*50,row*50)
                #     temp0.draw(screen,col,row)
                #     self.Barri0.append(temp0)
                # elif(self.filemap[row][col]==4):
                #     temp0=Sandgrey_bg(col*50,row*50)
                #     temp0.draw(screen,col,row)
                #     self.Barri0.append(temp0)