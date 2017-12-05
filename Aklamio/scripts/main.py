import functools as ft
from  models import market, user , stock
import utils
import pandas as pd
import datetime
import numpy as np
from datetime import date, datetime, timedelta



def bestDays(values):
    # If array has two entries, then only one trade possible, so return it
    if len(values) == 2:
        return [[0, 1]]
    # If array has one or zero entries, no trades possible, return empty list
    elif len(values) == 1 or not values:
        return []

    trades = []  # List of trades
    share = 0  # Flag to indicate whether share currently held

    # Step through array. Logical tests explained in doc string
    for i in  range(len(values) - 1):

        if not share:  # Share not held
            if values[i + 1] > values[i]:  # Increasing tomorrow
                trades.append([i])  # Buy and add new trade
                share = 1

        else:  # Share held
            if values[i + 1] < values[i]:  # Decreasing tomorrow
                trades[len(trades) - 1].append(i)  # Add sell day to existing trade
                share = 0

    # If share held on the last day, sell
    if share:
        trades[len(trades) - 1].append(len(values) - 1)

    elif not trades:  # No share held, no trades made, the result of decreasing array
        # Find day with minimum loss:
        buy = min(range(len(values) - 1), key=lambda i: values[i] - values[i + 1])
        return [[buy, buy + 1]]  # Sell on next day

    return trades

val=[117,116,115]
#bestDays(val)

def goodTrades(stock):

    trades = []  # List of trades
    share = 0  #  boolean indicate share holder /not share holder
    trades_x=[]
    for i in  range(len(stock.history) - 1):

        if not share:  # Share not held
            if stock.history.loc[i + 1]['Open'] > stock.history.loc[i]['Open']:  # Increasing tomorrow
                #trades.append(stock.history.loc[i])
                trades.append([i])  # Buy and add new trade
                trades_x.append([stock.history.loc[i]['Date'],stock.history.loc[i]['Open'],'BUY',stock.name])
                share = 1

        else:  # Share held
            if stock.history.loc[i + 1]['Open'] < stock.history.loc[i]['Open']:  # Decreasing tomorrow
                trades[len(trades) - 1].append(i)  # Add sell day to existing trade
                #trades[len(trades) - 1].append(stock.history.loc[i])
                trades_x.append([stock.history.loc[i]['Date'],stock.history.loc[i]['Open'],'SELL',stock.name])
                share = 0

    # df_trades= pd.DataFrame(trades,columns=['Buy_index','Sell_index'])
    # print(df_trades.head(5))

    df_trades= pd.DataFrame(trades_x,columns=['Date','Price','Action','Stock'])
    print(df_trades.head(5))


#Companies In Stock Market
companies= ['ADS.DE' , 'BMW.DE' , 'SAP.DE','VOW3.DE','CBK.DE']

# init User
user = user.user('ABELARD')
user.updatePortfolioBalance(10000,'Add')

# init Stock market
mrk= market.market(companiesInMarket,users)


for s in mrk.stocks:
    print (s.name)
    # Find day with minimum loss:
    goodTrades(s)

# set start and the end of the trading cycle
tradingCycle=utils.dateRange('2016-12-5','2017-12-5')
print (dates)



#print (a)
#tool that finds the optimal (or nearly optimal)
#order of trades to maximize the value of your portfolio

#speficif date  open  day after open  owen
# 1.1.2017      5     2.1.2017  6      Y   - sell
# 1.4.2017      6     5.1.2017  5      N   - buy


# no stocks - find the minimum lose - buy there




""" Intermediate challenge:
" Basic method: buy low, sell high.  Loop through array. On a given day:
" - If the value decreases tomorrow:
"   - if you currently hold a share, sell sell sell!
"   - if you don't, wait to buy
" - If the value increases tomorrow:
"   - if you don't hold a share, buy buy buy!
"   - if you do, wait to sell
" - On any day, if the value stays the same tomorrow, do nothing
" - At end, if no trades made, array must be decreasing
" - Therefore find minimal loss and make that trade.
" All this is accomplished through a simple day-to-day comparison, and an ownership flag.
"""




