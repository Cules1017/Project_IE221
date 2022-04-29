import pygame
from boom import Boom


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.X=pos_x
        self.Y=pos_y
        self.heath=100
        self.speed=50
        self.point=0
        self.WIDTH=40
        self.HEIGHT=50

        self.run_animation=[]

        self.action=0
        #animation run_top 0->2 ⬆️
        self.run_animation.append(pygame.image.load('asset/Player 1/01.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/02.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/03.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/04.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/05.gif').convert_alpha())

        self.run_animation.append(pygame.image.load('asset/Player 1/11.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/12.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/13.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/14.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/15.gif').convert_alpha())

        self.run_animation.append(pygame.image.load('asset/Player 1/21.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/22.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/23.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/24.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/25.gif').convert_alpha())

        self.run_animation.append(pygame.image.load('asset/Player 1/31.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/32.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/33.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/34.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/35.gif').convert_alpha())

        self.current_run = 3
        self.image = pygame.transform.smoothscale( self.run_animation[3], (self.WIDTH,self.HEIGHT))
        #rectangle collision
        self.rect = self.image.get_rect()
        self.rect.topleft= [self.X,self.Y]
    def walk_TopBottom(self,n):
            self.rect.topleft=[self.X+0,self.Y+self.speed*n]
            self.Y+=self.speed*n
    def walk_Left_Right(self,n):
            self.rect.topleft=[self.X+self.speed*n,self.Y]
            self.X+=self.speed*n
    def put_boom(self,screen):
        boom=Boom(self.X,self.Y)
        boom1_id=pygame.sprite.Group()
        boom1_id.add(boom)
        boom1_id.update(0.02)
        boom1_id.draw(screen)
    def update(self,second):
        if self.action==0:
            self.current_run=self.current_run
        if self.action==1:
            self.current_run+=second
            if int(self.current_run) > 4:
                self.current_run=0
        elif self.action==2:
            self.current_run+=second
            if int(self.current_run)<5 or int(self.current_run)>9:
                self.current_run=5
        elif self.action==3:
            self.current_run+=second
            if int(self.current_run)<10 or int(self.current_run)>14:
                self.current_run=10
        elif self.action==4:
            self.current_run+=second
            if int(self.current_run)<15 or int(self.current_run)>19:
                self.current_run=15
        # print(self.current_run)
        self.image = pygame.transform.smoothscale(self.run_animation[int(self.current_run)], (self.WIDTH,self.HEIGHT))