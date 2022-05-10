from tkinter import SEL
import pygame
from boom import *


class Player(pygame.sprite.Sprite):
    ''' Nhân vật trong game'''
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.X=pos_x
        self.Y=pos_y
        self.name="Yellow"
        self.heath=100
        self.speed=25
        self.point=0
        self.WIDTH=30
        self.HEIGHT=40
        self.boom_num=10
        self.boom_real=11
        self.boom=[]
        self.boom_sprite=[]

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

        self.run_animation.append(pygame.image.load('asset/Player 1/41.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/42.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/43.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/44.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 1/45.gif').convert_alpha())

        self.current_run = 3
        self.image = pygame.transform.smoothscale( self.run_animation[3], (self.WIDTH,self.HEIGHT))
        #rectangle collision
        self.rect = self.image.get_rect()
        self.rect.topleft= [self.X,self.Y]
    def draw(self,screen):
        player_idle=pygame.sprite.Group()
        player_idle.add(self)
        player_idle.update(0.5)
        player_idle.draw(screen)
        for i in self.boom_sprite:
            i.draw(screen)
            i.update(0.14,screen)


    def walk_TopBottom(self,n):
            self.rect.topleft=[self.X+0,self.Y+self.speed*n]
            self.Y+=self.speed*n
    def walk_Left_Right(self,n):
            self.rect.topleft=[self.X+self.speed*n,self.Y]
            self.X+=self.speed*n

    def checkboom(self,players,map,x,y):
        orig_x=x
        orig_y=y
        for b in self.boom:
            b.destroy(map,self)
        for playeri in players:
            if playeri.rect.colliderect(self):
                self.X=orig_x
                self.Y=orig_y
                self.rect.topleft=[orig_x,orig_y]
            for b in playeri.boom:
                #print(playeri.name)
                b.destroyPL(self)
    #Set up moverment
    def move(self,map,*players):
        orig_x=self.X
        orig_y=self.Y
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and self.X>=60:
            self.walk_Left_Right(-0.25)
            self.action=3
        elif keys[pygame.K_RIGHT] and self.X<=950:
            self.walk_Left_Right(0.25)
            self.action=4
        elif keys[pygame.K_UP] and self.Y>=55:
            self.walk_TopBottom(-0.25)
            self.action=1
        elif keys[pygame.K_DOWN] and self.Y<=605:
            self.walk_TopBottom(0.25)
            self.action=2
        # if self.rect.collidelist(map.Barri1)!=1:
        #     print('cham')
        #     self.X=orig_x
        #     self.Y=orig_y
        #     self.rect.topleft=[orig_x,orig_y]
        self.rect.colliderect(self)
        enemymap=map.fireLR+map.fireBT
        for brick in map.Barri1:
            if brick.rect.colliderect(self):
                self.X=orig_x
                self.Y=orig_y
                self.rect.topleft=[orig_x,orig_y]
        # for b in self.boom:
        #     b.destroy(map,self)
        for enemy in enemymap:
            enemy.acttack(self)
        index_item=self.rect.collidelist(map.item)
        if index_item!=-1:
                x=int(map.item[index_item].X/50)
                y=int(map.item[index_item].Y/50) 
                map.filemap[y][x]=0
                map.item[index_item].acttack(self)
                map.item.remove(map.item[index_item])
        # for it in map.item:
        #     it.acttack(self)
        #     if it.rect.colliderect(self):
        #         x=int(map.it[index].X/50)
        #         y=int(barri.Barri2[index].Y/50)
        #         barri.filemap[y][x]=random.randint(5,7)
        #         map.item.remove(it)
        #         print(len(map.item))
        for brick in map.Barri2:
            if brick.rect.colliderect(self):
                self.X=orig_x
                self.Y=orig_y
                self.rect.topleft=[orig_x,orig_y]
        self.checkboom(players,map,orig_x,orig_y)
        # for playeri in players:
        #     if playeri.rect.colliderect(self):
        #         self.X=orig_x
        #         self.Y=orig_y
        #         self.rect.topleft=[orig_x,orig_y]
        #     for b in playeri.boom:
        #         b.destroy(map,self)
        

            
        # for b in self.boom:
        #     if b.exploy_boom!=None:
        #         # indexb= b.exploy_boom.rect.collidelist(map.Barri1)
        #         # if indexb != -1:
        #         #     del map.Barri1[indexb]
        #         #     self.boom.remove(b)
        #         if b.exploy_boom.rect.

    
    
    def put_boom(self,event):
        if event.key==pygame.K_SPACE:
            if len(self.boom)<=self.boom_num:
                self.boom_real-=1
                boom=Boom(self.X-10,self.Y-5)
                boom.sound.play()
                boom.time = pygame.time.get_ticks()
                self.boom.append(boom)
                b1=pygame.sprite.Group()
                b1.add(boom)
                self.boom_sprite.append(b1)
                
    def being_attacked(self,damage):
        self.heath-=damage
    def animation(self,second):
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
        elif self.action==5:
            self.current_run+=second
            if int(self.current_run)<20:
                self.current_run=20
            if int(self.current_run)>24:
                self.kill()
                self.current_run=24
        # print(self.current_run)
        self.image = pygame.transform.smoothscale(self.run_animation[int(self.current_run)], (self.WIDTH,self.HEIGHT))
    
    def checkdie(self):
        if self.heath<=0:
            self.action=5
            return True
        return False
    def update(self,second):
        self.animation(second)


