# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 18:12:41 2017
Problem 6.4 an ideal guitar string

'''Created by 李东旭'''
"""

import matplotlib.pyplot as plt
'''以下两行代码用来解决中文字体在绘图时显示的问题'''
import matplotlib.font_manager as fm
zh=fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
'''如果你用的不是Windows平台，或者缺少msyh.ttc字体，请对上一行代码做相应的调整！！'''
import numpy as np
import math

def f1(x):
    if x<=0.3:
        y=0.004*x
    else:
        y=(-0.012/7)*x+(0.012/7)
    return y

#def f2(x):
#    if x<=0.3:
#        y=0.0015*x
#    else:
#        y=(-0.0045/7)*x+(0.0045/7)
#    return y

def f3(x):
    if x<=0.5:
        y=0.004*x
    else:
        y=(-0.004)*x+(0.004)
    return y

def f4(x):
    y=0.001*math.exp(-1000*(x-0.3)**2)
    return y

#c=100 m/s
dx=0.001 #m
dt=0.00001 #s  so that r=c*dt/dx=1

L=1 #m 弦长度
N=int(L/dx+1) # 线元个数



X=np.linspace(0,L,N)
X.tolist()

def cal(fun,T):  #T为演化时间
    Y1=list(map(fun,X))
    Y2=list(map(fun,X))
    Y3=list(np.zeros(1001))
    
    t=0
    while t<=T:
        for i in range(1,N-2):
            Y3[i]=-Y1[i]+Y2[i+1]+Y2[i-1]
        for i in range(1,N-2):
            Y1[i]=-Y2[i]+Y3[i+1]+Y3[i-1]
        for i in range(1,N-2):
            Y2[i]=-Y3[i]+Y1[i+1]+Y1[i-1]
        t=t+3*dt
    return Y2


plt.figure(dpi=140,figsize=(6,4.5))

k=0
while k<=0.03:
    Y=cal(f4,k)
    plt.plot(X,Y)
    plt.xlim((0,1.1))
    plt.ylim((-0.003,0.003))
    plt.savefig('%5.4f.png'%k)
    plt.clf()
    k=k+0.0002




