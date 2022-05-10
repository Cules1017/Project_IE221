import imp
from barrier import *
from enemy import*
from item import*
import pygame

class Mapgame():
    '''Bản đồ của game
    render ra quái vật phẩm,....
        #TYPE 0: nền có thể di chuyển qua
        #TYPE 1: Vật thể cứng không thể di chuyển qua, có thể phá hủy theo heath
        #TYPE 2: Vật thể cứng kh thể di chuyển không thể phá hủy
        #type 3: Quái vật di chuyển làm  mất máu của player di chuyển trái phải
        #type 4: Quái vật di chuyển làm  mất máu của player di chuyển trên xuống
        #type 5: Cấp cứu hồi đầy máu cho nhân vật
        #type 6: Thuốc quí tăng 1.5 máu cho nhân vật
        #type 7: tăng tốc chạy cho nhân vật
        #Type 8: tặng cho player thêm boom
        #type 9: tường đá không thể phá
        #Type 19: tặng coin vàng +2 point
        #type 20: tặng coin bạc +1 point
        #type 21: tặng sao +5 point
    '''
    def __init__(self):
        self.filemap=None
        self.Barri0=[]
        self.Barri1=[]
        self.Barri2=[]
        self.fireLR=[]
        self.fireBT=[]
        self.item=[]
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
        self.item=[]
        for row in range(len(self.filemap)):
            for col in range(len(self.filemap[row])):
                if(self.filemap[row][col]==1):
                    temp1=Stone(col*50,row*50)
                    temp1.draw(screen,col,row)
                    self.Barri1.append(temp1)
                elif(self.filemap[row][col]==2):
                    temp2=Brick(col*50,row*50)
                    temp2.draw(screen,col,row)
                    self.Barri2.append(temp2)
                elif(self.filemap[row][col]==5):
                    temp0=Sandgrey_bg(col*50,row*50)
                    temp0.draw(screen,col,row)
                    temp=emergency(col*50,row*50)
                    temp.draw(screen,col,row)
                    self.item.append(temp)
                elif(self.filemap[row][col]==6):
                    temp0=Sandgrey_bg(col*50,row*50)
                    temp0.draw(screen,col,row)
                    temp=dulicate(col*50,row*50)
                    temp.draw(screen,col,row)
                    self.item.append(temp)
                elif(self.filemap[row][col]==7):
                    temp0=Sandgrey_bg(col*50,row*50)
                    temp0.draw(screen,col,row)
                    temp=speed(col*50,row*50)
                    temp.draw(screen,col,row)
                    self.item.append(temp)
                elif(self.filemap[row][col]==8):
                    temp0=Sandgrey_bg(col*50,row*50)
                    temp0.draw(screen,col,row)
                    temp=addbomm(col*50,row*50)
                    temp.draw(screen,col,row)
                    self.item.append(temp)
                elif(self.filemap[row][col]==9):
                    temp1=Stone1(col*50,row*50)
                    temp1.draw(screen,col,row)
                    self.Barri1.append(temp1)
                elif(self.filemap[row][col]==19):
                    temp0=Sandgrey_bg(col*50,row*50)
                    temp0.draw(screen,col,row)
                    temp=coin_gold(col*50,row*50)
                    temp.draw(screen,col,row)
                    self.item.append(temp)
                elif(self.filemap[row][col]==20):
                    temp0=Sandgrey_bg(col*50,row*50)
                    temp0.draw(screen,col,row)
                    temp=coin_silver(col*50,row*50)
                    temp.draw(screen,col,row)
                    self.item.append(temp)
                elif(self.filemap[row][col]==21):
                    temp0=Sandgrey_bg(col*50,row*50)
                    temp0.draw(screen,col,row)
                    temp=coin_star(col*50,row*50)
                    temp.draw(screen,col,row)
                    self.item.append(temp)
                else:
                    temp0=Sandgrey_bg(col*50,row*50)
                    temp0.draw(screen,col,row)
                    self.Barri0.append(temp0)
class MapgameLAN(Mapgame):
    def __init__(self):
        super().__init__()
    def render_enemy(self):
        for row in range(len(self.filemap)):
            for col in range(len(self.filemap[row])):
                if(self.filemap[row][col]==3):
                    temp=fire_LR(col*50,row*50)
                    temp.image=pygame.transform.scale(pygame.image.load('asset/enemy/Fire/F1.gif'),(temp.WIDTH,temp.HEIGHT))
                    self.fireLR.append(temp)
                elif(self.filemap[row][col]==4):
                    temp=fire_TB(col*50,row*50)
                    temp.image=pygame.transform.scale(pygame.image.load('asset/enemy/Fire/F1.gif'),(temp.WIDTH,temp.HEIGHT))
                    self.fireBT.append(temp)
    