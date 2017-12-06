import functools as ft
from  models import market, user , stock
import utils
import pandas as pd
import datetime
import numpy as np
from datetime import date, datetime, timedelta


# specify Companies In Stock Market
companies= ['ADS.DE' , 'BMW.DE' , 'SAP.DE','VOW3.DE','CBK.DE']

########### Users - Start
users= []
# initialize  1 User  named ABELARD with 10000 Euro
user = user.user('ABELARD')
user.updatePortfolioBalance(10000,'Add')

# Add to array of users
users.append(user)
############ Users - End


# Set trade cycle : start - end Dates.
tradingCycle=utils.dateRange('2016-12-5','2016-12-20')



# initialize Stock market
# @parameters :
# Name      - stock market name
# Users     - list of users
# companies - list of companies names
#             based on company name - loads history data
#             based on company name & stock data history build trades recommendation
stockMarket= market.market('DAX',companies,users)


for s in stockMarket.stocks:
   print (s.bestTrades)
# Print Example :
#    Date         Price   Action   Stock
#0   2016-12-05   6.500    BUY     CBK.DE
#1   2016-12-13   7.740   SELL     CBK.DE


# Main Loop - Represent the Trading
# Loop throw trading days
# Per Each Day
#   Per each Company
#     check what action required BUY/SELL
#     Pre execute Action
#       Buy  - Calculate price for 10 shares
#            - check user balance
#            - Update user shares
#            - Update user balance
#       Sell - Calculate price for 10 shares
#            - Update user shares
#            - Update user balance
for day in tradingCycle:
     for stck in stockMarket.stocks:
         # get only rows with data
         if (len(stck.bestTrades[(stck.bestTrades['Date'] == day)]>0)) :
             #convert to single row
             row= stck.bestTrades[(stck.bestTrades['Date'] == day)]
             if row['Action'].item()=='BUY':
                 #calculate 10 shares value
                 amount=(row['Price'].item() * 10) + stockMarket.tradeValue
                 if (amount<user.portfolio.balance):
                 #check if user have money to buy
                    user.portfolio.balance = user.portfolio.balance- amount
                    user.portfolio.shares.append(row)
             if row['Action'].item() == 'SELL':
                 # check user not have at least 4 stocks - cant go lower then 3
                 if (len(user.portfolio.shares)>3):
                     # calculate 10 shares
                     amount = (row['Price'].item() * 10) + stockMarket.tradeValue
                     user.portfolio.balance = user.portfolio.balance + amount

                     for i in range(len(user.portfolio.shares) - 1):
                         if (user.portfolio.shares[i]['Stock'].item()==row['Stock'].item()):
                            user.portfolio.shares.pop(i)
                         break