class PlayerTwo(Player):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.name="BLUE"
        self.run_animation=[]
        self.run_animation.append(pygame.image.load('asset/Player 4/01.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/02.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/03.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/04.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/05.gif').convert_alpha())

        self.run_animation.append(pygame.image.load('asset/Player 4/11.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/12.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/13.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/14.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/15.gif').convert_alpha())

        self.run_animation.append(pygame.image.load('asset/Player 4/21.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/22.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/23.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/24.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/25.gif').convert_alpha())

        self.run_animation.append(pygame.image.load('asset/Player 4/31.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/32.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/33.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/34.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/35.gif').convert_alpha())

        self.run_animation.append(pygame.image.load('asset/Player 4/41.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/42.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/43.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/44.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 4/45.gif').convert_alpha())
    def move(self,map,*players):
        orig_x=self.X
        orig_y=self.Y
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a] and self.X>=60:
            self.walk_Left_Right(-0.25)
            self.action=3
        elif keys[pygame.K_d] and self.X<=950:
            self.walk_Left_Right(0.25)
            self.action=4
        elif keys[pygame.K_w] and self.Y>=55:
            self.walk_TopBottom(-0.25)
            self.action=1
        elif keys[pygame.K_s] and self.Y<=605:
            self.walk_TopBottom(0.25)
            self.action=2
        # if self.rect.collidelist(map.Barri1)!=1:
        #     print('cham')
        #     self.X=orig_x
        #     self.Y=orig_y
        #     self.rect.topleft=[orig_x,orig_y]
        self.rect.colliderect(self)
        enemymap=map.fireLR+map.fireBT
        for brick in map.Barri1:
            if brick.rect.colliderect(self):
                self.X=orig_x
                self.Y=orig_y
                self.rect.topleft=[orig_x,orig_y]
        # for b in self.boom:
        #     if b.exploy_boom==None:
        #         print('hahah')
        #     if b.exploy_boom!=None:
        #         print("Có Boom")
        #         if b.exploy_boom.rect.colliderect(self):
        #             self.being_attacked(20)
        for enemy in enemymap:
            enemy.acttack(self)
        index_item=self.rect.collidelist(map.item)
        if index_item!=-1:
                x=int(map.item[index_item].X/50)
                y=int(map.item[index_item].Y/50) 
                map.filemap[y][x]=0
                map.item[index_item].acttack(self)
                map.item.remove(map.item[index_item])
        # for it in map.item:
        #     it.acttack(self)
        #     if it.rect.colliderect(self):
        #         x=int(map.it[index].X/50)
        #         y=int(barri.Barri2[index].Y/50)
        #         barri.filemap[y][x]=random.randint(5,7)
        #         map.item.remove(it)
        #         print(len(map.item))
        for brick in map.Barri2:
            if brick.rect.colliderect(self):
                self.X=orig_x
                self.Y=orig_y
                self.rect.topleft=[orig_x,orig_y]
        self.checkboom(players,map,orig_x,orig_y)

        # for playeri in players:
        #     if playeri.rect.colliderect(self):
        #         self.X=orig_x
        #         self.Y=orig_y
        #         self.rect.topleft=[orig_x,orig_y]
        #     for b in playeri.boom:
        #         if b.exploy_boom!=None:
        #             if b.exploy_boom.rect.colliderect(self):
        #                 self.being_attacked(20)
    def put_boom(self,event):
        if event.key==pygame.K_LCTRL:
            if len(self.boom)<=self.boom_num:
                self.boom_real-=1
                boom=Boom(self.X-10,self.Y-5)
                boom.sound.play()
                boom.time = pygame.time.get_ticks()
                self.boom.append(boom)
                b1=pygame.sprite.Group()
                b1.add(boom)
                self.boom_sprite.append(b1)
