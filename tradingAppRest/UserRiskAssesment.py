import numpy as np
import sys


#accountSize = float(input('What is the size of your account?: '))
#accountRisk = input('What is your account risk, please enter as a %: ')
#targetPrice = float(input('What is your target price?: '))
#entryPrice = float(input('Entry Price?: '))
#stopLoss = float(input('What is your stop loss level(price)?: '))

accountSize = str(sys.argv[1])
accountRisk = str(sys.argv[2])
targetPrice = str(sys.argv[3])
entryPrice = str(sys.argv[4])
stopLoss = str(sys.argv[5])

class UserRiskAssesment:
    
    def positionLevels():
        
        profitPerShare = float(targetPrice) - float(entryPrice)
        lossPerShare = float(entryPrice) - float(stopLoss)
        ReturnRiskRatio = profitPerShare/lossPerShare #This number should be atleast 2 for a good trade
        maxLoss = ((float(accountRisk.rstrip('%')))/100) * float(accountSize)
        numShares = int(maxLoss/lossPerShare)
        positionValue = float(entryPrice) * numShares
        maxProfit = np.round((profitPerShare * numShares),2)

        #print('Your maximum loss given your account size and risk, is: $' + str(maxLoss) + '. Given your stop loss and maximum loss potential, you should purchase at max ' + str(numShares) + ' shares. Given your target price, your max profit is: $' + str(maxProfit) + '.')
        #print('Given your stop loss and maximum loss potential, you should purchase at max ' + str(numShares) + ' shares')
        #print('Given your target price, your max profit is: $' + str(maxProfit))
        print(str(maxLoss), " ", str(numShares), " ", str(maxProfit))
        

    #positionLevels()

UserRiskAssesment.positionLevels()