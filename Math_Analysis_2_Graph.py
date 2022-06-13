'''
Program Name: graphStock.py
Prgram Description: This program reads lines from a csv file on stock prices and graphs the information within a specific date range.
Programmer: Ray, Stephen
Date: 05/06/2022
Course: CSC233-1L1
'''

import pandas
import numpy as np
import turtle


#Explain the program to the user
def explainProgram():
    print("This program reads lines from a csv file on stock prices and graphs the information within a specific date range.")
    

#readCSVGraph() function accepts begin date, end date, file name, and stock ticker as arguments
#The function finds the 
def readCSVGraph(bDate, eDate, fileName, ticker):
    
    #Read the Date column of the csv file    
    fileDateData = pandas.read_csv(fileName, usecols = ["Date"])
    
    #Get the index of the row we want to begin at with begin Date
    allDateData = np.array(fileDateData)
    startDate = np.where(allDateData == bDate)
    sD = (startDate[0])
    superTuper = sD.astype(int)
    superList = superTuper.tolist()
    
    #Convert the index position to an integer
    impInfo1 = superList[0]
    
    #Get the index of the row we want to end at with end date
    endDate = np.where(allDateData == eDate)
    eD = (endDate[0])
    superTuper2 = eD.astype(int)
    superList2 = superTuper2.tolist()
    
    #Convert the index position to an integer
    impInfo2 = superList2[0]
            
    #Read the Close price column of the csv file
    fileData = pandas.read_csv(fileName, usecols=(["Close"]))            
    n = np.array(fileData)
    
    #Typecast array to float data type    
    result = n.astype(float)
    
    #Convert array to list
    listResult = result.tolist()
    
    #Select specific range of the list using the indices of interest from the begin dates and end dates
    
    #***********************************************************************************************************
    #The resulting interestList contains all of the closing stock prices from the date range we have selected
    #***********************************************************************************************************
    interestList = listResult[impInfo1:impInfo2 + 1]
    
    print("The prices of the stock", ticker, "in the date range", bDate, "to", eDate, "are:", interestList)
    
    wn = turtle.Screen()
    chartT = turtle.Turtle()
    wn.setworldcoordinates(-1, -1, 7, 55)
    chartT.hideturtle()
    turtle.title("Stock Price Graph")
    # chartT.width(width=5)  using default width
    # chartT.shape(name='turtle') a cute turtle!

    chartT.up()         # pick up the pen
    chartT.goto(0,0)    # move the pen to this location
    chartT.down()       # put the pen on the drawing surface
    chartT.goto(15, 0)   # draw over to this location
    chartT.up()         # pick up the pen

    #Set up axis labels
    chartT.goto(-1,0)   # move the pen to the bottom left margin of the graph
    chartT.write("$ 0", font=("Helvetica",16,"bold")) # write 0 to the left of the y axis
    chartT.goto(-1,50)   # move the pen to the highest point of the left margin
    chartT.write("$50", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis
    chartT.goto(-1,40)   # move the pen to the highest point of the left margin
    chartT.write("$40", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis
    chartT.goto(-1,30)   # move the pen to the highest point of the left margin
    chartT.write("$30", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis
    chartT.goto(-1,20)   # move the pen to the highest point of the left margin
    chartT.write("$20", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis
    chartT.goto(-1,10)   # move the pen to the highest point of the left margin
    chartT.write("$10", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis
    chartT.goto(-3,25)   # move the pen to the highest point of the left margin
    chartT.write("Stock Price", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis
    chartT.goto(-3,30)   # move the pen to the highest point of the left margin
    chartT.write(ticker, font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis
    chartT.goto(1,-2)
    chartT.write("1", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis
    chartT.goto(3,-2)
    chartT.write("2", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis
    chartT.goto(5,-2)
    chartT.write("3", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis
    chartT.goto(7,-2)
    chartT.write("4", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis
    chartT.goto(3,-4)
    chartT.write("Time", font=("Helvetica", 16, "bold"))# write 5 to the left of the y axis

    # now iterate through the list and graph it
    for index in range(len(interestList)):
        chartT.goto(index, -1)
        chartT.write(str(interestList[index][0]), font=("Helvetica",16,"bold"))

        chartT.goto(index,0)
        chartT.down()
        chartT.goto(index, interestList[index][0])
        chartT.up()
    wn.exitonclick()    
        
#driver() function calls the readCSVGraph() function and passes relevant parameters
def driver():
    
    #Pass relevant parameters to the readCSVGraph: Begin Date, End Date, Stock File, and ticker symbol
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Note that there are some dates that are not recorded in the 6 month date range of the stock csv file
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!     
    readCSVGraph('2022-04-01', '2022-04-11', 'GBTC.csv', 'GBTC')
                 
#The main function calls all relevant functions and assigns variables userFile and weekDictionary to their appropriate returned values
def main():
    explainProgram()
    driver()  
       
#Call the main() function
main()