class PlayerLan(Player):
    def __init__(self, pos_x, pos_y,type):
        super().__init__(pos_x, pos_y)
        self.name="BLUE"
        self.run_animation=[]
        if type==0:
            self.run_animation.append(pygame.image.load('asset/Player 4/01.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/02.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/03.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/04.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/05.gif').convert_alpha())

            self.run_animation.append(pygame.image.load('asset/Player 4/11.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/12.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/13.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/14.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/15.gif').convert_alpha())

            self.run_animation.append(pygame.image.load('asset/Player 4/21.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/22.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/23.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/24.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/25.gif').convert_alpha())

            self.run_animation.append(pygame.image.load('asset/Player 4/31.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/32.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/33.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/34.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/35.gif').convert_alpha())

            self.run_animation.append(pygame.image.load('asset/Player 4/41.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/42.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/43.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/44.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 4/45.gif').convert_alpha())
        else:
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

            self.run_animation.append(pygame.image.load('asset/Player 1/41.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 1/42.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 1/43.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 1/44.gif').convert_alpha())
            self.run_animation.append(pygame.image.load('asset/Player 1/45.gif').convert_alpha())
    def move(self,map,*players):
        orig_x=self.X
        orig_y=self.Y
        self.rect.colliderect(self)
        enemymap=map.fireLR+map.fireBT
        for brick in map.Barri1:
            if brick.rect.colliderect(self):
                print("Chạm")
                self.X=orig_x
                self.Y=orig_y
                self.rect.topleft=[orig_x,orig_y]
        for enemy in enemymap:
            enemy.acttack(self)
        index_item=self.rect.collidelist(map.item)
        if index_item!=-1:
                x=int(map.item[index_item].X/50)
                y=int(map.item[index_item].Y/50) 
                map.filemap[y][x]=0
                map.item[index_item].acttack(self)
                map.item.remove(map.item[index_item])
        for brick in map.Barri2:
            if brick.rect.colliderect(self):
                print("Chạm")
                self.X=orig_x
                self.Y=orig_y
                self.rect.topleft=[orig_x,orig_y]
        self.checkboom(players,map,orig_x,orig_y)
    def put_boom(self):
        self.boom_real-=1
        boom=BoomPlayLan(self.X-10,self.Y-5)
        boom.sound.play()
        boom.time = pygame.time.get_ticks()
        self.boom.append(boom)
        b1=pygame.sprite.Group()
        b1.add(boom)
        self.boom_sprite.append(b1)
class PlayerLan1(Player):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)  
    def put_boom(self,event):
        if event.key==pygame.K_SPACE:
            if len(self.boom)<=self.boom_num:
                self.boom_real-=1
                boom=BoomPlayLan(self.X-10,self.Y-5)
                boom.sound.play()
                boom.time = pygame.time.get_ticks()
                self.boom.append(boom)
                b1=pygame.sprite.Group()
                b1.add(boom)
                self.boom_sprite.append(b1)
