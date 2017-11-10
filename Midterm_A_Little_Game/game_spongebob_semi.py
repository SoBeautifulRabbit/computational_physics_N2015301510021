# -*- coding: utf-8 -*-
"""
代码正在完善中
"""

import pygame
import random
import sys
import time
import math
from pygame.locals import *

WINDOWWIDTH=1024
WINDOWHEIGHT=600
DT=0.1

INITIAL_MONEY=200
CHARACTER_SIZE=70
HAMBURGER_SIZE=20
CUSTOMER_SPEED=3
HAMBURGER_SPEED=20
GRAVITY=10

def terminate():
    pygame.quit()
    sys.exit()
    
def wait_for_player_to_press_key():
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    terminate()
                if event.key==K_RETURN:
                    return


#两种结束游戏的方式
def stolen_recipe():
    terminate()

def no_money():
    terminate()



#四个碰撞函数
def hamburger_hit_customer(hamburgers,customers):
    for h in hamburgers:
        if h['rect'].colliderect(c['rect']):
            hamburgers.remove(h)
            return True
    return False

def hamburger_hit_pilaoban(hamburgers,pilaobans):
    for h in hamburgers:
        if h['rect'].colliderect(p['rect']):
            hamburgers.remove(h)
            return True
    return False

def bomb_hit_customer(bombs,customers):
    for b in bombs:
        if b['rect'].colliderect(c['rect']):
            bombs.remove(b)
            return True
        return False

def bomb_hit_pilaoban(bombs,pilaobans):
    for b in bombs:
        if b['rect'].colliderect(p['rect']):
            bombs.remove(b)
            return True
        return False

    
pygame.init()
window_surface=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('SpongeBob')
pygame.mouse.set_visible(True)


#加载图片并勾勒方框
BACKGROUND_IMAGE=pygame.image.load('background.png')
RESCALED_BACKGROUND=pygame.transform.scale(BACKGROUND_IMAGE,(WINDOWWIDTH,WINDOWHEIGHT))
START_SCREEN=pygame.image.load('background.png')
RESCALED_START_SCREEN=pygame.transform.scale(START_SCREEN,(WINDOWWIDTH,WINDOWHEIGHT))
CUSTOMER_IMAGE=pygame.image.load('1.gif')
PILAOBAN_IMAGE=pygame.image.load('2.png')
HAMBURGER_IMAGE=pygame.image.load('3.gif')
BOMB_IMAGE=pygame.image.load('4.gif')

customerRect=CUSTOMER_IMAGE.get_rect()
pilaobanRect=PILAOBAN_IMAGE.get_rect()
hamburgerRect=HAMBURGER_IMAGE.get_rect()
bombRect=BOMB_IMAGE.get_rect()


#开始屏幕
window_surface.blit(RESCALED_START_SCREEN,(0,0))
pygame.display.update()
wait_for_player_to_press_key()


