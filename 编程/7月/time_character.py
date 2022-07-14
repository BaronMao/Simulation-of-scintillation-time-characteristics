# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 19:04:28 2022

@author: bao'bao'mao
"""

import math 
import matplotlib.pyplot as plt

fp=open('collect.txt')#读取出射角度信息
items=fp.readlines()
time=[]
for each in items:
    each=each.split(',')
    eachtime=each[7]
    if len(eachtime)==6 :
        time.append(int(eachtime[-5:-2]))
    else:
        time.append(int(eachtime[-4:-2]))

print(time)
n=20 #x刻度间隔
t=1000 #总时间
px=[i*t/n for i in range(n+1)]
py=[0 for i in range(n+1)]
for each in time:
    for i in range(n):
        if i*t/n<each<(i+1)*t/n:
            py[i]+=1
        
plt.plot(px,py)#初设角度分布
fp.close()