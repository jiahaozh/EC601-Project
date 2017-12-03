#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:04:18 2017

@author: abhivora
@author: fengjun li
"""

import pandas as pd
import datetime

 

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



print(score)

sentiment_score=[]
for i in score:
    sentiment_score.append([i])
print(sentiment_score)

#output CSV file
df = pd.DataFrame(score)
df.columns = ['score']
#df.index = ['seq1']
df.to_csv("firstone.csv", )


 
    
       
    
    
       
            
    
    
        
        
        
        
    




         
            
            
        
    


 
  


   
