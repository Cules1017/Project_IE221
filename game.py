import pygame
import sys
from boomman import *
from mapgame import *
from pygame import mixer
from enemy import*
import random
 

pygame.init()
screen=pygame.display.set_mode((1280,700))
pygame.display.set_caption("Game Đặt Boomm")
FPS=144
clock=pygame.time.Clock()
panel_player=pygame.image.load('asset/panel_player.png')
music= random.randint(0, 2)
mixer.music.load('asset/sound/'+str(music)+'bg.mp3')
mixer.music.play(-1)
mixer.music.set_volume(50)
map1=Mapgame()
map1.filemap=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,2,2,0,0,0,2,0,0,0,0,0,0,0,0,2,0,2,1],
    [1,0,2,2,2,0,2,2,2,0,0,3,0,0,0,2,2,4,0,2,1],
    [1,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,2,1],
    [1,0,2,2,2,0,0,0,0,2,0,0,2,2,0,0,2,2,0,0,1],
    [1,0,2,0,0,0,0,0,0,2,0,0,2,0,0,0,0,0,0,0,1],
    [1,0,0,0,2,0,0,0,2,0,2,0,0,0,0,0,0,2,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

player=Player(400,600)

map1.render_enemy()

def draw_window():
    screen.fill((125,155,255))
    map1.draw(screen)
    player.draw(screen)
    map1.draw_enemy(screen,map1)
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
            player.put_boom(event)
    player.move(map1)
    player.update(0.01)
    if player.checkdie():
        player.speed=0
        print("END GAME")
    draw_window()