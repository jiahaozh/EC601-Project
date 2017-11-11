#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:44:48 2017

@author: jiahaozhang
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def runplot():
    plt.figure()
    plt.title("The relationship between sentiment score and next-day stock price change percent")
    plt.xlabel('Sentiment Score')
    plt.ylabel('Next-day stock price change(%)')
    plt.grid(True)
    return plt
runplot()
x1=[[1],[5],[10],[15],[20]]
y1=[[20],[-20],[30],[-40],[60]]
plt.plot(x1,y1,'k.')

x2=[[0],[8],[12],[16],[20]]
model=LinearRegression()
model.fit(x1,y1)
y2=model.predict(x2)
plt.plot(x2,y2,'g-.')


#输入x1,y1为list
x=[1,5,10,15,20]
y=[20,-20,30,-40,60]
a=np.cov(x,y)
b=a[0][1]
c=a[0][0]
beta=b/c
alpha=np.mean(y1)-np.mean(x1)*beta
x3=[0,8,12,16,20]
y3=x3
for i in range(5):
    y3[i]=x3[i]*beta+alpha
plt.plot(x3,y3,'g-')
#残差预测值,模型的残差是训练样本点与线性回归模型的纵向距离
#yr=model.predict(x1)
#for i,j in enumerate(x1):
 #   plt.plot([j,j],[y1[i],y2[i]],'r-')
 
#残差平方和
print("SSres is %.2f" % np.mean((model.predict(x1)-y1)**2))

variance = np.var(x1)

    

