from client import *
import pygame
import sys
from boomman import *
from mapgame import *
from pygame import mixer
from enemy import*
from baner import*
from AutoPlay import*
import random
from serve import *
print(sequence_num)


pygame.init()
screen=pygame.display.set_mode((1300,700))
pygame.display.set_caption("Game Đặt Boomm")
FPS=160
clock=pygame.time.Clock()
music= random.randint(0, 2)
mixer.music.load('asset/sound/'+str(music)+'bg.mp3')
mixer.music.play(-1)
mixer.music.set_volume(50)
map1=Mapgame()
map1.filemap=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,0,0,2,0,0,3,0,4,0,0,0,0,0,1],
    [1,0,0,4,2,0,0,0,2,0,3,0,0,0,0,0,0,2,0,2,1],
    [1,0,0,2,2,0,2,0,2,0,0,3,0,0,0,2,2,4,0,2,1],
    [1,0,0,0,0,0,0,2,0,2,2,2,0,0,0,0,0,0,0,2,1],
    [1,0,2,2,0,0,0,0,0,2,0,2,0,0,0,3,2,2,0,0,1],
    [1,0,2,0,0,0,3,0,0,2,2,2,2,0,0,4,0,0,0,0,1],
    [1,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,1],
    [1,0,0,0,0,0,2,0,0,0,2,0,2,0,0,0,0,0,0,0,1],
    [1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,2,0,0,4,0,1],
    [1,0,2,0,0,4,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
player=Player(50,600)
ortherplayer=PlayerLan(950,600,0)
panel_info=BanerInfo(player,map1)
panel_infoBOT1=BanerInfoBot(ortherplayer,map1)
panel_infoBOT1.y+=200
def handleLan():
    if(server.Datagame.move_i==1 and  ortherplayer.X>=60):
        ortherplayer.walk_Left_Right(-0.25)
        ortherplayer.action=3
    elif(server.Datagame.move_i==2 and ortherplayer.X<=950):
        ortherplayer.walk_Left_Right(0.25)
        ortherplayer.action=4
    elif(server.Datagame.move_i==3 and ortherplayer.Y>=55):
        ortherplayer.walk_TopBottom(-0.25)
        ortherplayer.action=1
    elif(server.Datagame.move_i==4 and ortherplayer.Y<=605):
        ortherplayer.walk_TopBottom(0.25)
        ortherplayer.action=2
    if(server.Datagame.put_boom==1):
        ortherplayer.put_boom()
    if(client.Datagame.move_i==1 and  ortherplayer.X>=60):
        ortherplayer.walk_Left_Right(-0.25)
        ortherplayer.action=3
    elif(client.Datagame.move_i==2 and ortherplayer.X<=950):
        ortherplayer.walk_Left_Right(0.25)
        ortherplayer.action=4
    elif(client.Datagame.move_i==3 and ortherplayer.Y>=55):
        ortherplayer.walk_TopBottom(-0.25)
        ortherplayer.action=1
    elif(client.Datagame.move_i==4 and ortherplayer.Y<=605):
        ortherplayer.walk_TopBottom(0.25)
        ortherplayer.action=2
    if(client.Datagame.put_boom==1):
        ortherplayer.put_boom()

isclient=False    
server=Server()
server.AddSubscribersForLockBrokenEvent(handleLan)
client=Client()
client.AddSubscribersForLockBrokenEvent(handleLan)
# server.startServer()
map1.render_enemy()

def draw_window():
    screen.fill((125,155,255))
    map1.draw(screen)
    player.draw(screen)
    ortherplayer.draw(screen)
    map1.draw_enemy(screen,map1)
    panel_info.draw(screen)
    panel_info.update(player)
    panel_infoBOT1.draw(screen)
    panel_infoBOT1.update(ortherplayer)
    pygame.display.flip()
    pygame.display.update()
while True:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYUP:
            if player.action!=5:
                player.action=0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                player=Player(950,600)
                ortherplayer=PlayerLan(50,600,0)
                server.startServer()
            if event.key ==pygame.K_2:
                client.ConnectToServer()
                isclient=True
            if event.key==pygame.K_SPACE:
                if len(player.boom)<=player.boom_num:
                    if isclient:
                        client.sendData(Data=SocketData(5,1))
                    else:
                        server.sendData(Data=SocketData(5,1))
            player.put_boom(event)
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        if isclient:
            client.sendData(Data=SocketData(1,0))
        else:
            server.sendData(Data=SocketData(1,0))
    elif keys[pygame.K_RIGHT]:
        if isclient:
            client.sendData(Data=SocketData(2,0))
        else:
            server.sendData(Data=SocketData(2,0))
    elif keys[pygame.K_UP]:
        if isclient:
            client.sendData(Data=SocketData(3,0))
        else:
            server.sendData(Data=SocketData(3,0))
    elif keys[pygame.K_DOWN]:
        if isclient:
            client.sendData(Data=SocketData(4,0))
        else:
            server.sendData(Data=SocketData(4,0))
    player.move(map1,ortherplayer)
    ortherplayer.move(map1,player)
    player.update(0.01)
    ortherplayer.update(0.01)
    if player.checkdie():
        player.speed=0
    draw_window()