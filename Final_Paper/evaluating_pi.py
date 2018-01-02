# -*- coding: utf-8 -*-
"""
Created by Li Dongxu (2015301510021) on Tue Dec 26 10:29:50 2017
Final paper : Evaluating Pi by random progress
"""

'''警告！在PC上运行本程序的全部内容可能需要10小时或者更长的时间，
因此将大部分调用函数进行计算并生成结果的命令写成了以#为开头的注释形式。
如果运行相应的部分并查看结果，请手动去掉#，就可以运行该命令。'''

'''以下两行代码用来解决中文字体在绘图时显示的问题'''
import matplotlib.font_manager as fm
zh=fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

'''如果你用的不是Windows平台，或者缺少msyh.ttc字体，请对上一行代码做相应的调整。'''

import random as rd
import math
import matplotlib.pyplot as plt
import numpy as np
import time
import scipy.io as sio  
np.set_printoptions(threshold=np.inf)

#这个类完整地包含了进行Buffon投针的所有动作
class Buffon_MonteCarlo:
    
    #l为针的长度，size为白纸尺寸，N为投针次数
    def __init__(self,l,size,N):
        self.size=size
        self.N=N
        self.l=l #针的长度
        self.counter=0  #相交次数
        if self.size<20:
            print('您选的纸的size太小了，不能做这个实验，建议将size设为100或更大')
        if self.size<2*self.l:
            print('针的长度必须比纸的边长的一半小')
            
    #画平行线        
    def drawlines(self):
        lines=np.zeros((self.size,), dtype=np.int)
        i=int(self.l/2) #在针的长度的一半的位置画第一条线
        while i<=self.size-1:
            lines[i]=1
            i=i+self.l
        return lines
    
    #扔一次针
    def toss(self,lines):
        self.lines=lines
        #确定针眼的位置
        #x_0=rd.randint(self.l,self.size-self.l)  #这一步计算是不需要的
        y_0=rd.randint(self.l,self.size-self.l)
        
        #确定针尖的位置(本程序误差瓶颈)
        theta=rd.uniform(0,360)
        #x=round(x_0+self.l*math.cos(math.radians(theta))) #这一步计算是不需要的
        y=round(y_0+self.l*math.sin(math.radians(theta)))  #四舍五入取整

        #判断是否跨过平行线
        upper=max(y,y_0)
        lower=min(y,y_0)
        delta=0 #计数器的辅助变量
        
          #如果其中有跨过平行线的点，那么记一次相交
        _randomone=rd.uniform(0,1)
        if _randomone>0.6366197723675814:
            randomone=1
        else:
            randomone=0
        if upper!=lower:
            for k in range(lower,upper-randomone):   #减去其中一个端点的投影值
                delta=delta+lines[k]
            if delta>0.0001:
                self.counter=self.counter+1
          #如果针躺在平行线上也要记一次相交        
        else:
            if lines[upper]-1<0.0001:
                self.counter=self.counter+1
                
    #开展一次实验，包含画线和投针
    def experiment(self):
        lines=self.drawlines()
        for i in range(self.N):
            self.toss(lines)
            #if i %1000000 ==0:
                #print(i/1000000)  #每投针1e6次输出一个数字来显示进度
        probability=self.counter/self.N  #相交概率
        return probability


#这个函数实例化上方定义的类，返回估算的pi值
def cal(l=300,size=1500,N=10000):  
    Buffon=Buffon_MonteCarlo(l,size,N)
    p=Buffon.experiment()
    estimated_pi=2/p
    return estimated_pi


#这个函数用来执行投针次数非常多的模拟，输入你可以承受的运算时间（有40,400,4000,40000
#秒四挡可以选择），函数会显示估算的pi值和运算实际花费的时间。  
def cal_extreme(Time): #Time是你可以承受的运算时间，单位：秒
    l=300
    size=1500
    
    if Time==40000:
        #N=1000000000  #1e9是个人电脑的运算极限，将它拆分为4x2.5e8行并行计算(4核心)
        N=250000000
    elif Time==4000:
        #N=100000000  #将1e8拆分为4x2.5e7并行计算(4核心)
        N=25000000
    elif Time==400:
        N=10000000
    elif Time==40:
        N=1000000

    time_start=time.time()
    Buffon=Buffon_MonteCarlo(l,size,N)
    p=Buffon.experiment()
    estimated_pi=2/p
    time_end=time.time()
    
    T=time_end-time_start
    print('estimated_pi=',estimated_pi)
    print('computing time=',T)
    return estimated_pi


