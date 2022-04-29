from player import Player
from boom import Boom
from topographic import *
import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((1280,700))
pygame.display.set_caption("Game Đặt Boomm")
FPS=60
clock=pygame.time.Clock()
panel_player=pygame.image.load('asset/panel_player.png')
map=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,2,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,2,0,0,2,2,0,0,2,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,2,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

player=Player(500,500)
player_idle=pygame.sprite.Group()
player_idle.add(player)
b1=False
listboom=[]
unit_bg=[]
unit_topo=[]
def collisionPlayerTopo(unit_topo):
    for i in unit_topo:
        if i.rect.colliderect(player):
            if(player.action==3):
                player.X=i.X+55
            elif player.action==4:
                player.X=i.X+-50
            elif player.action==1:
                player.Y=i.Y+50
            elif player.action==2:
                player.Y=i.Y-50
def readmap(map,screen):
    for row in range(len(map)):
        for col in range(len(map[row])):
            if(map[row][col]==0):
                unit=Sandgrey_bg(col*50,row*50)
                screen.blit(unit.image,(col*50,row*50))
                unit_bg.append(unit)
            elif(map[row][col]==2):
                unit=Brick_red(col*50,row*50)
                screen.blit(unit.image,(col*50,row*50))
                unit_topo.append(unit)
            elif(map[row][col]==1):
                unit=Stone(col*50,row*50)
                screen.blit(unit.image,(col*50,row*50))
                unit_topo.append(unit)
def window_draw():
    screen.fill((125,155,255))
    readmap(map,screen)
    player_idle.update(0.5)
    player_idle.draw(screen)
    screen.blit(panel_player,(1050,20))
    
    if b1:
        for i in listboom:
            i.update(0.06)
            i.draw(screen)
    pygame.display.flip()
    pygame.display.update()

while True:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                print("BUMM")
                Bomm=Boom(player.X,player.Y)
                Bomm.time = pygame.time.get_ticks()
                b1=pygame.sprite.Group()
                b1.add(Bomm)
                listboom.append(b1)
    keys = pygame.key.get_pressed()  
    # if left arrow key is pressed
    #with action value 1:UP 2:DOWN 3:LEFT 4:RIGHT
    if keys[pygame.K_LEFT] and player.X>=60:
        player.walk_Left_Right(-0.25)
        player.action=3
    elif keys[pygame.K_RIGHT] and player.X<=950:
        player.walk_Left_Right(0.25)
        player.action=4
    elif keys[pygame.K_UP] and player.Y>=55:
        player.walk_TopBottom(-0.25)
        player.action=1
    elif keys[pygame.K_DOWN] and player.Y<=605:
        player.walk_TopBottom(0.25)
        player.action=2
    if event.type==pygame.KEYUP:
        player.action=0
    window_draw()
    collisionPlayerTopo(unit_topo)