#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 23:54:46 2019

@author: shriramgharpure
"""
''' 5-Year Beta Calculation '''
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import math
import numpy as np
emptyList = []
#def q7(I=np.eye(10), N=4):
#    numLooper = np.size(I,0) - N 
#    emptyM = np.zeros((numLooper, numLooper)
#    for i in range(numLooper):
#        for j in range(numLooper):
#            if(i==j):
#                emptyM[i,j] = 1
 #   return emptyM
for i in range(np.size(A,1)): 
    if(i%2==0):
        np.concatenate((B,A[:,i]),axis=0)

    
        

        
'''currentYear = input("Enter the current year for the 5-Year beta calculation.")
ticker1 = input("Enter the ticker of the first stock(all caps)")
currentYear = int(currentYear)
returnPercentages = [];
returnPercentagesSPY = [];
#5-Year Beta Calculation - Relative to SPY
for i in range(currentYear-5,currentYear):
    start = dt.datetime(i,1,1)
    end = dt.datetime(i+1,1,1)
    dfOne = web.DataReader(ticker1,'yahoo',start,end)
    returnOneSt = dfOne['Close'][0]
    returnTwoSt = dfOne['Close'][len(dfOne)-1]
    temp = (returnTwoSt - returnOneSt) / (returnOneSt)
    returnPercentages.append(temp)
    dfTwo = web.DataReader('SPY','yahoo',start,end)
    returnOneSPY = dfTwo['Close'][0]
    returnTwoSPY = dfTwo['Close'][len(dfTwo)-1]
    temp2 = (returnTwoSPY - returnOneSPY) / (returnOneSPY)
    returnPercentagesSPY.append(temp2)
stDevReturns = np.std(returnPercentages)
stDevSPY = np.std(returnPercentagesSPY)
print(stDevSPY)'''


