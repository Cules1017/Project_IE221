import pygame

#TYPE 1: nền có thể di chuyển qua
#TYPE 2: Vật thể cứng không thể di chuyển qua, có thể phá hủy theo heath
#TYPE 3: Vật thể cứng kh thể di chuyển không thể phá hủy

class Barrier():
    def __init__(self, pos_x, pos_y):
        self.X=pos_x
        self.Y=pos_y
        self.type=None
        self.heath=None
        self.image=None
    def draw(self,screen,col,row):
        screen.blit(self.image,(col*50,row*50))

class Brick(Barrier):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.type=2
        self.heath=100
        self.image=pygame.transform.scale(pygame.image.load('asset/topographic/16.gif'),(50,50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]
class Stone(Barrier):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.type=3
        self.image=pygame.transform.scale(pygame.image.load('asset/topographic/brick.jpg'),(50,50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]

class Stone1(Barrier):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.type=3
        self.image=pygame.transform.scale(pygame.image.load('asset/topographic/2.gif'),(50,50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]
class Sandgrey_bg(Barrier):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.type=1
        self.image=pygame.transform.scale(pygame.image.load('asset/topographic/Sand.gif'),(50,50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]