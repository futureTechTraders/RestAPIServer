import numpy as np
import yfinance as yf
import sys
from datetime import datetime
import time

class TickerDataFrame:
    
    def __init__(self, tSymbol):
        
        self.tickerSymbol = tSymbol
        
        if int(str(time.strftime("%I:%M:%S"))[0:2]) >= 4 and int(str(time.strftime("%I:%M:%S"))[0:2]) <= 9:
            
            self.period = '2d'
        else:
            
            self.period = '1d'
            self.start = datetime.today()
    
        self.end = self.start
        
    def createDataFrame(self):
        
        symbol = yf.Ticker(self.tickerSymbol)
        #print(str(time.strftime("%I:%M:%S"))[0:2])
        
        if int(str(time.strftime("%I:%M:%S"))[0:2]) >= 4 and int(str(time.strftime("%I:%M:%S"))[0:2]) <= 9:
            
            tickerData = symbol.history(period = self.period)
        else:
            
            tickerData = symbol.history(peroid = self.period, start = self.start)
        
        #tickerData = symbol.history(start = self.start, end = self.end)
        return tickerData
    
#symbol = sys.argv[1]
symbol = input("Enter the ticker: ")
data = TickerDataFrame(symbol)
dataFrame = data.createDataFrame()

print(dataFrame['Close'])
print("@")
print(dataFrame['Open'])
print("@")
print(dataFrame['Low'])
print("@")
print(dataFrame['High'])
print("@")
print(dataFrame['Volume'])
