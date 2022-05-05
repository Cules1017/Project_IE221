from boomman import *
class autoplay(Player):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.redirect=random.randint(1,4)
        self.decideBoom=random.randint(0,2)
        self.name="RED"
        self.boom=[]
        self.last_put=0
        self.last_turn=0
        self.now1=pygame.time.get_ticks()

        self.run_animation=[]

        self.run_animation.append(pygame.image.load('asset/Player 3/01.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/02.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/03.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/04.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/05.gif').convert_alpha())

        self.run_animation.append(pygame.image.load('asset/Player 3/11.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/12.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/13.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/14.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/15.gif').convert_alpha())

        self.run_animation.append(pygame.image.load('asset/Player 3/21.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/22.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/23.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/24.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/25.gif').convert_alpha())

        self.run_animation.append(pygame.image.load('asset/Player 3/31.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/32.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/33.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/34.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/35.gif').convert_alpha())

        self.run_animation.append(pygame.image.load('asset/Player 3/41.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/42.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/43.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/44.gif').convert_alpha())
        self.run_animation.append(pygame.image.load('asset/Player 3/45.gif').convert_alpha())
    def put_boomAuto(self):
            if len(self.boom)<=self.boom_num:
                self.boom_real-=1
                boom=Boom(self.X-10,self.Y-5)
                boom.sound.play()
                boom.time = pygame.time.get_ticks()
                self.boom.append(boom)
                b1=pygame.sprite.Group()
                b1.add(boom)
                self.boom_sprite.append(b1)
                self.last_put=self.now
    def automove(self,map,*players):
        orig_x=self.X
        orig_y=self.Y
        if self.redirect==1:# and self.X>=60:
            self.walk_Left_Right(-0.25)
            self.action=3
        elif self.redirect==2:# and self.X<=950:
            self.walk_Left_Right(0.25)
            self.action=4
        elif self.redirect==3:# and self.Y>=55:
            self.walk_TopBottom(-0.25)
            self.action=1
        elif self.redirect==4:# and self.Y<=605:
            self.walk_TopBottom(0.25)
            self.action=2
        if self.now1-self.last_turn > 7000:
            self.redirect=random.randint(1,4)

        # if self.X<=59.5:
        #     self.redirect=random.randint(1,4)
        # elif self.X>=949.5:
        #     self.redirect=random.randint(1,4)
        # elif self.Y==55:
        #     self.redirect=random.randint(1,4)
        # elif self.Y==605:
        #     self.redirect=random.randint(1,4)
        # if self.rect.collidelist(map.Barri1)!=1:
        #     print('cham')
        #     self.X=orig_x
        #     self.Y=orig_y
        #     self.rect.topleft=[orig_x,orig_y]
        self.rect.colliderect(self)
        enemymap=map.fireLR+map.fireBT
        self.now = pygame.time.get_ticks()

        for brick in map.Barri1:
            if brick.rect.colliderect(self):
                self.X=orig_x
                self.Y=orig_y
                self.rect.topleft=[orig_x,orig_y]
                self.decideBoom=random.randint(0,5)
                if self.decideBoom==1 and self.now-self.last_put >= 5000:
                    self.put_boomAuto()
                self.redirect=random.randint(1,4)
        # for b in self.boom:
        #     b.destroy(map,self)
        #     if b.exploy_boom!=None:
        #         if b.exploy_boom.rect.colliderect(self):
        #             self.being_attacked(20)
        for enemy in enemymap:
            if enemy.rect.colliderect(self):
                if self.now-self.last_put >= 5000:
                    self.put_boomAuto()
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
        for playeri in players:
            if playeri.rect.colliderect(self):
                self.X=orig_x
                self.Y=orig_y
                self.rect.topleft=[orig_x,orig_y]
                if  self.now-self.last_put >= 5000:
                    self.put_boomAuto()
                self.redirect=random.randint(1,4)
            # for b in playeri.boom:
            #     b.destroy(map,self)
            #     if b.exploy_boom!=None:
            #         print(self.name)
            #         if b.exploy_boom.rect.colliderect(self):
            #             self.being_attacked(20)
        for brick in map.Barri2:
            if brick.rect.colliderect(self):
                self.X=orig_x
                self.Y=orig_y
                self.rect.topleft=[orig_x,orig_y]
                self.redirect=random.randint(1,4)
        self.checkboom(players,map,orig_x,orig_y)


