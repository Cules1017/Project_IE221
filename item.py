import pygame
from pygame import mixer

class item():
    ''' Các item xuất hiện trong game 
    xuất hiện khi giết quái hoặc phá vỡ tường gạch
    '''
    def __init__(self,pos_x,pos_y) -> None:
        self.X=pos_x
        self.Y=pos_y
        self.addheath=0
        self.addspeed=0
        self.addpoint=0
        self.dupli=1
        self.addboom=0
        self.image=None
        self.rect =None
        self.sound=pygame.mixer.Sound('asset/sound/XU.mp3')
    def draw(self,screen,col,row):
        screen.blit(self.image,(col*50,row*50))
    def acttack(self,player):
            self.sound.play()
            player.heath=player.heath+self.addheath
            player.heath=player.heath
            player.speed+=self.addspeed
            player.boom_num+=self.addboom
            player.boom_real+=self.addboom
            player.point+=self.addpoint
            
class emergency(item):
    '''Cấp cứu giúp hồi 20 máu
    '''
    def __init__(self,pos_x,pos_y) -> None:
        super().__init__(pos_x,pos_y)
        self.addheath=20
        self.image=pygame.transform.scale(pygame.image.load('asset/item/capcuu.gif'),(50,50))
        self.rect = self.image.get_rect()
        self.rect.center= [self.X,self.Y]
class dulicate(item):
    '''Tim giúp hồi 15 máu
    '''
    def __init__(self,pos_x,pos_y) -> None:
        super().__init__(pos_x,pos_y)
        self.addheath=15
        self.image=pygame.transform.scale(pygame.image.load('asset/item/1x.gif'),(50,50))
        self.rect = self.image.get_rect()
        self.rect.center= [self.X,self.Y]
class speed(item):
    '''Tăng tốc cho nhân vật'''
    def __init__(self,pos_x,pos_y) -> None:
        super().__init__(pos_x,pos_y)
        self.addspeed=5
        self.image=pygame.transform.scale(pygame.image.load('asset/item/speed.gif'),(50,50))
        self.rect = self.image.get_rect()
        self.rect.center= [self.X,self.Y]

class addbomm(item):
    '''Thêm Boom cho nhân vật'''
    def __init__(self,pos_x,pos_y) -> None:
        super().__init__(pos_x,pos_y)
        self.addboom=1
        self.image=pygame.transform.scale(pygame.image.load('asset/item/2.gif'),(50,50))
        self.rect = self.image.get_rect()
        self.rect.center= [self.X,self.Y]
class coin_gold(item):
    '''Tăng thêm 2 tiền'''
    def __init__(self,pos_x,pos_y) -> None:
        super().__init__(pos_x,pos_y)
        self.addpoint=2
        self.image=pygame.transform.scale(pygame.image.load('asset/item/coin_gold.gif'),(40,50))
        self.rect = self.image.get_rect()
        self.rect.center= [self.X,self.Y]
class coin_silver(item):
    '''Tăng 1 tiền'''
    def __init__(self,pos_x,pos_y) -> None:
        super().__init__(pos_x,pos_y)
        self.addpoint=1
        self.image=pygame.transform.scale(pygame.image.load('asset/item/coin_silver.gif'),(40,50))
        self.rect = self.image.get_rect()
        self.rect.center= [self.X,self.Y]
class coin_star(item):
    '''Tăng 6 tiền'''
    def __init__(self,pos_x,pos_y) -> None:
        super().__init__(pos_x,pos_y)
        self.addpoint=5
        self.image=pygame.transform.scale(pygame.image.load('asset/item/star.gif'),(40,50))
        self.rect = self.image.get_rect()
        self.rect.center= [self.X,self.Y]