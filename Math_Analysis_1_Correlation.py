'''
Program Name: Program9_2
Prgram Description: This program reads lines from the mbox-short.txt file and displays days of the week messages were sent.
Programmer: Ray, Stephen
Date: 05/06/2022
Course: CSC233-1L1
'''

import pandas
import numpy as np

#Explain the program to the user
def explainProgram():
    print("This program reads lines from csv files on stock prices and compares the closing prices of two stocks to find any correlation between the two.")

#The mean() function accepts the valuesList as a parameter and returns the list average    
def mean(valuesList):
    listAvg = sum(valuesList) / len(valuesList)
    
    return listAvg

#The standardDeviation() function accepts the valuesList as a parameter and returns the standard deviation
def standardDeviation(valuesList):
    
    listAvg = mean(valuesList)
    variance = sum([((n - listAvg) ** 2) for n in valuesList]) / len(valuesList)
    staDeviation = variance ** 0.5
    
    return staDeviation

#The correlation() function accepts the two lists read from their csv files and finds a correlation number
#Correlation will range from 1 to -1, closer to 1 indicates a postive correlation, closer to 0 indicates no correlation, and closer to -1 indicates a negative correlation
def correlation(xlist, ylist):
    xbar = mean(xlist)
    ybar = mean(ylist)
    xstd = standardDeviation(xlist)
    ystd = standardDeviation(ylist)
    num = 0.0
    
    for i in range(len(xlist)):
        num = num + (xlist[i] - xbar) * (ylist[i] - ybar)
        
    corr = num / ((len(xlist) - 1) * xstd * ystd)
    
    return corr

#The readCSV() function accepts the file name as a parameter and returns a numpy array
def readCSV(fileName):
    fileData = pandas.read_csv(fileName,usecols = ["Close"])
    
    n = np.array(fileData)
    
    result = n.astype(float)
    
    return result
       
#The driver() function executes all the necessary functions and returns the correlation number between two stocks
def driver():
    
    xlist = readCSV('GBTC.csv')
    ylist = readCSV('ADBE.csv')
    
    corr = correlation(xlist, ylist)
    
    return corr

#The displayresults function accepts the standard deviation variable as a paramter and displays the reuslts    
def displayresults(staDeviation):
    print("The correlation of the two stocks is:", staDeviation)

      
#The main function calls all relevant functions and assigns the variable corr to its appropriate returned value
def main():
    explainProgram()
    
    corr = driver()
    displayresults(corr)

    
    
#Call the main() function
main()
