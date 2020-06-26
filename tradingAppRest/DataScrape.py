import numpy as np
import yfinance as yf
import sys
from datetime import datetime
import time

class TickerDataFrame:
    
    def __init__(self, tSymbol):
        
        self.tickerSymbol = tSymbol
        
        if (str(time.strftime("%I:%M:%S%p"))[8:] == "PM" and int(str(time.strftime("%I:%M:%S"))[0:2]) >= 4) or (str(time.strftime("%I:%M:%S%p"))[8:] == "AM" and int(str(time.strftime("%I:%M:%S"))[0:2]) <= 12):
            
            self.period = '2d'
        else:
            
            self.period = '1d'
            self.start = datetime.today()
        
    def createDataFrame(self):
        
        #symbol = yf.Ticker(self.tickerSymbol)
        #print(str(time.strftime("%I:%M:%S"))[0:2])
        
        if (str(time.strftime("%I:%M:%S%p"))[8:] == "PM" and int(str(time.strftime("%I:%M:%S"))[0:2]) >= 4) or (str(time.strftime("%I:%M:%S%p"))[8:] == "AM" and int(str(time.strftime("%I:%M:%S"))[0:2]) <= 12):
            #below two lines changed to provide pre & post market data
            tickerData = yf.download(tickers = self.tickerSymbol,period = self.period, prepost = True)
            #tickerData = symbol.history(period = self.period)
        else:
            
            tickerData = yf.download(tickers = self.tickerSymbol,start = self.start, prepost = True)
            #tickerData = symbol.history(start = self.start)
        #tickerData = symbol.history(start = self.start, end = self.end)
        return tickerData
    
symbol = sys.argv[1]
#symbol = input("Enter the ticker: ")
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
