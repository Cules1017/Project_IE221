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
player1=PlayerTwo(950,600)
player2=autoplay(800,100)
panel_info=BanerInfo(player,map1)
panel_infoBOT=BanerInfoBot(player1,map1)
panel_infoBOT1=BanerInfoBot(player2,map1)
panel_infoBOT1.y+=200
def aa():
    print(555)
    player1.X=Server1.Datagame.X
    player1.Y=Server1.Datagame.Y
    print(Server1.Datagame.X)
    print(Server1.Datagame.Y)

    player1.rect.topleft=[Server1.Datagame.X,Server1.Datagame.Y]
Server1=Server()
Server1.AddSubscribersForLockBrokenEvent(aa)
Server1.startServer()
map1.render_enemy()

def draw_window():
    screen.fill((125,155,255))
    map1.draw(screen)
    player.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    map1.draw_enemy(screen,map1)
    panel_info.draw(screen)
    panel_info.update(player)
    panel_infoBOT.draw(screen)
    panel_infoBOT.update(player1)
    panel_infoBOT1.draw(screen)
    panel_infoBOT1.update(player2)
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
            if player1.action!=5:
                player1.action=0
        if event.type==pygame.KEYDOWN:

            player.put_boom(event)
            player1.put_boom(event)
    player.move(map1,player1,player2)
    player1.move(map1,player,player2)
    player2.automove(map1,player,player1)
    player2.update(0.01)
    player.update(0.01)
    player1.update(0.01)
    if player.checkdie():
        player.speed=0
        #print("END GAME")
    if player1.checkdie():
        player1.speed=0
        #print("END GAME")
    if player2.checkdie():
        player2.speed=0
        #print("END GAME")
    draw_window()