#这个函数用来探究针的长度对误差的影响
def err1(lengthmin,lengthmax,size):
    Lengths=np.linspace(lengthmin,lengthmax,num=200,dtype=int)
    Estimated_pi=[]
    Errors=[]
    for l in Lengths:
        l=int(l)  #将np.float64形式转化为int形式
        _pi=cal(l,size)
        Estimated_pi.append(_pi)
        _error=(abs(_pi-math.pi))/math.pi
        Errors.append(_error)
    
    #相邻的10个l值的结果取平均
    X=[]
    Y_pi=[]
    Y_error=[]
    for i in range(20):
        X.append(Lengths[10*i+5])
        sum_pi=0
        sum_error=0
        for k in range(10):
            sum_pi+=Estimated_pi[10*i+k]
            sum_error+=Errors[10*i+k]
        Y_pi.append(sum_pi/10)
        Y_error.append(sum_error/10)

    plt.figure(dpi=140,figsize=(6,4.5))
    plt.title('针的长度与π的估算值的关系',fontproperties=zh)
    plt.hlines(math.pi,min(X),max(X))
    plt.plot(X,Y_pi)
    plt.scatter(X,Y_pi)
    plt.ylim((3.00,3.28))
    plt.xlabel('针的长度 l',fontproperties=zh)
    plt.ylabel('π的估算值',fontproperties=zh)
    plt.text(max(X),math.pi,'π',fontproperties=zh)
    
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.title('针的长度与相对误差的关系',fontproperties=zh)
    plt.plot(X,Y_error,c='r')
    plt.scatter(X,Y_error,c='r',marker='s')
    plt.ylim((0,0.05))
    plt.xlabel('针的长度 l',fontproperties=zh)
    plt.ylabel('相对误差',fontproperties=zh)
    

#这个函数用来探究纸张大小对误差的影响
def err2(sizemin,sizemax):
    Sizes=np.linspace(sizemin,sizemax,num=200,dtype=int)
    Estimated_pi=[]
    Errors=[]
    l=300  
    for size in Sizes:
        size=int(size)  #将np.float64形式转化为int形式
        _pi=cal(l,size)
        Estimated_pi.append(_pi)
        _error=(abs(_pi-math.pi))/math.pi
        Errors.append(_error)
        
    #相邻的10个l值的结果取平均
    X=[]
    Y_pi=[]
    Y_error=[]
    for i in range(20):
        X.append(Sizes[10*i+5])
        sum_pi=0
        sum_error=0
        for k in range(10):
            sum_pi+=Estimated_pi[10*i+k]
            sum_error+=Errors[10*i+k]
        Y_pi.append(sum_pi/10)
        Y_error.append(sum_error/10)

    plt.figure(dpi=140,figsize=(6,4.5))
    plt.title('纸的边长与π的估算值的关系',fontproperties=zh)
    plt.hlines(math.pi,min(X),max(X))
    plt.plot(X,Y_pi)
    plt.scatter(X,Y_pi)
    plt.ylim((3.00,3.28))
    plt.xlabel('纸的边长 size',fontproperties=zh)
    plt.ylabel('π的估算值',fontproperties=zh)
    plt.text(max(X),math.pi,'π',fontproperties=zh)
    
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.title('纸的边长与相对误差的关系',fontproperties=zh)
    plt.plot(X,Y_error,c='r')
    plt.scatter(X,Y_error,c='r',marker='s')
    plt.ylim((0,0.05))
    plt.xlabel('纸的边长 size',fontproperties=zh)
    plt.ylabel('相对误差',fontproperties=zh)