while True:
    customers=[]
    pilaobans=[]
    hamburgers=[]
    bombs=[]
    money=INITIAL_MONEY
    shoot_counter=49
    customer_counter=99
    pilaoban_counter=0
    type=True
    
    
    while True:#game loop
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
                
            if event.type==KEYUP:
                if event.key==K_ESCAPE:
                    terminate()
                if event.key==K_SPACE:
                    shoot=True
                if event.key==ord('h'):
                    Type=True
                if event.key==ord('b'):
                    Type=False

        
        #增加一个顾客或者痞老板
        if shoot_counter<=50:
            shoot=False
        
        if customer_counter>=100:
            new_customer={'rect':pygame.Rect(WINDOWWIDTH,WINDOWHEIGHT-90,CHARACTER_SIZE,CHARACTER_SIZE),'surface':pygame.transform.scale(CUSTOMER_IMAGE,(CHARACTER_SIZE,CHARACTER_SIZE))}
            customers.append(new_customer)
            customer=0
            
        if pilaoban_counter>=1000:
            new_pilaoban={'rect':pygame.Rect(WINDOWWIDTH,WINDOWHEIGHT-90,CHARACTER_SIZE,CHARACTER_SIZE),'surface':pygame.transform.scale(PILAOBAN_IMAGE,(CHARACTER_SIZE,CHARACTER_SIZE))}
            pilaobans.append(new_pilaoban)
            pilaoban_counter=0
            
        #增加一个蟹黄包或者炸弹
        if shoot==True and type==True:   #此时是汉堡
            new_hamburger={'rect':pygame.Rect(50,WINDOWHEIGHT-50,HAMBURGER_SIZE,HAMBURGER_SIZE),'surface':pygame.transform.scale(HAMBURGER_IMAGE,(HAMBURGER_SIZE,HAMBURGER_SIZE))}
            hamburgers.append(new_hamburger)
            shoot==False
            pos=pygame.mouse.get_pos()
            mouse_x=pos[0]
            mouse_y=pos[1]
            delta_x=mouse_x-50
            delta_y=WINDOWHEIGHT-50-mouse_y
            delta_l=math.sqrt(delta_x**2+delta_y**2)
            v_x=HAMBURGER_SPEED*delta_x/delta_l
            v_y=HAMBURGER_SPEED*delta_y/delta_l
            customer_counter=0
            shoot_counter=0
            
        if shoot==True and type==False:
            new_bomb={'rect':pygame.Rect(50,WINDOWHEIGHT-50,HAMBURGER_SIZE,HAMBURGER_SIZE),'surface':pygame.transform.scale(BOMB_IMAGE,(HAMBURGER_SIZE,HAMBURGER_SIZE))}
            bombs.append(new_bomb)
            shoot==False
        
        #move the customers
        for c in customers:
            c['rect'].move_ip(-1*CUSTOMER_SPEED,0)
        for p in pilaobans:
            p['rect'].move_ip(-2*CUSTOMER_SPEED,0)
            
        #move the hamburger
        for h in hamburgers:
            h['rect'].move_ip(v_x,v_y)  #这种算法下，只允许屏幕上存在一个汉堡或炸弹
            v_y=v_y-GRAVITY*DT

        for b in bombs:
            b['rect'].move_ip(v_x,v_y)
            v_y=v_y-GRAVITY*DT
            
        shoot_counter=shoot_counter+1
        customer_counter=customer_counter+1
        pilaoban_counter=pilaoban_counter+1
        
        #删除超出边界的元素
        for h in hamburgers:
            if h['rect'].bottom>WINDOWHEIGHT:
                hamburgers.remove(h)
        
        for b in bombs:
            if b['rect'].bottom>WINDOWHEIGHT:
                bombs.remove(b)
        
        for c in customers:
            if c['rect'].left<100:
                customers.remove(c)
                
        for p in pilaobans:
            if p['rect'].left<100:
                stolen_recipe()
        
        #检查是否产生碰撞
        for c in customers:
            if hamburger_hit_customer(hamburgers,customers):
                money=money+10
                customers.remove(c)
        for c in customers:
            if bomb_hit_customer(bombs,customers):
                customers.remove(c)
        for p in pilaobans:
            if hamburger_hit_pilaoban(hamburgers.pilaobans):
                stolen_recipe()
        for p in pilaobans:
            if bomb_hit_pilaoban(bombs,pilaobans):
                pilaobans.remove(p)
                
        #绘制图形
        window_surface.blit(RESCALED_BACKGROUND,(0,0))
        
        for h in hamburgers:
            window_surface.blit(h['surface'],h['rect'])
        for b in bombs:
            window_surface.blit(b['surface'],b['rect'])
        for c in customers:
            window_surface.blit(c['surface'],c['rect'])
        for p in pilaobans:
            window_surface.blit(p['surface'],p['rect'])
        
        pygame.display.update()
        time.sleep(0.2)





            
            
            
        
        
        