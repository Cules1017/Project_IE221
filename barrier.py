import pygame

#TYPE 1: nền có thể di chuyển qua
#TYPE 2: Vật thể cứng không thể di chuyển qua, có thể phá hủy theo heath
#TYPE 3: Vật thể cứng kh thể di chuyển không thể phá hủy

class Barrier():
    '''Vật thể ngăn cản
        self.X=tọa độ của X
        self.Y=tọa độ của Y
        self.type: loại vật thể
        self.heath: sức mạnh vật thể
        self.image: hình ảnh thể hiện
    '''
    def __init__(self, pos_x, pos_y):
        self.X=pos_x
        self.Y=pos_y
        self.type=None
        self.heath=None
        self.image=None
    def draw(self,screen,col,row):
        '''
        Vẽ vật thể lên màn hình 
        các tọa độ x y của vật thể là tọa độ trên ma trận
        nên khi vẽ ra phải nhân lên 50( kích thước từng ô là 50)
        '''
        screen.blit(self.image,(col*50,row*50))

class Brick(Barrier):
    '''Gạch có thể phá vỡ
    self.rect: khối bao bọc vật thể để xử lý va chạm
    self.rect.topleft: vị trí kíc thước
    '''
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.type=2
        self.heath=100
        self.image=pygame.transform.scale(pygame.image.load('asset/topographic/16.gif'),(50,50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]
class Stone(Barrier):
    '''Gạch đá không thể phá vỡ'''
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.type=3
        self.image=pygame.transform.scale(pygame.image.load('asset/topographic/brick.jpg'),(50,50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]

class Stone1(Barrier):
    '''Đá tản không thể phá vỡ'''
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.type=3
        self.image=pygame.transform.scale(pygame.image.load('asset/topographic/2.gif'),(50,50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]
class Sandgrey_bg(Barrier):
    '''Nền cỏ'''
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.type=1
        self.image=pygame.transform.scale(pygame.image.load('asset/topographic/Sand.gif'),(50,50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.X,self.Y]