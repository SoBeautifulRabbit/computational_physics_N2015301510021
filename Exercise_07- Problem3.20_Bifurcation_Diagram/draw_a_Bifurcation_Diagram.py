# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:48:32 2017"""

'''solution to problem 3.20: Bifurcation diagram for
 the Driven Nonlinear Pendulum'''
'''Created by 李东旭'''

import matplotlib.pyplot as plt
'''以下两行代码用来解决中文字体在绘图时显示的问题'''
import matplotlib.font_manager as fm
zh=fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
'''如果你用的不是Windows平台，请对上一行代码做相应的调整！！'''
import math

'''警告：完全运行本程序可能需要20分钟或者更长时间，
请根据需要注释掉其中的一部分代码或者手动缩短循环长度'''

Omega=2/3
zhouqi=3*math.pi
dt=0.01
#begin=52.3       
end=500


def points(F_D,begin=52.3):  #如果以52.3s位开始观测时间，每一次都可以观测到峰值
    end_zhouqi_number=(end-begin)/zhouqi
    q=0.5
    theta=[0.2,]
    omega=[0,]
    T=[0,]
    for i in range(end*100):   #相当于500秒
        t=i*dt
        omega_=omega[i]+(-math.sin(theta[i])-q*omega[i]+F_D*math.sin(Omega*t))*dt
        theta_=theta[i]+omega_*dt
        
        if theta_>math.pi:
            theta_=theta_-2*math.pi
        elif theta_<-math.pi:
            theta_=theta_+2*math.pi
            
        theta.append(theta_)
        omega.append(omega_)
        T.append(t)
        
    theta=theta[int(begin*100):end*100]          #时间截断
                                                 #从begin时间开始取点
    T=T[int(begin*100):end*100]
    theta=list(map(lambda x:round(x,3),theta))   #浮点截断
                                                 #这样才能用set函数去掉重复的点
    
    theta_observed=[]
    i=0
    
    
    while i<end_zhouqi_number:
        j=int(i*zhouqi/dt)                    #取整
        theta_observed.append(theta[j])       #观测，每个原始周期观测一次
        i=i+1
    theta=theta_observed
    
    theta=list(set(theta))                    #去除重复的点
    F_D_list=[F_D,]*len(theta)
    
    return F_D_list,theta

'''下面是用于画出动图的循环，需要手动设置循环时间'''
begintime=50
while begintime<=51:    
    F_D=1.350
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.title('Bifurcation diagram   观测起始时间%3.1f秒'%begintime,fontproperties=zh)
    while F_D<=1.500:
        x,y=points(F_D,begintime)
        plt.scatter(x,y,c='b',s=0.01)
        F_D=F_D+0.001   
    plt.xlabel("驱动力F_D",fontproperties=zh)
    plt.ylabel("角度 θ(rad)",fontproperties=zh)
    begintime=begintime+0.1
    
'''下面的程序可以画出不同尺度的Bifurcation图,需要手动设置画图范围'''
begintime=53.7   #最佳观测时间
F_D=1.475
plt.figure(dpi=140,figsize=(6,4.5))
plt.title('Bifurcation diagram',fontproperties=zh)
plt.ylim(1.6,2.1)
while F_D<=1.478:
    x,y=points(F_D,begintime)
    plt.scatter(x,y,c='b',s=0.01)
    F_D=F_D+0.000002   
plt.xlabel("驱动力F_D",fontproperties=zh)
plt.ylabel("角度 θ(rad)",fontproperties=zh)
