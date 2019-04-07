#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 17:48:58 2018

@author: shriramgharpure
"""
#df = web.DataReader('GOOG','yahoo', start, end)
#df.to_csv('goog.csv')
#Look at pandas documentation to further clean the data, parse_dates and index_col necessary to parse the stock data
#df = pd.read_csv('goog.csv', parse_dates = True, index_col = 1)
#df.plot() plots all the columns (w/labels) onto one graph 
#df['(name of column)'].plot() - plots the column data onto one graph
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import math
import numpy as np
print(math.floor(2.8))
print(math.ceil(2.8))
'''
#Cross-Correlation Measurement between two stocks
print('Make sure to check that your dates are valid(ex: both companies are public at BOTH dates)')
yrBegin = input("Beginning year of cross-correlation measurement")
monthBegin = input("Beginning month of cross-correlation measurement(1 - January, 12 - December)")
dateBegin = input("Beginning date of cross-correlation measurement(1 to 31)")
yrEnd = input("End Year of cross-correlation measurement")
monthEnd = input("End month of cross-correlation measurement")
dateEnd = input("End date of cross-correlation measurement")
ticker1 = input("Enter the ticker of the first stock(all caps)")
ticker2 = input("Enter the ticker of the second stock(all caps)")
yrBegin = int(yrBegin)
monthBegin = int(monthBegin)
dateBegin = int(dateBegin)
yrEnd = int(yrEnd)
monthEnd = int(monthEnd)
dateEnd = int(dateEnd)
#(error handle if time permits)

    #Getting relevant dates and creating dataframe
start = dt.datetime(yrBegin,monthBegin,dateBegin)
end = dt.datetime(yrEnd,monthEnd,dateEnd)
dfOne = web.DataReader(ticker1,'yahoo',start,end)
#Reversing order of dates, easier to calculate ln(prevAdj/curAdj) ratio
dfOne = dfOne[::-1]
dfTwo = web.DataReader(ticker2,'yahoo',start,end)
dfTwo  = dfTwo[::-1]
adjCloseOne = dfOne['Adj Close']
adjCloseTwo = dfTwo['Adj Close']
#Generating the Periodic Returns List 
periodicReturnsOne = []
periodicReturnsTwo = []
for i in range(len(adjCloseOne)):
    if i != len(adjCloseOne)-1:
        temp = -1 * math.log(adjCloseOne[i] / adjCloseOne[i+1])
        periodicReturnsOne.append(temp)
for j in range(len(adjCloseTwo)):
    if j != len(adjCloseTwo)-1:
        temp = -1 * math.log(adjCloseTwo[j] / adjCloseTwo[j+1])
        periodicReturnsTwo.append(temp)
corrCoef = np.corrcoef(periodicReturnsOne, periodicReturnsTwo)
corrCoef = corrCoef.item((0,1))
corrCoef = round(corrCoef, 4)
print(corrCoef)
    '''
        
        
    
    
        


