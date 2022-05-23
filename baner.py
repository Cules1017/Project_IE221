from boomman import Player
from mapgame import *
import pygame


class BanerInfo():
    '''Bảng hiển thị thông tin người chơi'''
    def __init__(self, player,map) -> None:
        '''
        self.font: Qui định font chữ trên panel
        self.player: Người chơi mà panel hiển thị
        self.map: Thông tin map của màn chơi hiện tại
        self.name: Thuộc tính tên nhân vật
        self.heath: Lượng máu nhân vật
        self.heath_icon: icon thể hiện biếu tượng máu
        self.speed: tốc độ nhân vật
        self.speed_icon: icon thể hiện tốc độ nhân vật
        self.boom: số boom còn lại của nhân vật
        self.boom_icon: thiện thị biểu tượng thể hiện boom
        self.point: số điểm cũa player
        self.point_icon: biểu tượng thể hiện túi tiền
        self.x: vị trí X hiển thị panel
        self.y: vị trí Y hiển thị panel
        self.WIDTH: Kích thước Panel
        self.HEIGTH: Kích thước Panel
        self.avata: hình ảnh tượng trưng cho nhân vật
        self.bg: Hình ảnh nền của khung hiển thi
        self.display_player
        '''
        self.font = pygame.font.Font('freesansbold.ttf', 15)
        self.player=player
        self.map=map
        self.name=self.font.render(str(player.name), True,(33,31,88))
        self.heath=self.font.render(str(player.heath), True,(33,31,88))
        self.heath_icon=pygame.transform.scale(pygame.image.load('asset/banner/heath.gif'),(18,18))
        self.speed=self.font.render(str(player.speed), True,(33,31,88))
        self.speed_icon=pygame.transform.scale(pygame.image.load('asset/banner/speed.gif'),(18,22))
        self.boom=self.font.render(str(player.boom_real), True,(33,31,88))
        self.boom_icon=pygame.transform.scale(pygame.image.load('asset/item/2.gif'),(18,18))
        self.point=self.font.render(str(player.point), True,(33,31,88))
        self.point_icon=pygame.transform.scale(pygame.image.load('asset/banner/point.gif'),(18,22))
        self.x=1050
        self.y=0
        self.WIDTH=240
        self.HEIGTH=140
        self.avata=pygame.transform.smoothscale(self.player.run_animation[5],(70,70))
        self.bg=pygame.transform.scale(pygame.image.load('asset/banner/bg.gif'),(250,700))
        self.display_player=pygame.transform.scale(pygame.image.load('asset/banner/Cardgreen.gif'),(self.WIDTH,self.HEIGTH))
    def update(self,player):
        '''
        Cập nhật và render các thông số nhân vật
        '''
        self.heath=self.font.render(str(player.heath), True,(33,31,88))
        self.speed=self.font.render(str(player.speed), True,(33,31,88))
        self.boom=self.font.render(str(player.boom_real), True,(33,31,88))
        self.point=self.font.render(str(player.point), True,(33,31,88))
    def draw(self, screen):
        '''
        Vẽ các thông tin lên màn hình
        '''
        if self.bg!=None:
            screen.blit(self.bg,(self.x,self.y))
        screen.blit(self.display_player,(self.x+5,self.y+105))
        screen.blit(self.avata,(self.x+35,self.y+125))
        screen.blit(self.name,(self.x+45,self.y+212))

        screen.blit(self.heath,(self.x+180,self.y+132))
        screen.blit(self.heath_icon,(self.x+130,self.y+129))
        screen.blit(self.speed,(self.x+180,self.y+156))
        screen.blit(self.speed_icon,(self.x+130,self.y+152))
        screen.blit(self.boom,(self.x+180,self.y+182))
        screen.blit(self.boom_icon,(self.x+130,self.y+180))
        screen.blit(self.point,(self.x+180,self.y+210))
        screen.blit(self.point_icon,(self.x+130,self.y+206))
        # screen.blit(self.name,(self.x+45,self.y+212))
        # screen.blit(self.name,(self.x+45,self.y+212))
        # screen.blit(self.name,(self.x+45,self.y+212))
class BanerInfoBot(BanerInfo):
    '''
    Một loại panel hiển thị thông tin của Bot
    Được kế thừa từ BanerInfor
    '''
    def __init__(self, player, map) -> None:
        super().__init__(player, map)
        self.y=130
        self.bg=None
