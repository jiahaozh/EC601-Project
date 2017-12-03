#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:31:24 2017

@author: abhivora
"""
import pandas as pd
import datetime
import numpy as np

def get_data(file_name):
 data = pd.read_csv(file_name)
 day = []
 sentiment= []
 for i,j in zip(data['sentiment'],data['time']):
        sentiment.append(i)
        day.append(j)
 return day,sentiment       
        

day,sentiment = get_data('news_6.csv')   

year = []
month =[]
new_day =[]
whole_date=[]
for i in range(len(day)):   # THIS LOOP REMOVES THE TIME AND THE UNWANTED CHARACTERS IN THE TIME COLUMN I.E TO KEEP ONLY THE DATE
       
     year.append(int(day[i][0:4]))   
     month.append(int(day[i][5:7]))
     new_day.append(int(day[i][8:10])) #Type casting to make compatible for the date to day function
     whole_date.append(day[i][0:10])  
     


weekday = [];                   # THIS PART HELPS US GET THE DAY From the date

DayL = ['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun']
for i in range(len(day)):
    
  a=year[i]
  b=month[i]
  c=new_day[i]
  weekday.append(DayL[datetime.date(a,b,c).weekday()] + 'day')

  

news_date_sentiment = {} # MADE A EMPTY DICTIONARY, WHERE THE KEY = DATE.
for i in whole_date:
    news_date_sentiment[i] = []



for key in news_date_sentiment: # THIS CODE COMPILES ALL THE SENTIMENT FOR 1 DAY AND APPENDS IT TO THE DICT 
    for j in range(len(whole_date)):
        if key==whole_date[j]:
            news_date_sentiment[key].append(sentiment[j])
            
positive_count=[]  # THESE LISTS KEEP A COIUNT OF THE NUMBER OF +VE,-VE & 
negative_count=[]
neutral_count=[]
pos_temp=0
neg_temp =0
neu_temp=0 

#print (news_date_sentiment)   
#print (len(news_date_sentiment['2017-05-23']))


for key in news_date_sentiment:
    for i in range(len(news_date_sentiment[key])):
        if (news_date_sentiment[key][i]=='positive'):
          pos_temp = pos_temp+1
        if (news_date_sentiment[key][i]=='negative'):
          neg_temp = neg_temp+1
        if (news_date_sentiment[key][i]=='neutral'):
          neu_temp = neu_temp+1
        
    positive_count.append(pos_temp)
    negative_count.append(neg_temp)
    neutral_count.append(neu_temp)
    pos_temp=0
    neg_temp =0
    neu_temp=0  
     
#print(positive_count)
#print(negative_count)
#print(neutral_count)
#print(weekday)

weekday_no_repeats = [];                   # THIS PART HELPS US GET THE DAY From the date
temp_day = []
temp_month = []
temp_year = []
temp_weekday = []

for key in news_date_sentiment.keys():
    temp_year.append(int(key[0:4]))
    temp_month.append(int(key[5:7]))
    temp_day.append(int(key[8:10]))
#print(len(temp_day))

DayL = ['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun']
for i in range(len(temp_day)):
    
  a=temp_year[i]
  b=temp_month[i]
  c=temp_day[i]
  temp_weekday.append(DayL[datetime.date(a,b,c).weekday()] + 'day')   
         
#print(len(temp_weekday))

score=[]
                                    #FORMULA FOR SCORE COMES HERE... NEED TO CHANGE IT SOON
for i in range(len(temp_day)):
    temp_score = positive_count[i]-negative_count[i]
    score.append(temp_score)
    
#print(score)

final_score=[]
temp =0
temp1=0

for i in range(len(temp_weekday)):
    if(temp_weekday[i]=='Saturday'):
        temp = score[i]
        score[i+1]=temp+score[i+1]
        score[i] = 100000
        
for i in range(len(temp_weekday)):       
    if(temp_weekday[i]=='Sunday'):
        temp1 = score[i]
        score[i+2]=temp1+score[i+2]
        score[i] = 100000
  



#for key in news_date_sentiment.keys():
#for i in range(len(whole_date)):
#    if (whole_date[i] == '2017-09-01' or '2017-07-04' or '2017-05-29'):
#            score[i]=100000
Date_list= list(news_date_sentiment.keys())    
#print(Date_list)

for i in range(len(Date_list)):
    if (Date_list[i] == '2017-09-01' or Date_list[i] == '2017-07-04' or Date_list[i] == '2017-05-29'):
       
        score[i]=100000
        
def remove_values_from_list(the_list, val):
        while val in the_list:
            the_list.remove(val)

remove_values_from_list(score, 100000)


sentiment_score=[]
for i in score:
    sentiment_score.append([i])
#print(sentiment_score)











import matplotlib.pyplot as plt   
from sklearn import linear_model
from sklearn.model_selection import train_test_split  #here we used cross validation  

# Function to get data  
def get_data(file_name):  
 data = pd.read_csv(file_name)  #here ,use pandas to read cvs file.  
 X_parameters = []  
 #Y_parameters = []  
 for i in data['%change']:  
       X_parameters.append([float(i)])#store in corresponding lists  
       #Y_parameters.append([float(j)])  
 return X_parameters 


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
 print(X_test)
 regr = linear_model.LinearRegression()  
 regr.fit(X_train, Y_train)
 plt.scatter(X_test,Y_test,color='blue',label="test")  
 plt.plot(X_test,regr.predict(X_test),color='red',linewidth=2,label="predict") 
 plt.title("The relationship between sentiment score and next-day stock price change percent")
 plt.xlabel('Sentiment Score')
 plt.ylabel('Next-day stock price change(%)')
 plt.grid(True)
 plt.legend(loc="upper left") 
 plt.xticks([-20,-10,0,10,20,30,40,50,60])  
 plt.yticks= np.linspace(-5, 5, 11) 
 plt.show()
 #R square
 print("Coefficient of determination R-squred is:%.3f" % regr.score(X_test,Y_test))
 plt.figure()  
 plt.plot(range(len(Y_test)),regr.predict(X_test),'r',label="predict")  
 plt.plot(range(len(Y_test)),Y_test,'b',label="test")
 plt.legend(loc="upper left") 
 plt.xlabel("The number of data")  
 plt.ylabel('Next-day stock price change(%)')   


 
 
Y= get_data('6months.csv')
X=sentiment_score
print(X)
#print(Y)
plt.scatter(X,Y,color='orange')
#plt.axis([-20,60,40,60])
#print(X[0][0])
#predictvalue = X[0][0]
result = linear_model_main(X,Y,3)  
print ("Intercept value is: %.3f" % result['intercept'][0])
print ("coefficient is: %.3f" % result['coefficient'][0][0]) 
print ("Predicted percentage change is: %.3f" % result['predicted_value'][0][0]) 


#print ("The acu)
show_linear_line(X,Y)
