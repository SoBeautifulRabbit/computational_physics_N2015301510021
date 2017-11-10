# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:52:53 2017"""


'''solution to problem 3.33: Power Spectrum for
 the Driven Nonlinear Pendulum'''
'''Created by 李东旭'''

import matplotlib.pyplot as plt
'''以下两行代码用来解决中文字体在绘图时显示的问题'''
import matplotlib.font_manager as fm
zh=fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
'''如果你用的不是Windows平台，请对上一行代码做相应的调整！！'''
import math

#Omega=2/3
#zhouqi=3*math.pi
#dt=0.01

class bai:
    def __init__(self,F=1.2,q=0.5,t_begin=100,t_end=500):
        #g/l=1 分别为重力加速度和摆长
        self.F=F
        self.q=q
        self.t_end=t_end
        self.Omega=2/3
        self.t_begin=t_begin
        
    def cal(self):
        theta=[0.2,]
        omega=[0,]
        T=[0,]
        i=0
        t=0
        dt=0.01

        while t<self.t_end:
            omega_=omega[i]+(-math.sin(theta[i])-self.q*omega[i]+self.F*math.sin(self.Omega*t))*dt
            theta_=theta[i]+omega_*dt
            
            if theta_>math.pi:
                theta_=theta_-2*math.pi
            elif theta_<-math.pi:
                theta_=theta_+2*math.pi
                
            theta.append(theta_)
            omega.append(omega_)
            t=t+dt
            i=i+1
            T.append(t)
            
        theta=theta[int(self.t_begin*100):self.t_end*100]   #时间截断
        T=T[int(self.t_begin*100):self.t_end*100]
        omega=omega[int(self.t_begin*100):self.t_end*100]
        return theta,T,omega,self.F
    
def show(bai):    #绘图函数
    T=bai[1]
    theta=bai[0]
    F=bai[3]
    
    fig=plt.figure(dpi=140,figsize=(6,9))
    real=fig.add_subplot(2,1,1)
    real.plot(T,theta)
    plt.xlim((100,200))
    plt.grid(True)
    plt.title('物理摆实空间图 驱动力振幅F=%3.2f'%F,fontproperties=zh)
    plt.xlabel("时间 t(s)",fontproperties=zh)
    plt.ylabel("角度 θ(rad)",fontproperties=zh)
    
    fourier=fig.add_subplot(2,1,2)
    fourier.psd(theta,NFFT=len(T),pad_to=len(T),noverlap=0,Fs=100,c='orange')
    plt.vlines(0.1061033, -100, 100, colors = "m", linestyles = "dashed") #f=1/zhouqi=0.1061033
    plt.xlim((0.01,1.5))
    
    plt.yscale('symlog')
    plt.title('Power Spectrum 驱动力振幅F=%3.2f'%F,fontproperties=zh)
    
    
bai1=bai(0.5)
result1=bai1.cal()
show(result1)

bai2=bai(0.95)
result2=bai2.cal()
show(result2)

bai3=bai(1.2)
result3=bai3.cal()
show(result3)

bai4=bai(1.44)
result4=bai4.cal()
show(result4)

bai5=bai(0.96)
result5=bai5.cal()
show(result5)

bai6=bai(0.97)
result6=bai6.cal()
show(result6)

bai7=bai(0.98)
result7=bai7.cal()
show(result7)

bai8=bai(0.99)
result8=bai8.cal()
show(result8)

bai9=bai(1.00)
result9=bai9.cal()
show(result9)

bai10=bai(1.40)
result10=bai10.cal()
show(result10)

bai11=bai(1.41)
result11=bai11.cal()
show(result11)

bai12=bai(1.42)
result12=bai12.cal()
show(result12)

bai13=bai(1.43)
result13=bai13.cal()
show(result13)

bai14=bai(1.44)
result14=bai14.cal()
show(result14)