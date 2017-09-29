# -*- coding: utf-8 -*-
'''solution to problem 1.6: A Simple Population Model'''
'''Created by 李东旭'''
'''如果你想改变参数，请直接去最后一行，调用函数的时候输入不同的参数就行啦~'''

import numpy as np
import matplotlib.pyplot as plt
'''以下两行代码用来解决中文字体在绘图时显示的问题'''
import matplotlib.font_manager as fm
zh=fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

def cal(N_0,a,b,t,dt,check=1):
    '''各个参数的含义：
       N_0:初始个体数量
       a,b:出生和死亡参数
       t  :演化时间
       dt :计算精度
       check=1 :不执行理论检验（默认）
       check=0 :执行理论检验'''
    
    N=[N_0,]
    s=t/dt
    s=int(s)
    T=np.linspace(0,t,s+1)
    
    n=N_0
    time=0
    
    '''利用欧拉法数值解常微分方程'''
    while time<=t-dt:
        n=n+(a*n-b*n**2)*dt
        N.append(n)
        time=time+dt
    N=np.array(N)
    
    '''做出数值解图像'''
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(T,N,label='数值解')
    plt.grid(True)
    plt.title('A Simple Population Model',fontsize=10)
    plt.xlabel("演化时间 t ",fontproperties=zh)
    plt.ylabel("个体数量 N",fontproperties=zh)
    
    '''当输入参数check为0时，执行解析结果检验'''
    if check==0:
        Ntheory=(a*np.exp(a*T)*N_0)/(a+b*(-1+np.exp(a*T))*N_0)  #数组运算
        '''做出理论图像'''
        plt.plot(T,Ntheory,linewidth=4,linestyle=':',label='理论值')
    plt.legend(prop=zh)                #prop=zh用来显示中文字体
    plt.ylim(0,max(N)*1.1)
    plt.text(14,0.4*max(N),'b=%5.3f'%b,fontsize=20)
    plt.text(14,0.8*max(N),'a=%5.3f'%a,fontsize=20)    
cal(100,0.6,0.001,20,0.002,0)     #在这里改变参数就可以啦！

