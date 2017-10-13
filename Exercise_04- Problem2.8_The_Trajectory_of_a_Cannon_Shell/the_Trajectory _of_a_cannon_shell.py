# -*- coding: utf-8 -*-
'''solution to problem 1.6: A Simple Population Model'''
'''Created by 李东旭'''

import matplotlib.pyplot as plt

'''以下两行代码用来解决中文字体在绘图时显示的问题'''
import matplotlib.font_manager as fm
zh=fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
'''如果你用的不是Windows平台，请对上一行代码做相应的调整！！'''

import math
#import pygame

class cannon:
    '''这种加农炮既考虑了空气阻力又考虑了重力变化,
       如果你不想要空气阻力，就设置B_m=0
       如果你不想要重力变化，就用另外一种加农炮（下面的cannong）'''
    def __init__(self,ang=45,B_m=4e-5,speed=700):
        self.ang=ang/(180)*math.pi
        self.speed=speed
        self.B_m=B_m
        
    '''发射模块'''    
    def shoot(self):
        dt=0.001
        g_0=9.820
        T=[0,]
        x=[0,]
        y=[0,]
        costheta=[math.cos(self.ang),]
        sintheta=[math.sin(self.ang),]
        v_x=[(self.speed)*(costheta[0]),]
        v_y=[self.speed*sintheta[0],]
        v=[self.speed,]
        g=[g_0,]
        
        '''重力变化计算'''
        def gravity(h):
            G=6.674e-11
            M=5.9721986e24
            R=6371008
            _g=(G*M)/((R+h)**2)
            _g=round(_g,3)         #保留3位小数
            return _g
        
        '''欧拉法解微分方程组'''
        t=0
        i=0
        while y[i]>=0:
            t=t+dt
            v_x_=v_x[i]-self.B_m*v[i]**2*costheta[i]*dt
            v_y_=v_y[i]+((-self.B_m)*v[i]**2*sintheta[i]-g[i])*dt
            v_=math.sqrt(v_x_**2+v_y_**2)
            costheta_=v_x_/v_
            sintheta_=v_y_/v_
            x_=x[i]+v_x[i]*dt
            y_=y[i]+v_y[i]*dt
            T.append(t)
            v_x.append(v_x_)
            v_y.append(v_y_)
            v.append(v_)
            costheta.append(costheta_)
            sintheta.append(sintheta_)
            x.append(x_)
            y.append(y_)
            g.append(gravity(y[i]))
            i=i+1
            
        '''修正落点'''
        def line(_y):      #一条直线
            k=(y[i]-y[i-1])/(x[i]-x[i-1])
            b=y[i]-k*x[i]
            return (_y-b)/k
        
        x[i]=line(0)
        y[i]=0
        return x,y

class cannong(cannon):     #继承父类
    def shoot(self):
        dt=0.001
        g_0=9.820
        T=[0,]
        x=[0,]
        y=[0,]
        costheta=[math.cos(self.ang),]
        sintheta=[math.sin(self.ang),]
        v_x=[(self.speed)*(costheta[0]),]
        v_y=[self.speed*sintheta[0],]
        v=[self.speed,]
        
        '''欧拉法解微分方程组'''
        t=0
        i=0
        while y[i]>=0:
            t=t+dt
            v_x_=v_x[i]-self.B_m*v[i]**2*costheta[i]*dt
            v_y_=v_y[i]+((-self.B_m)*v[i]**2*sintheta[i]-g_0)*dt
            v_=math.sqrt(v_x_**2+v_y_**2)
            costheta_=v_x_/v_
            sintheta_=v_y_/v_
            x_=x[i]+v_x[i]*dt
            y_=y[i]+v_y[i]*dt
            T.append(t)
            v_x.append(v_x_)
            v_y.append(v_y_)
            v.append(v_)
            costheta.append(costheta_)
            sintheta.append(sintheta_)
            x.append(x_)
            y.append(y_)
            i=i+1
            
        '''修正落点'''
        def line(_y):     #一条直线
            k=(y[i]-y[i-1])/(x[i]-x[i-1])
            b=y[i]-k*x[i]
            return (_y-b)/k
        
        x[i]=line(0)
        y[i]=0
        return x,y
    