#这个函数用来探究投针次数对误差的影响
def err3(Nmin,Nmax):
    Ns=np.linspace(Nmin,Nmax,num=200,dtype=int)
    Estimated_pi=[]
    Errors=[]
    l=300
    size=1500
    for N in Ns:
        N=int(N)  #将np.float64形式转化为int形式
        _pi=cal(l,size,N)
        Estimated_pi.append(_pi)
        _error=(abs(_pi-math.pi))/math.pi #注意这里取了绝对值
        Errors.append(_error)
        
    #相邻的10个l值的结果取平均
    X=[]
    Y_pi=[]
    Y_error=[]
    for i in range(20):
        X.append(Ns[10*i+5])
        sum_pi=0
        sum_error=0
        for k in range(10):
            sum_pi+=Estimated_pi[10*i+k]
            sum_error+=Errors[10*i+k]
        Y_pi.append(sum_pi/10)
        Y_error.append(sum_error/10)

    plt.figure(dpi=140,figsize=(6,4.5))
    plt.title('投针次数与π的估算值的关系',fontproperties=zh)
    plt.hlines(math.pi,min(X),max(X))
    plt.plot(X,Y_pi)
    plt.scatter(X,Y_pi)
    plt.ylim((3.00,3.28))
    plt.xlabel('投针次数 N',fontproperties=zh)
    plt.ylabel('π的估算值',fontproperties=zh)
    plt.text(max(X),math.pi,'π',fontproperties=zh)
    
    plt.figure(dpi=140,figsize=(6,4.5))
    plt.title('投针次数与相对误差的关系',fontproperties=zh)
    plt.plot(X,Y_error,c='r')
    plt.scatter(X,Y_error,c='r',marker='s')
    plt.ylim((0,0.05))
    plt.xlabel('投针次数 N',fontproperties=zh)
    plt.ylabel('相对误差',fontproperties=zh)


#这个函数用来绘制固定N并重复20次实验的结果散点分布图
def err4(fixed_N):
    X=[]
    Y=[]
    for k in range(20):
        _y=cal(300,1500,fixed_N)
        X.append(k)
        Y.append(_y)

    plt.figure(dpi=140,figsize=(6,4.5))
    plt.title('投针次数N=%d'%fixed_N,fontproperties=zh)
    plt.hlines(math.pi,min(X),max(X))
    plt.scatter(X,Y)
    plt.ylim((3.00,3.28))
    plt.ylabel('π的估算值',fontproperties=zh)
    plt.text(max(X),math.pi,'π',fontproperties=zh)
    #去掉x轴，因为x轴在本图中没有意义
    frame=plt.gca()
    frame.axes.get_xaxis().set_visible(False)


#以下代码为准蒙特卡罗方法
class Buffon_QuasiMonteCarlo(Buffon_MonteCarlo):
    
    #准随机数列长度只有1e8，所以N不能大于5e7次。
    def quasi_random(self):
        path='C:\\Users\\LDX\\Documents\\真正的文档\\学习\\物\
理\\计算物理\\FINAL\\halton\\halton.mat'
        
        '''这个文件的大小接近200mb，它所提供的准随机数列可以允许的最大
        投针次数为5e6次。如果要做另一次准蒙特卡罗模拟，需要重新用MATLAB
        生成一个新的数组，否则只会得出相同的结果'''
        
        matfile=sio.loadmat(path) #读取matlab生成的mat文件
        halton=matfile['X0']
        Halton=[] #在python中产生准随机数的list
        for k in range(2*self.N): #投N次针共需要2N个准随机数
            _halton=float(halton[k])
            Halton.append(_halton)
        return Halton
           
    def toss(self,lines,index):
        self.lines=lines
        #确定针眼的位置
        #x_0=rd.randint(self.l,self.size-self.l)  #这一步计算是不需要的
        y_0=int(round(abs(self.l-(self.size-self.l)))*self.Halton[index]+self.l)
        
        #确定针尖的位置(本程序误差瓶颈)
        theta=int(round(360*self.Halton[-index]))
        #x=round(x_0+self.l*math.cos(math.radians(theta))) #这一步计算是不需要的
        y=int(round(y_0+self.l*math.sin(math.radians(theta))))  #四舍五入取整

        #判断是否跨过平行线
        upper=max(y,y_0)
        lower=min(y,y_0)
        delta=0 #计数器的辅助变量
        
          #如果其中有跨过平行线的点，那么记一次相交
        _randomone=rd.uniform(0,1)
        if _randomone>0.6366197723675814:
            randomone=1
        else:
            randomone=0

        if upper!=lower:
            for k in range(lower,upper-randomone):
                delta=delta+lines[k]
            if delta>0.0001:
                self.counter=self.counter+1
          #如果针躺在平行线上也要记一次相交        
        else:
            if lines[upper]-1<0.0001:
                self.counter=self.counter+1
                
    def experiment(self):
        lines=self.drawlines()
        for i in range(self.N):
            self.toss(lines,index=i)
            if i %1000000 ==0:
                print(i/1000000)
        probability=self.counter/self.N  #相交概率
        return probability
    
    def estimate(self):
        '''这里把Halton作为类属性而不是函数里的一个局域变量，是因为
        (1)它是常量，不随计算改变
        (2)如果不将它作为类属性，每次循环都要重新读取mat文件，会将程序整体的速度
        减小到现有程序速度的千分之一一下'''
        
        self.Halton=self.quasi_random()
        p=self.experiment()
        #print('probability=',p)
        print('estimated Pi=',2/p)

