import pygame
from exploy import *

class Boom(pygame.sprite.Sprite):
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
    def destroy(self, barri,player):
        if self.exploy_boom!=None:
            if self.exploy_boom.rect.colliderect(player):
                player.being_attacked(20)
                print(player.heath)
            index=self.exploy_boom.rect.collidelist(barri.Barri2)
            if index!=-1:
                x=int(barri.Barri2[index].X/50)
                y=int(barri.Barri2[index].Y/50)
                barri.filemap[y][x]=0
                barri.Barri2.remove(barri.Barri2[index])
            self.exploy_boom=None
                
    def update(self,second,screen):
        if self.time is not None:
            if pygame.time.get_ticks() - self.time >= 1500:
                self.exploy_boom=boom1_exploy(self.X,self.Y,self.power_explo)
                self.exploy_boom.draw(screen)
                self.kill()
        self.current_animation+=second
        if int(self.current_animation) >= len(self.boom_animation):
                self.current_animation=0
        self.image = pygame.transform.smoothscale(self.boom_animation[int(self.current_animation)], (self.WIDTH,self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]