'''以下为每种加农炮配置一个绘图函数'''
def show():    #正常的加农炮
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(x1,y1,label='15°')
    plt.plot(x2,y2,label='30°')
    plt.plot(x3,y3,label='45°')
    plt.plot(x4,y4,label='70°')
    plt.xlim((0,25000))
    plt.ylim((0,25000))
    plt.grid(True)
    plt.title('同时考虑空气阻力和重力变化的炮弹轨迹',fontproperties=zh)
    plt.xlabel("横坐标 距离 x(m)",fontproperties=zh)
    plt.ylabel("纵坐标 高度 y(m)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体


def showg():    #不考虑重力变化的加农炮
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(x1g,y1g,label='15°')
    plt.plot(x2g,y2g,label='30°')
    plt.plot(x3g,y3g,label='45°')
    plt.plot(x4g,y4g,label='70°')
    plt.xlim((0,25000))
    plt.ylim((0,25000))
    plt.grid(True)
    plt.title('只考虑空气阻力不考虑重力变化的炮弹轨迹',fontproperties=zh)
    plt.xlabel("横坐标 距离 x(m)",fontproperties=zh)
    plt.ylabel("纵坐标 高度 y(m)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体

def showa():    #不考虑重力变化的加农炮
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(x1a,y1a,label='15°')
    plt.plot(x2a,y2a,label='30°')
    plt.plot(x3a,y3a,label='45°')
    plt.plot(x4a,y4a,label='70°')
    plt.xlim((0,55000))
    plt.ylim((0,55000))
    plt.grid(True)
    plt.title('不考虑空气阻力但考虑重力变化的炮弹轨迹',fontproperties=zh)
    plt.xlabel("横坐标 距离 x(m)",fontproperties=zh)
    plt.ylabel("纵坐标 高度 y(m)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体

def compareg1():    #对比重力变化1
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(x1,y1,label='15°重力改变')
    plt.plot(x1g,y1g,label='15°重力不变')
    plt.plot(x3,y3,label='45°重力改变')
    plt.plot(x3g,y3g,label='45°重力不变')
    plt.xlim((0,25000))
    plt.ylim((0,25000))
    plt.grid(True)
    plt.title('重力是否改变对炮弹轨迹的影响1',fontproperties=zh)
    plt.xlabel("横坐标 距离 x(m)",fontproperties=zh)
    plt.ylabel("纵坐标 高度 y(m)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体

def compareg2():    #对比重力变化2
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(x2,y2,label='30°重力改变')
    plt.plot(x2g,y2g,label='30°重力不变')
    plt.plot(x4,y4,label='70°重力改变')
    plt.plot(x4g,y4g,label='70°重力不变')
    plt.xlim((0,25000))
    plt.ylim((0,25000))
    plt.grid(True)
    plt.title('重力是否改变对炮弹轨迹的影响2',fontproperties=zh)
    plt.xlabel("横坐标 距离 x(m)",fontproperties=zh)
    plt.ylabel("纵坐标 高度 y(m)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体

def comparea():    #对比风阻影响
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(x1,y1,label='15有风阻°')
    plt.plot(x2,y2,label='30°有风阻')
    plt.plot(x3,y3,label='45°有风阻')
    plt.plot(x4,y4,label='70°有风阻')
    plt.plot(x1a,y1a,label='15无风阻°')
    plt.plot(x2a,y2a,label='30°无风阻')
    plt.plot(x3a,y3a,label='45°无风阻')
    plt.plot(x4a,y4a,label='70°无风阻')
    plt.xlim((0,55000))
    plt.ylim((0,55000))
    plt.grid(True)
    plt.title('风阻对炮弹轨迹的影响',fontproperties=zh)
    plt.xlabel("横坐标 距离 x(m)",fontproperties=zh)
    plt.ylabel("纵坐标 高度 y(m)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体

def extreme():    #为超高速的加农炮画图，显示重力的影响
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(xe,ye,label='45重力变化°')
    plt.plot(xeg,yeg,label='45°重力不变')
    plt.grid(True)
    plt.title('重力是否变化对超高速炮弹轨迹的影响',fontproperties=zh)
    plt.xlabel("横坐标 距离 x(m)",fontproperties=zh)
    plt.ylabel("纵坐标 高度 y(m)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体
    
def extreme_detail():    #放大超高速加农炮落地时的细节
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(xe,ye,label='45重力变化°')
    plt.plot(xeg,yeg,label='45°重力不变')
    plt.grid(True)
    plt.title('落地点细节-重力是否变化对超高速炮弹轨迹的影响',fontproperties=zh)
    plt.xlabel("横坐标 距离 x(m)",fontproperties=zh)
    plt.ylabel("纵坐标 高度 y(m)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体   
    plt.xlim((70000,73000))
    plt.ylim((0,3000))

'''计算一组正常加农炮并画图'''
cannon_1=cannon(15)
x1,y1=cannon_1.shoot()
cannon_2=cannon(30)
x2,y2=cannon_2.shoot()
cannon_3=cannon(45)
x3,y3=cannon_3.shoot()
cannon_4=cannon(70)
x4,y4=cannon_4.shoot()
show()

'''计算一组不考虑重力变化的加农炮并画图'''
cannong_1=cannong(15)
x1g,y1g=cannong_1.shoot()
cannong_2=cannong(30)
x2g,y2g=cannong_2.shoot()
cannong_3=cannong(45)
x3g,y3g=cannong_3.shoot()
cannong_4=cannong(70)
x4g,y4g=cannong_4.shoot()
showg()

'''计算一组不考虑风阻的加农炮并不画图'''
cannon_1a=cannon(15,0)
x1a,y1a=cannon_1a.shoot()
cannon_2a=cannon(30,0)
x2a,y2a=cannon_2a.shoot()
cannon_3a=cannon(45,0)
x3a,y3a=cannon_3a.shoot()
cannon_4a=cannon(70,0)
x4a,y4a=cannon_4a.shoot()
showa()

'''分两次对比重力是否变化对加农炮的影响'''
compareg1()
compareg2()

'''对比风阻对加农炮的影响'''
comparea()

'''计算超高速加农炮，重力改变和重力不变,画图对比'''
cannonextreme1=cannon(45,4e-5,7000)
xe,ye=cannonextreme1.shoot()
cannonextreme2=cannong(45,4e-5,7000)
xeg,yeg=cannonextreme2.shoot()
extreme()
extreme_detail()


'''以下时pygame部分'''
import pygame
import time
import os
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800,300))
white = 255,255,255



while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            #os.sys.exit()
    screen.fill(white)
     
    #画一个圆
    color = 35,35,35
    radius = 20
    width = 10
    i=0
    while x3[i]<=21680:
        position = int(x3[i]/30),int(300-y3[i]/30)    #等比例缩小
        pygame.draw.circle(screen, color, position, radius, width)
        i=i+100
        pygame.display.update()
        time.sleep(0.005)
        
    
