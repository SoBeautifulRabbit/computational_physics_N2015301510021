# -*- coding: utf-8 -*-
'''solution to problem 2.18: Backspin of a fastball'''
'''Created by 李东旭'''

import matplotlib.pyplot as plt

'''以下两行代码用来解决中文字体在绘图时显示的问题'''
import matplotlib.font_manager as fm
zh=fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
'''如果你用的不是Windows平台，请对上一行代码做相应的调整！！'''

import math

class ball:
    '''这种棒球既考虑了空气阻力又考虑了旋转的效应,
       由于湍流，空气阻力B_m是速度v的函数
       旋转引起的效应可以扔出fastball
       如果你不想要fastball，就设置spin=0 '''
    end=18.4          #投手到击球手的距离(类属性)
    g=9.82            #重力加速度(类属性)
    
    def __init__(self,spin=1000,ang=2):
        self.ang=ang/(180)*math.pi
                          #默认以2度左右仰角出手,才能把球扔向击球者
        self.speed=43     #出手速度，优秀的投手
        self.S_m=4.1e-4   #旋转摩擦因数
        self.height=1.5   #投手的出手高度
        self.spin=spin/60*math.pi*2   #旋转速度，由rpm换算成rad/s单位
        
    '''发射模块'''    
    def pitch(self):
        dt=0.00001         #飞行时间大约为0.1秒量级，据此设计dt
        t=0
        T=[0,]
        x=[0,]
        y=[self.height,]        
        v_x=[(self.speed)*math.cos(self.ang),]
        v_y=[(self.speed)*math.sin(self.ang),]
        v=[self.speed,]
        
        
        '''欧拉法解微分方程组'''
        t=0
        i=0
        while x[i]<=ball.end:
            B_m=0.0039+0.0058/(1+math.exp((v[i]-35)/5))
            v_x_=v_x[i]-B_m*v[i]*v_x[i]*dt
            v_y_=v_y[i]-ball.g*dt-B_m*v[i]*v_y[i]*dt+self.S_m*self.spin*v_x[i]*dt
            v_=math.sqrt(v_x_**2+v_y_**2)
            x_=x[i]+v_x[i]*dt
            y_=y[i]+v_y[i]*dt
            
            T.append(t)
            v_x.append(v_x_)
            v_y.append(v_y_)
            v.append(v_)
            x.append(x_)
            y.append(y_)
            i=i+1
            t=t+dt
        '''不需要修正落点'''
        return x,y,t,T,v

class farball(ball):
    '''扔得很远的球，实际棒球比赛不会这样扔'''
    def pitch(self):
        dt=0.00001         
        t=0
        T=[0,]
        x=[0,]
        y=[self.height,]        
        v_x=[(self.speed)*math.cos(self.ang),]
        v_y=[(self.speed)*math.sin(self.ang),]
        v=[self.speed,]
        
        
        '''欧拉法解微分方程组'''
        t=0
        i=0
        while y[i]>=0:
            B_m=0.0039+0.0058/(1+math.exp((v[i]-35)/5))
            v_x_=v_x[i]-B_m*v[i]*v_x[i]*dt
            v_y_=v_y[i]-ball.g*dt-B_m*v[i]*v_y[i]*dt+self.S_m*self.spin*v_x[i]*dt
            v_=math.sqrt(v_x_**2+v_y_**2)
            x_=x[i]+v_x[i]*dt
            y_=y[i]+v_y[i]*dt
            
            T.append(t)
            v_x.append(v_x_)
            v_y.append(v_y_)
            v.append(v_)
            x.append(x_)
            y.append(y_)
            i=i+1
            t=t+dt
        '''需要修正落点'''
        def line(_y):      #一条直线
            k=(y[i]-y[i-1])/(x[i]-x[i-1])
            b=y[i]-k*x[i]
            return (_y-b)/k
        
        x[i]=line(0)
        y[i]=0
        return x,y,t,T,v
'''绘图函数'''
def show():    
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(x1,y1,label='with spin')
    plt.plot(x2,y2,label='no spin')
    plt.xlim((0,18.4))
    plt.ylim((0,1.8))
    plt.grid(True)
    plt.title('棒球快球的轨迹',fontproperties=zh)
    plt.xlabel("横坐标 距离 x(m)",fontproperties=zh)
    plt.ylabel("纵坐标 高度 y(m)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体

def showspeed():    
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(T1,v1,label='with spin')
    plt.plot(T2,v2,label='no spin')

    plt.grid(True)
    plt.title('棒球快球的速率',fontproperties=zh)
    plt.xlabel("时间 T(s)",fontproperties=zh)
    plt.ylabel("速率 v(m/s)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体
    
def comparetime():
    plt.figure(dpi=140,figsize=(6,4.5))
    labels=['with spin','no spin']
    data=[t1,t2]
    plt.barh(range(0,2),data,tick_label=labels)

    plt.grid(True)
    plt.title('棒球快球的飞行时间',fontproperties=zh)
    plt.xlabel("时间 T(s)",fontproperties=zh)
    
def showfar():    
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(x3,y3,label='with spin')
    plt.plot(x4,y4,label='no spin')
    plt.grid(True)
    plt.title('棒球向远处抛的轨迹',fontproperties=zh)
    plt.xlabel("横坐标 距离 x(m)",fontproperties=zh)
    plt.ylabel("纵坐标 高度 y(m)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体
    
def comparetimefar():
    plt.figure(dpi=140,figsize=(6,4.5))
    labels=['with spin','no spin']
    data=[t3,t4]
    plt.barh(range(0,2),data,tick_label=labels)

    plt.grid(True)
    plt.title('棒球快球向远处扔的飞行时间',fontproperties=zh)
    plt.xlabel("时间 T(s)",fontproperties=zh)


fastball=ball(1000,1.48)  
normalball=ball(0,2.02)           #通过多次尝试，求出最终投射到y=1.2m处的投射角
#没有旋转时，初始投射角2.05°
#有旋转时，初始投射角1.48°
farfastball=farball(1000,35)
farnormalball=farball(0,35)
x1,y1,t1,T1,v1=fastball.pitch()
x2,y2,t2,T2,v2=normalball.pitch()
x3,y3,t3,T3,v3=farfastball.pitch()
x4,y4,t4,T4,v4=farnormalball.pitch()
show()
showspeed()
comparetime()
showfar()
comparetimefar()
print('t1=%f'%t1)
print('t2=%f'%t2)
print('t3=%f'%t3)
print('t4=%f'%t4)
'''以下时pygame部分'''
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((500,300))
white = 255,255,255



while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()

    screen.fill(white)
     
    #画一个圆
    color = 35,35,35
    radius = 15
    width = 10
    i=0
    while x1[i]<=18.3:
        position = int(x1[i]*20),int(200-y1[i]*20)    #等比例放大
        pygame.draw.circle(screen, color, position, radius, width)
        i=i+15
        pygame.display.update()
        screen.fill(white)
        
    