#用准蒙特卡罗方法计算
def cal_quasi_montecarlo(size=1000000000,N=5000000):
    Buffon2=Buffon_QuasiMonteCarlo(300,size,N)
    Buffon2.quasi_random()
    Buffon2.estimate()

#以下代码用于生成论文中的算法介绍的示意图，不返回计算结果
class my_demo(Buffon_MonteCarlo):
    def drawlines1(self):
        lines=[]
        i=int(self.l/2) #在针的长度的一半的位置画第一条线
        while i<=self.size-1:
            _lines=i
            lines.append(_lines)
            i=i+self.l
        return lines
    
    def plotlines(self):
        y=self.drawlines1()    
        print(y)
        plt.figure(dpi=140,figsize=(6,4.5))
        plt.title('在白纸上画一些平行线',fontproperties=zh)
        plt.hlines(y,0,self.size)
        plt.xlim((0,100))
        plt.ylim((0,100))
        
    #扔一次针    
    def toss(self):  
        #确定针眼的位置
        x_0=round(rd.uniform(self.l,self.size-self.l))
        y_0=rd.randint(self.l,self.size-self.l)
        
        #确定针尖的位置(本程序误差瓶颈)
        theta=rd.uniform(0,360)
        x=round(x_0+self.l*math.cos(math.radians(theta)))  
        y=round(y_0+self.l*math.sin(math.radians(theta)))  #四舍五入取整
        return x_0,y_0,x,y
    
    #画出投针示意图
    def plotneedles(self):
        X=[0,0]
        Y=[0,0]
        fig=plt.figure(dpi=140,figsize=(6,4.5))
        plt.title('投针（50根）',fontproperties=zh)
        plt.xlim((0,100))
        plt.ylim((0,100))
        for i in range(self.N):
            x_0,y_0,x,y=self.toss()
            X[0]=x_0
            X[1]=x
            Y[0]=y_0
            Y[1]=y
            plt.plot(X,Y)
        plt.hlines(self.drawlines1(),0,self.size)


'''以下为计算命令，请根据需要去掉前方的#来执行运算'''
#err1(2,600,1200)        #两端误差都大
#err1(300,5000,10000)    #左端误差小，右端误差大
#err1(300,1000,10000)    #两端误差都很小

#err2(600,3000)          #左边误差大
#err2(3000,100000)       #两端误差都很小

#err3(100,2000)
#err3(2000,100000)

#err4(1000)
#err4(10000)
#err4(100000)
#err4(1000000)

cal_extreme(40)
#cal_extreme(400)
#cal_extreme(4000)  #需要并行计算，用4个内核分别调用此函数后求平均
#cal_extreme(40000) #需要并行计算，用4个内核分别调用此函数后求平均

#cal_quasi_montecarlo(10000,50000000)
#cal_quasi_montecarlo(1000000000,5000000)

#demo=my_demo(10,100,50)
#demo.plotlines()
#demo.plotneedles()