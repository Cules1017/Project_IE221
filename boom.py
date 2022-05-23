import pygame
from exploy import *
import random

class Boom(pygame.sprite.Sprite):
    '''Bomm trong game
        self.X=tọa độ x của boom
        self.Y=tọa độ y của boom
        self.power_explo: độ lớn của vụ nổ
        self.WIDTH=kích thước của bomm
        self.HEIGHT=kích thước của bomm
        self.time=Thời gian boom bắt đầu nổ
        self.exploy_boom=Vụ nổ gây ra
        self.sound : âm thanh boom nổ


        self.boom_animation: hoạt ảnh bom đang cháy
    '''
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.X=pos_x
        self.Y=pos_y
        self.power_explo=1
        self.WIDTH=50
        self.HEIGHT=50
        self.time=None
        self.exploy_boom=None
        self.sound = pygame.mixer.Sound('asset/sound/bigbang.mp3')


        self.boom_animation=[]

        #animation run_top 0->2 ⬆️
        self.boom_animation.append(pygame.image.load('asset/boom/1.png').convert_alpha())
        self.boom_animation.append(pygame.image.load('asset/boom/2.png').convert_alpha())
        self.boom_animation.append(pygame.image.load('asset/boom/3.png').convert_alpha())

        self.current_animation = 0
        self.image = pygame.transform.smoothscale( self.boom_animation[0], (self.WIDTH,self.HEIGHT))
        #rectangle collision
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]
    def destroyPL(self,player):
        '''
        Boom tác động trừ máu player
        trừ 20 máu mỗi lần trúng
        '''
        if self.exploy_boom!=None:
            #print(player.name)
            if self.exploy_boom.rect.colliderect(player):
                player.being_attacked(20)
    def destroy(self, barri,player):
        '''
        Phá hủy
        Phá hủy , tiêu diệt quái 
        đồng thời tính toán cho phép các vật phẩm rơi ra
        '''
        # print(self.exploy_boom!=None )
        if self.exploy_boom!=None:
            #print(player.name)
            if self.exploy_boom.rect.colliderect(player):
                player.being_attacked(20)
            index=self.exploy_boom.rect.collidelist(barri.Barri2)
            index_eneLR=self.exploy_boom.rect.collidelist(barri.fireLR)
            index_eneBT=self.exploy_boom.rect.collidelist(barri.fireBT)
            if index_eneBT!=-1:
                player.point+=1
                print(player.name)
                x=int(barri.fireBT[index_eneBT].X/50)
                y=int(barri.fireBT[index_eneBT].Y/50) 
                barri.filemap[y][x]=random.randint(15,22)
                barri.fireBT.remove(barri.fireBT[index_eneBT])
            if index_eneLR!=-1:
                player.point+=1
                print(player.name)
                x=int(barri.fireLR[index_eneLR].X/50)
                y=int(barri.fireLR[index_eneLR].Y/50) 
                barri.filemap[y][x]=random.randint(15,22)
                barri.fireLR.remove(barri.fireLR[index_eneLR])
            if index!=-1:
                x=int(barri.Barri2[index].X/50)
                y=int(barri.Barri2[index].Y/50)
                barri.filemap[y][x]=random.randint(5,13)
                barri.Barri2.remove(barri.Barri2[index])
            #self.exploy_boom=None
                
    def update(self,second,screen):
        '''
        Update
        Kiểm tra thời gian boom nổ
        cho phép xảy ra vụ nổ 
        qui định cái hoạt ảnh boom nổ
        '''
        if self.time is not None:
            if pygame.time.get_ticks() - self.time >= 1700:
                self.exploy_boom=boom1_exploy(self.X,self.Y,self.power_explo)
                self.exploy_boom.draw(screen)
            if pygame.time.get_ticks() - self.time >= 1800:
                self.exploy_boom=None
                self.kill()
        self.current_animation+=second
        if int(self.current_animation) >= len(self.boom_animation):
                self.current_animation=0
        self.image = pygame.transform.smoothscale(self.boom_animation[int(self.current_animation)], (self.WIDTH,self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]
class BoomPlayLan(Boom):
    '''Boom trong màn chơi qua LAN'''
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
    def destroy(self, barri,player):
        # print(self.exploy_boom!=None )
        if self.exploy_boom!=None:
            #print(player.name)
            if self.exploy_boom.rect.colliderect(player):
                player.being_attacked(20)
            index=self.exploy_boom.rect.collidelist(barri.Barri2)
            index_eneLR=self.exploy_boom.rect.collidelist(barri.fireLR)
            index_eneBT=self.exploy_boom.rect.collidelist(barri.fireBT)
            if index_eneBT!=-1:
                player.point+=1
                print(player.name)
                x=int(barri.fireBT[index_eneBT].X/50)
                y=int(barri.fireBT[index_eneBT].Y/50) 
                barri.filemap[y][x]=0
                barri.fireBT.remove(barri.fireBT[index_eneBT])
            if index_eneLR!=-1:
                player.point+=1
                print(player.name)
                x=int(barri.fireLR[index_eneLR].X/50)
                y=int(barri.fireLR[index_eneLR].Y/50) 
                barri.filemap[y][x]=0
                barri.fireLR.remove(barri.fireLR[index_eneLR])
            if index!=-1:
                x=int(barri.Barri2[index].X/50)
                y=int(barri.Barri2[index].Y/50)
                barri.filemap[y][x]=0
                barri.Barri2.remove(barri.Barri2[index])