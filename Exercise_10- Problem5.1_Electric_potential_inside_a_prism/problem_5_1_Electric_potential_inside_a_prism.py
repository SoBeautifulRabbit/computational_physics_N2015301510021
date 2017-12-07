# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:30:16 2017

Problem 5.1 Electric potential inside a prism
"""
'''Created by 李东旭'''
import matplotlib.pyplot as plt
'''以下两行代码用来解决中文字体在绘图时显示的问题'''
import matplotlib.font_manager as fm
zh=fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
'''如果你用的不是Windows平台，或者缺少msyh.ttc字体，请对上一行代码做相应的调整！！'''
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
#import math

#设置初始条件
V_A=np.zeros((101,101))
V_B=np.zeros((101,101))
a=np.linspace(30,70,41,dtype=int)
for i in a:
    for j in a:
        V_A[i,j]=1
        V_B[i,j]=1

#计算部分

def calA():
    V_A[i,j]=(1/4)*(V_B[i+1,j]+V_B[i-1,j]+V_B[i,j+1]+V_B[i,j-1])

def calB():
    V_B[i,j]=(1/4)*(V_A[i+1,j]+V_A[i-1,j]+V_A[i,j+1]+V_A[i,j-1])
    _Delta=abs(float(V_B[i,j]-V_A[i,j]))
    return _Delta

list_k=[]
list_Delta=[]
    
for k in range(100):
    Delta=0
    _Delta=0
    for i in range(101):
        for j in range(101):
            if i!=0 and j!=0 and i!=100 and j!=100:
                if i in a and j not in a:
                    _Delta=calB()
                elif j in a and i not in a:
                    _Delta=calB()
                elif i not in a and j not in a:
                    _Delta=calB()
                else:
                    _Delta=0
            Delta=Delta+_Delta
    for i in range(101):
        for j in range(101):
            if i!=0 and j!=0 and i!=100 and j!=100:
                if i in a and j not in a:
                    calA()
                elif j in a and i not in a:
                    calA()
                elif i not in a and j not in a:
                    calA()
                else:
                    pass

    list_k.append(k)
    list_Delta.append(Delta)
    
addition=0
while Delta>=1e-5*101*101:
    Delta=0
    _Delta=0
    for i in range(101):
        for j in range(101):
            if i!=0 and j!=0 and i!=100 and j!=100:
                if i in a and j not in a:
                    _Delta=calB()
                elif j in a and i not in a:
                    _Delta=calB()
                elif i not in a and j not in a:
                    _Delta=calB()
                else:
                    _Delta=0
            Delta=Delta+_Delta
    for i in range(101):
        for j in range(101):
            if i!=0 and j!=0 and i!=100 and j!=100:
                if i in a and j not in a:
                    calA()
                elif j in a and i not in a:
                    calA()
                elif i not in a and j not in a:
                    calA()
                else:
                    pass
    addition=addition+1
    list_k.append(addition+100)
    list_Delta.append(Delta)

list_k=[x*2 for x in list_k]

V=V_A
#画图部分
x=list(np.linspace(-1,1,101))
y=list(np.linspace(-1,1,101))
i=0
j=0
X=[]
Y=[]
Z=[]
for i in range(101):
    for j in range(101):
        _X=x[i]
        _Y=y[j]
        _Z=float(V[i,j])
        X.append(_X)
        Y.append(_Y)
        Z.append(_Z)

fig1= plt.figure(dpi=140,figsize=(10,4.5))
ax = fig1.gca(projection='3d')
ax.plot(X, Y, Z, lw=0.7,alpha=0.6,color='darkblue')

ax.set_xlabel("X轴/m",fontproperties=zh)
ax.set_ylabel("Y轴/m",fontproperties=zh)
ax.set_zlabel("电势/V",fontproperties=zh)
ax.set_title("求解电场的拉普拉斯方程 迭代次数：%d"%list_k[-1],fontproperties=zh)

fig2= plt.figure(dpi=140,figsize=(6.5,4.5))
plt.plot(list_k,list_Delta)
plt.grid(True)
plt.title('$\Delta$V随迭代次数的变化',fontproperties=zh)
plt.xlabel("迭代次数",fontproperties=zh)
plt.ylabel("$\Delta$V",fontproperties=zh)



