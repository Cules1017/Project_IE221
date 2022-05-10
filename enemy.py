import pygame
import random

from boomman import Player

#with action value 1:UP 2:DOWN 3:LEFT 4:RIGHT
class fire():
    '''Quái vật trong game
    Làm mất máu
    có thể sinh ra tiền sau khi bị giết
    '''
    def __init__(self,pos_x,pos_y):
        self.X=pos_x
        self.Y=pos_y
        self.heath=10
        self.WIDTH=50
        self.HEIGHT=50
        self.speed=4
        self.action=2
        self.damage=5
        self.sound_attack=pygame.mixer.Sound('asset/sound/swoosh.ogg')
        self.image=pygame.transform.scale(pygame.image.load('asset/enemy/Fire/F1.gif'),(self.WIDTH,self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.topleft= [self.X,self.Y]
    
    def acttack(self,player):
        if self.rect.colliderect(player):
            self.sound_attack.play()
            player.being_attacked(self.damage)
    def move(self,map):
        if self.action==1:
            self.X=self.X
            self.Y=self.Y+self.speed*-1
            self.rect.topleft=[self.X+0,self.Y+self.speed*-1]
        elif self.action==2:
            self.X=self.X
            self.Y=self.Y+self.speed*1
            self.rect.topleft=[self.X+0,self.Y+self.speed*1]
        elif self.action==3:
            self.X=self.X+self.speed*-1
            self.Y=self.Y
            self.rect.topleft=[self.X+self.speed*-1,self.Y]
        elif self.action==4:
            self.X=self.X+self.speed*1
            self.Y=self.Y
            self.rect.topleft=[self.X+self.speed*1,self.Y]
        for brick in map.Barri1:
            if brick.rect.colliderect(self):
                if(self.action==3):
                    self.action=4
                elif self.action==4:
                    self.action=3
                elif self.action==1:
                    self.action=2
                elif self.action==2:
                    self.action=1
        for brick in map.Barri2:
            if brick.rect.colliderect(self):
                if(self.action==3):
                    self.action=4
                elif self.action==4:
                    self.action=3
                elif self.action==1:
                    self.action=2
                elif self.action==2:
                    self.action=1
    def draw(self,screen,map):
        screen.blit(self.image,(self.X,self.Y))
        self.move(map)
        

class fire_LR(fire):
    '''Quái vật trong game
    chỉ có thể di chuyển trái phải
    Làm mất máu
    có thể sinh ra tiền sau khi bị giết
    '''
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.action=1
        n=random.randint(0,2)
        if n==1:
            self.image=pygame.transform.scale(pygame.image.load('asset/enemy/Ghost/ghost.gif'),(self.WIDTH,self.HEIGHT))
            self.damage=8


class fire_TB(fire):
    '''Quái vật trong game
    chỉ có thể di chuyển lên xuống
    Làm mất máu
    có thể sinh ra tiền sau khi bị giết
    '''
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.action=3
        n=random.randint(0,2)
        if n==1:
            self.image=pygame.transform.scale(pygame.image.load('asset/enemy/Ghost/ghost.gif'),(self.WIDTH,self.HEIGHT))
            self.damage=8
