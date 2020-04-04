# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:33:34 2020

@author: hcbarnet
"""
#Import the dependencies

import yfinance as yf 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import datetime


#Get Stock Data from Facebook
today = datetime.date.today()
df = yf.download('FB','2018-11-06',today)
print(df.tail())

#Get the adjusted close price
df = df[['Adj Close']]


##Forcast for n days
forcast_out = 5

#Create another column (target) shift -n days
df['Prediction'] = df[['Adj Close']].shift(-forcast_out)

##Create the indepedent data set (X)
##Convert df to a numpy array
X = np.array(df.drop(['Prediction'], 1))

##Remove last n rows
X = X[:-forcast_out]

##print(X)

##Create the dependent dataset y
#Convert the data frame to numpy array all values including NaN
y = np.array(df['Prediction'])
##Get all of the y values except the last n rows
y = y[:-forcast_out]

##print(y)

#Split data into 80% training and 20% testing
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

##Create and train model the Support Vector Algorithm/Machine (Linear Regression)
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf.fit(x_train, y_train)

#Testing Model: Returns coefficient of determination
#Best possible score = 1.0
svm_confidence = svr_rbf.score(x_test, y_test)


#Create and train the Linear Regression model
regression = LinearRegression()
#Train the model
regression.fit(x_train, y_train) 
#Testing Model: Returns coefficient of determination
#Best possible score = 1.0
regression_confidence = regression.score(x_test, y_test)

##Set x_forcast = last 30 rows of original dataset from Adj. Close column
x_forcast = np.array(df.drop(['Prediction'],1))[-forcast_out:]

##Take a look at the predictions for the next n days
svm_prediction = svr_rbf.predict(x_forcast)
print("svm confidence: ", svm_confidence)
print(svm_prediction)


##Take a look at the predictions for the next n days
regression_prediction = regression.predict(x_forcast)
print("Regression confidence: ", regression_confidence)
print(regression_prediction)



