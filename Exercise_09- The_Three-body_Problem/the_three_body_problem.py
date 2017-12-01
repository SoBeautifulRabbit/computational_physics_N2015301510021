# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:05:59 2017

The three-body problem
"""
'''Created by 李东旭'''
import matplotlib.pyplot as plt
'''以下两行代码用来解决中文字体在绘图时显示的问题'''
import matplotlib.font_manager as fm
zh=fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
'''如果你用的不是Windows平台，请对上一行代码做相应的调整！！'''
import math

G=39.43
def threebody(x_A,y_A,x_B,y_B,x_C,y_C,v_Ax,v_Ay,v_Bx,v_By,v_Cx,v_Cy,M_A,M_B,M_C,T):
    
    #检查质心是否静止
    center_x=v_Ax*M_A+v_Bx*M_B+v_Cx*M_C
    center_y=v_Ay*M_A+v_By*M_B+v_Cy*M_C
    if center_x<=0.00000000001 and center_y<=0.00000000001:
        print('yes')
    else:
        print('no')
        return
    
    #创建列表：坐标
    L_x_A=[x_A,]
    L_y_A=[y_A,]
    L_x_B=[x_B,]
    L_y_B=[y_B,]
    L_x_C=[x_C,]
    L_y_C=[y_C,]
    
    #创建列表：速度
    L_v_Ax=[v_Ax,]
    L_v_Ay=[v_Ay,]
    L_v_Bx=[v_Bx,]
    L_v_By=[v_By,]
    L_v_Cx=[v_Cx,]
    L_v_Cy=[v_Cy,]
    
    i=0
    dt=0.001
    while i<=(int(T/dt)):
        #计算恒星之间的距离
        r_AB=math.sqrt((L_x_A[i]-L_x_B[i])**2+(L_y_A[i]-L_y_B[i])**2)
        r_AC=math.sqrt((L_x_A[i]-L_x_C[i])**2+(L_y_A[i]-L_y_C[i])**2)
        r_BC=math.sqrt((L_x_B[i]-L_x_C[i])**2+(L_y_B[i]-L_y_C[i])**2)
        
        #计算恒星之间的引力
        f_AB=G*M_A*M_B/((r_AB)**2)
        f_AC=G*M_A*M_B/((r_AC)**2)
        f_BC=G*M_A*M_B/((r_BC)**2)
        
        #计算引力的分量
        f_ABx=f_AB*(L_x_B[i]-L_x_A[i])/r_AB
        f_ABy=f_AB*(L_y_B[i]-L_y_A[i])/r_AB
        f_ACx=f_AC*(L_x_C[i]-L_x_A[i])/r_AC
        f_ACy=f_AC*(L_y_C[i]-L_y_A[i])/r_AC
        f_BCx=f_BC*(L_x_C[i]-L_x_B[i])/r_BC
        f_BCy=f_BC*(L_y_C[i]-L_y_B[i])/r_BC
        
        #计算下一时刻的速度
        _v_Ax=L_v_Ax[i]+dt*(f_ABx+f_ACx)/M_A
        _v_Ay=L_v_Ay[i]+dt*(f_ABy+f_ACy)/M_A
        _v_Bx=L_v_Bx[i]+dt*(-f_ABx+f_BCx)/M_B
        _v_By=L_v_By[i]+dt*(-f_ABy+f_BCy)/M_B
        _v_Cx=L_v_Cx[i]+dt*(-f_ACx-f_BCx)/M_C
        _v_Cy=L_v_Cy[i]+dt*(-f_ACy-f_BCy)/M_C
        
        #用E-U方法计算下一时刻的坐标
        _x_A=L_x_A[i]+dt*_v_Ax
        _y_A=L_y_A[i]+dt*_v_Ay
        _x_B=L_x_B[i]+dt*_v_Bx
        _y_B=L_y_B[i]+dt*_v_By
        _x_C=L_x_C[i]+dt*_v_Cx
        _y_C=L_y_C[i]+dt*_v_Cy
    
        #写入列表：坐标
        L_x_A.append(_x_A)
        L_y_A.append(_y_A)
        L_x_B.append(_x_B)
        L_y_B.append(_y_B)
        L_x_C.append(_x_C)
        L_y_C.append(_y_C)
        
        #写入列表：速度
        L_v_Ax.append(_v_Ax)
        L_v_Ay.append(_v_Ay)
        L_v_Bx.append(_v_Bx)
        L_v_By.append(_v_By)
        L_v_Cx.append(_v_Cx)
        L_v_Cy.append(_v_Cy)
        
        #检测碰撞
        if r_AB<=0.01 or r_AC<=0.01 or r_BC<=0.01:
            print('collide!')
            i=int(T/dt)
        
        i=i+1
        
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.plot(L_x_A,L_y_A,label='A星 质量%2.1f'%M_A)
    plt.plot(L_x_B,L_y_B,label='B星 质量%2.1f'%M_B)
    plt.plot(L_x_C,L_y_C,label='C星 质量%2.1f'%M_C)
    plt.grid(False)
    plt.title('三体问题 演化时间：%d年'%T,fontproperties=zh)
    plt.xlabel("x (AU)",fontproperties=zh)
    plt.ylabel("y (AU)",fontproperties=zh)
    plt.legend(prop=zh)                #prop=zh用来显示中文字体
    print(x_A,y_A,';',x_B,y_B,';',x_C,y_C,';;;',v_Ax,v_Ay,';',v_Bx,v_By,';',v_Cx,v_Cy)
    
threebody(8.5,5,-8.5,5,0,-10,-1.425,1.45,-0.575,-1.95,2,0.5,1,1,1,2500)
        
        
        
        
    
    