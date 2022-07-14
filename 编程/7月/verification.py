# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:50:14 2022

@author: bao'bao'mao
"""
import math 
import matplotlib.pyplot as plt

fp=open('collect.txt')#读取出射角度信息
items=fp.readlines()
direct=[]
for each in items:
    each=each.split(',')
    dire=each[2]+each[3]
    direct.append(dire)

theta=[]#出射角度
for each in direct:
    xy=each.split()
    x=float(xy[0][1:])
    y=float(xy[1][:-1])
    thistheta=math.atan(y/x)
    theta.append(thistheta)

n=30 #x刻度间隔
px=[-math.pi/2+i*math.pi/n for i in range(n+1)]
py=[0 for i in range(n+1)]
for each in theta:
    for i in range(n):
        if -math.pi/2+i*math.pi/n<each<-math.pi/2+(i+1)*math.pi/n:
            py[i]+=1
        
plt.plot(px,py)#初设角度分布
fp.close()