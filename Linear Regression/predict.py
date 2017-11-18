#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:31:24 2017

@author: jiahaozhang
"""

import matplotlib.pyplot as plt  
import pandas as pd  
from sklearn import linear_model
from sklearn.model_selection import train_test_split    

# Function to get data  
def get_data(file_name):  
 data = pd.read_csv(file_name)  #here ,use pandas to read cvs file.  
 X_parameters = []  
 Y_parameters = []  
 for i ,j in zip(data['close'],data['high']):  
       X_parameters.append([float(i)])#store in corresponding lists  
       Y_parameters.append([float(j)])  
 return X_parameters,Y_parameters 


#Function for Fitting our data to Linear model  
def linear_model_main(X_parameters,Y_parameters,predict_value):
 X_train,X_test, Y_train, Y_test = train_test_split(X_parameters, Y_parameters, random_state=1) 
#default split is 75% for training and 25% for testing    
 # Create linear regression object  
 regr = linear_model.LinearRegression()  
 regr.fit(X_train, Y_train)   #train model  
 predict_outcome = regr.predict(predict_value)  
 predictions = {}  
 predictions['intercept'] = regr.intercept_  
 predictions['coefficient'] = regr.coef_  
 predictions['predicted_value'] = predict_outcome  
 return predictions  
# Function to show the resutls of linear fit model  
def show_linear_line(X_parameters,Y_parameters):  
 # Create linear regression object
 X_train,X_test, Y_train, Y_test = train_test_split(X_parameters, Y_parameters, random_state=1) 
 #default split is 75% for training and 25% for testing    
 regr = linear_model.LinearRegression()  
 regr.fit(X_train, Y_train)
 plt.scatter(X_test,Y_test,color='blue')  
 plt.plot(X_test,regr.predict(X_test),color='red',linewidth=2) 
 plt.title("The relationship between sentiment score and next-day stock price change percent")
 plt.xlabel('Sentiment Score')
 plt.ylabel('Next-day stock price change(%)')
 plt.grid(True) 
 plt.xticks(())  
 plt.yticks(())  
 plt.show()
 #R square
 print("Coefficient of determination R-squred is:%.3f" % regr.score(X_test,Y_test))

 
 
X,Y = get_data('data.csv')
#print(X)
#print(Y)
print(X[0][0])
predictvalue = X[0][0]
result = linear_model_main(X,Y,predictvalue)  
print ("Intercept value " , result['intercept'])
print ("coefficient" , result['coefficient']) 
print ("Predicted value: ",result['predicted_value'])
show_linear_line(X,Y)
