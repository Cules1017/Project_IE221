import pygame

class boom1_exploy(pygame.sprite.Sprite):
    '''Đây là vụ nổ sau khi boom đã nổ
    gây xác thương đến người chơi
    có thể phá vỡ gạch
    '''
    def __init__(self,pos_x,pos_y,pow):
        super().__init__()
        self.X=pos_x-5
        self.Y=pos_y-5
        self.power_explo=pow
        self.WIDTH=70
        self.HEIGHT=70
        self.time=None
        self.boom_animation=[]

        #animation run_top 0->2 ⬆️
        self.boom_animation.append(pygame.image.load('asset/explosion/1.png').convert_alpha())
        self.boom_animation.append(pygame.image.load('asset/explosion/2.png').convert_alpha())
        self.boom_animation.append(pygame.image.load('asset/explosion/3.png').convert_alpha())

        self.current_animation = 0
        self.image = pygame.transform.smoothscale( self.boom_animation[0], (self.WIDTH*1,self.HEIGHT*1))
        #rectangle collision
        self.rect = self.image.get_rect()
        self.rect.center = [self.X,self.Y]
    def update(self,second):
        self.current_animation+=second
        if int(self.current_animation) > 4:
            self.kill()
        self.image=pygame.transform.smoothscale( self.boom_animation[int(self.current_animation)], (self.WIDTH*1,self.HEIGHT*1))
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]
    def draw(self, screen):
        exploy=pygame.sprite.Group()
        exploy.add(self)
        exploy.update(2)
        exploy.draw(screen)