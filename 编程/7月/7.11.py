# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 21:30:03 2022

@author: bao'bao'mao
"""

import numpy as np
from math import *
import random
import matplotlib.pyplot as plt


fp=open("collect.txt","w") #新建文件准备写入


for en in range(5):   #重复 次，每次100个粒子
 photoncollect=[] #收集列表
 photonlist=[[] for x in range(10)]
 theta=2*pi*np.random.rand()
 for i in range(10):  
    for j in range(10):
      photonlist[j].append([[0,0],[cos(theta),sin(theta)],100,0,10*i+j]) #生成10组10个同方向粒子,并编号
      
      
      #粒子列表生成完毕，开始步进
 for t in range(500): #设置总时间
    
    for i in range(10):  
      for ii in range(10): #对每个粒子
     
      
        photonlist[i][ii][0][0]=photonlist[i][ii][0][0]+2*photonlist[i][ii][1][0]
        photonlist[i][ii][0][1]=photonlist[i][ii][0][1]+2*photonlist[i][ii][1][1]
        #步进，速度大小相同,为2
        
        
        #步进结束，开始触碰边界判断
        
        if photonlist[i][ii][0][0]>=99:  #如果碰到x=99(近似100)，视为出射被收集
            a=photonlist[i][ii] 
            num=a[4]
            tag=1
            if photoncollect==[]:
                tag=1
            else: 
              
               for k in photoncollect: #检查collect是否有同样的粒子，防止冗余
                  if k[4]==num:
                      tag=0
            if tag==1:   
              a.append(t)
              if a[0][0]>=99:
                photoncollect.append(a)#粒子被收集,加入时间元素
             
            
        if abs(photonlist[i][ii][0][0])>=99 and photonlist[i][ii][3]==0 :    #如果第一次碰撞
            for j in range(10):
               theta=pi/2+pi*np.random.rand() if photonlist[i][ii][0][0]>0 else -pi/2+pi*np.random.rand()
               
               for k in range(10):
                newdir=[cos(theta),sin(theta)]
                photonlist[j][k]=list(photonlist[j][k])                
                photonlist[j][k][1]=newdir  #将100个相同的粒子变成10*10的粒子
                photonlist[j][k][3]+=1      #碰撞数加1
                # photon2=Photon(photonlist[j][k][0],photonlist[j][k][1],photonlist[j][k][2],photonlist[j][k][3],photonlist[i][j][4])
                # photonlist[j][k]=photon2.step()  #步进一，防止反复触发第一次碰撞条件
   
        if abs(photonlist[i][ii][0][1])>=99 and photonlist[i][ii][3]==0 :    #如果第一次碰撞,y方向
            for j in range(10):
               theta=-pi+pi*np.random.rand() if photonlist[i][ii][0][1]>0 else pi*np.random.rand()
               
               for k in range(10):
                newdir=[cos(theta),sin(theta)]
                photonlist[j][k]=list(photonlist[j][k])                
                photonlist[j][k][1]=newdir  #将100个相同的粒子变成10*10的粒子
                photonlist[j][k][3]+=1      #碰撞数加1
                # photon2=Photon(photonlist[j][k][0],photonlist[j][k][1],photonlist[j][k][2],photonlist[j][k][3],photonlist[i][j][4])
                # photonlist[j][k]=photon2.step()  #步进一，防止反复触发第一次碰撞条件
   
        if abs(photonlist[i][ii][0][0])>=99 and photonlist[i][ii][3]==1 :    #如果第二次碰撞 
             for j in range(10):
                 theta=pi/2+pi*np.random.rand() if photonlist[i][ii][0][0]>0 else -pi/2+pi*np.random.rand()
                 newdir=[cos(theta),sin(theta)]
                 photonlist[i][j]=list(photonlist[i][j])
                 photonlist[i][j][1]=newdir
                 photonlist[i][j][3]+=1
                 
                 
                 
        if abs(photonlist[i][ii][0][1])>=99 and photonlist[i][ii][3]==1 :    #如果第二次碰撞 ,y
             for j in range(10):
                 theta=-pi+pi*np.random.rand() if photonlist[i][ii][0][1]>0 else pi*np.random.rand()
                 newdir=[cos(theta),sin(theta)]
                 photonlist[i][j]=list(photonlist[i][j])
                 photonlist[i][j][1]=newdir
                 photonlist[i][j][3]+=1
                 
                 
        
        if  abs(photonlist[i][ii][0][0])>=99 and photonlist[i][ii][3]>1 :  #第二次之后碰撞
            theta=pi/2+pi*np.random.rand() if photonlist[i][ii][0][0]>0 else -pi/2+pi*np.random.rand()
            newdir=[cos(theta),sin(theta)]
            photonlist[i][ii]=list(photonlist[i][ii])
            photonlist[i][ii][1]=newdir
            photonlist[i][ii][3]+=1
            
            
            
        if  abs(photonlist[i][ii][0][1])>=99 and photonlist[i][ii][3]>1 :  #第二次之后碰撞,y
            theta=-pi+pi*np.random.rand() if photonlist[i][ii][0][1]>0 else pi*np.random.rand()
            newdir=[cos(theta),sin(theta)]
            photonlist[i][ii]=list(photonlist[i][ii])
            photonlist[i][ii][1]=newdir
            photonlist[i][ii][3]+=1
            
        
        
 
 print(photoncollect)
    
 for i in range(len(photoncollect)):  #把收集列表转化为列表格式
  a=str(photoncollect[i])
  fp.write(a+"\n")
  photoncollect[i][0]=list(photoncollect[i][0])
  photoncollect[i]=list(photoncollect[i])
 #print(photoncollect)      
  
 # for l in range(10):
 #      for m in range(10):
 #        plt.scatter(photonlist[l][m][0][0],photonlist[l][m][0][1])
        
 for i in photoncollect:
     plt.scatter(i[0][0],i[0][1])