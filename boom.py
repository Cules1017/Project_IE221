import pygame

class Boom(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.X=pos_x
        self.Y=pos_y
        self.power_explo=1
        self.WIDTH=40
        self.HEIGHT=40
        self.time=None

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

    def update(self,second):
        if self.time is not None:
            if pygame.time.get_ticks() - self.time >= 1500:
                self.kill()
        self.current_animation+=second
        if int(self.current_animation) >= len(self.boom_animation):
                self.current_animation=0
        self.image = pygame.transform.smoothscale(self.boom_animation[int(self.current_animation)], (self.WIDTH,self.HEIGHT))
    