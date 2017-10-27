# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:42:30 2017"""

'''solution to problem 3.10: Chaos in the Driven Nonlinear Pendulum'''
'''Created by 李东旭'''

import matplotlib.pyplot as plt
'''以下两行代码用来解决中文字体在绘图时显示的问题'''
import matplotlib.font_manager as fm
zh=fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
'''如果你用的不是Windows平台，请对上一行代码做相应的调整！！'''
import math

class bai:
    def __init__(self,F=1.2,q=0.5,t_end=80):
        #g/l=1 分别为重力加速度和摆长
        self.F=F
        self.q=q
        self.t_end=t_end
        self.Omega=2/3
        
    def cal(self):
        theta=[0.2,]
        omega=[0,]
        T=[0,]
        i=0
        t=0
        dt=0.04

        while t<self.t_end:
            omega_=omega[i]+(-math.sin(theta[i])-self.q*omega[i]+self.F*math.sin(self.Omega*t))*dt
            theta_=theta[i]+omega_*dt
            theta.append(theta_)
            omega.append(omega_)
            t=t+dt
            i=i+1
            T.append(t)
        return theta,T,omega,self.F

def show(bai):    #绘图函数
    T=bai[1]
    theta=bai[0]
    F=bai[3]
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(T,theta,label='驱动力振幅F=%2.1f'%F)
#    plt.xlim((0,80))
#    plt.ylim((-35,35))
    plt.grid(True)
    plt.title('物理摆实空间图',fontproperties=zh)
    plt.xlabel("时间 t(s)",fontproperties=zh)
    plt.ylabel("角度 θ(rad)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体
    
def showpq(bai):
    theta=bai[0]
    omega=bai[2]
    F=bai[3]
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(theta,omega,label='驱动力振幅F=%2.1f'%F)
    plt.grid(True)
    plt.title('物理摆相空间图',fontproperties=zh)
    plt.xlabel("角度 θ(rad)",fontproperties=zh)
    plt.ylabel("角速度 ω(rad/s)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体
    
bai1=bai(0)
bai2=bai(0.1)
bai3=bai(0.5)
bai4=bai(0.99)
bai5=bai(1.2)
bai6=bai(100)        

for j in (1,2,3,4,5,6):
    exec('result%d=bai%d.cal()'%(j,j))
    exec('show(result%d)'%(j))
    exec('showpq(result%d)'%(j))
    

bai_longtime1=bai(1.2,0.5,300)
result_extreme1=bai_longtime1.cal()
show(result_extreme1)
showpq(result_extreme1)

bai_longtime2=bai(1.2,0.5,100000)
result_extreme2=bai_longtime2.cal()
show(result_extreme2)
showpq(result_extreme2)
        