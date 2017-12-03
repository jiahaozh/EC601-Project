#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:36:14 2017

@author: jiahaozhang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:44:48 2017
@author: jiahaozhang
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import csv

#
#with open('data.csv') as cvsfile:
#    read = csv.reader(cvsfile,delimiter=',')
#    next(read)
#    x=list()
#    y=list()
#    for row in read:
#      i=float(row[1])
#      j=float(row[3])
#      x.append(i)
#      y.append(j)
#print(x)
#print(y)
#plt.plot(x,y,'k.')
#model=LinearRegression()
#x=np.array(x).reshape(1,-1)
#y=np.array(y).reshape(1,-1)
#model.fit(x,y)
#x1=[[6],[8],[10],[14],[18]]
#y1=model.predict(x1)
#plt.plot(x1,y1,'g.')

        
        

def runplot():
    plt.figure()
    plt.title("The relationship between sentiment score and next-day stock price change percent")
    plt.xlabel('Sentiment Score')
    plt.ylabel('Next-day stock price change(%)')
    plt.grid(True)
    return plt
runplot()
x1=[[6],[8],[10],[14],[18]]
y1=[[7],[9],[13],[17.5],[18]]
plt.plot(x1,y1,'k.')
 
# x2 is taday's sentiment score, y2 is predicted percentage change
x2=[[0],[8],[12],[16]]
model=LinearRegression()
model.fit(x1,y1)
y2=model.predict(x2)
plt.plot(x2,y2,'g-.')
print("Tomorrow's predicted percentage change is %.3f" % model.predict(12))

#model evaluation
#test sets 30% of total
x_test=[[8],[9],[11],[16],[12]]
y_test=[[11],[8.5],[15],[18],[11]]
model=LinearRegression()
model.fit(x1,y1)
b=model.score(x_test,y_test)
print(b)

#输入x1,y1为list
#x=[1,5,10,15,20]
#y=[20,-20,30,-40,60]
#a=np.cov(x,y)
#b=a[0][1]
#c=a[0][0]
#beta=b/c
#alpha=np.mean(y)-np.mean(x)*beta
#x3=[0,8,12,16,20]
#y3=x3
#for i in range(5):
#    y3[i]=x3[i]*beta+alpha
#plt.plot(x3,y3,'g-')
#yr=model.predict(x1)
#for i,j in enumerate(x1):
 #   plt.plot([j,j],[y1[i],y2[i]],'r-')
 
#残差平方和
#print("SSres is %.2f" % np.mean((model.predict(x1)-y1)**2))

#variance = np.var(x1)








