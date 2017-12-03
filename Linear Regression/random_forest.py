#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:29:43 2017

@author: abhivora
"""
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import random
import numpy as np

import pandas as pd

df = pd.read_csv('nike.csv', usecols=['close', 'open', 'high', 'low','DJI','GSPC','IXIC','score'])

validate_df = pd.read_csv('Validate.csv', usecols=['open', 'high', 'low','score', 'close','DJI','GSPC','IXIC'])
validate_x = validate_df[['open', 'high', 'low','score','DJI','GSPC','IXIC']]
validate_y = validate_df['close']

train_x, test_x, train_y, test_y = train_test_split(df[['open', 'high', 'low','score','DJI','GSPC','IXIC']], df['close'], train_size=0.75)

clf = RandomForestRegressor()
clf.fit(train_x, train_y)

predictions = clf.predict(validate_df[['open', 'high', 'low','score','DJI','GSPC','IXIC']])

#print("Train Accuracy :: ", accuracy_score(train_y, clf.predict(train_x)))
#print("Test Accuracy  :: ", accuracy_score(test_y, predictions))
#print("Confusion matrix ", confusion_matrix(test_y, predictions))

print(predictions)
print(validate_y)

print(clf.score(train_x, train_y))
print(clf.score(test_x, test_y))
print(clf.score(validate_x, validate_y))


predicted_values = clf.predict(validate_x)
validate_df['predicted_close'] = predicted_values
validate_df.to_csv('Output.csv', index=False)
