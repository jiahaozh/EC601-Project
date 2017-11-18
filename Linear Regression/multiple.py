#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#优点：快速；没有调节参数；可轻易解释；可理解。
#缺点：相比其他复杂一些的模型，其预测准确率不是太高，因为它假设特征和响应之间存在确定的线性关系，这种假设对于非线性的关系，线性回归模型显然不能很好的对这种数据建模。
"""
Created on Sat Nov 18 10:59:45 2017

@author: jiahaozhang
"""
import pandas as pd
import seaborn as sns  
import matplotlib.pyplot as plt   

data=pd.read_csv('Advertising.csv')
# visualize the relationship between the features and the response using scatterplots  
sns.pairplot(data, x_vars=['TV','Radio','Newspaper'], y_vars='Sales', size=7, aspect=0.8)  
plt.show()
sns.pairplot(data, x_vars=['TV','Radio','Newspaper'], y_vars='Sales', size=7, aspect=0.8, kind='reg')  
plt.show()

data.head()


#create a python list of feature names   
X = data[['TV', 'Radio', 'Newspaper']]  
# print the first 5 rows  
print (X.head())  
# check the type and shape of X  
print (type(X))  
print (X.shape) 

# select a Series from the DataFrame  
Y = data['Sales']  
# print the first 5 values  
print (Y.head())

from sklearn.model_selection import train_test_split  #这里是引用了交叉验证  
X_train,X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1) 
#default split is 75% for training and 25% for testing
print (X_train.shape)  
print (Y_train.shape)  
print (X_test.shape)  
print (Y_test.shape)  

from sklearn.linear_model import LinearRegression  
linreg = LinearRegression()  
model=linreg.fit(X_train, Y_train)  
print (model)  
print (linreg.intercept_)
print (linreg.coef_)

# pair the feature names with the coefficients  
feature_cols = ['TV', 'Radio', 'Newspaper']  
zip(feature_cols, linreg.coef_)

Y_pred = linreg.predict(X_test)  
print (Y_pred)
print (type(Y_pred))

#计算Sales预测的RMSE  
print (type(Y_pred),type(Y_test))  
print (len(Y_pred),len(Y_test))  
print (Y_pred.shape,Y_test.shape)  
#from sklearn import metrics  
import numpy as np  
sum_mean=0  
for i in range(len(Y_pred)):  
    sum_mean+=(Y_pred[i]-Y_test.values[i])**2  
sum_erro=np.sqrt(sum_mean/50)  
# calculate RMSE by hand  
print ("RMSE by hand:",sum_erro)
print("Coefficient of determination R-squred is:%.3f" % linreg.score(X_test,Y_test))


plt.figure()  
plt.plot(range(len(Y_pred)),Y_pred,'r',label="predict")  
plt.plot(range(len(Y_pred)),Y_test,'b',label="test")  
plt.legend(loc="upper right") #显示图中的标签  
plt.xlabel("the number of sales")  
plt.ylabel('value of sales')  
plt.show()  
 
  