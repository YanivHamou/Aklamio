import functools as ft
import itertools as it
import utils
import pandas as pd
import errno
import datetime


class stock :

    def __init__(self,name):
        self.name=name
        self.symbol=name

        #load History data
        stockData = stockdata(name)
        self.history= stockData.getHistoricalData()

        #build trades recommendation based on history
        self.bestTrades= stockData.suggestTradesPaths(self.history,self.name)

class stockdata:

        def __init__(self,name):
            self.name= name
            self.records = []
            self.n_records = 0


        def add_record(self, rec):
            self.records.append(rec)
            self.n_records += 1

        # ///////////////////////////////////////////////////////////////////////////////////
        #  @brief    Based on Company Name - Read Data from Csv files.
        #  @details  have 3 parts:
        #               Read Csv
        #               Calculate MinimumLoss
        #               Convert date field to DateTime Object
        # //////////////////////////////////////////////////////////////////////////////
        def getHistoricalData(self):

            try:
                df = pd.read_csv(utils.getfullpath(self.name), sep=',')
            except:
                raise KeyError (errno.ENOENT,'Error : create History model for Stock : read CSV :' + name)

            # New column represent the change in stock Price
            df['MinimumLoss']=df['Open'].diff()
            df.MinimumLoss = df.MinimumLoss.astype(float).fillna(0.0)

            #convert to Date Type
            df['Date']=df['Date'].apply(lambda x: utils.convertDate(x,"%Y-%m-%d"))

            #df.to_csv('f.csv')
            return df


        # ///////////////////////////////////////////////////////////////////////////////////
        #  @brief    Based on Company data - Build recommendation trades.
        #            Finds the optimal (or nearly optimal) order of trades to maximize profit
        #            All this is accomplished through a simple day-to-day comparison
        #  @details  Loop throw all The history:
        #               If price decreases tomorrow:
        #                   - if you suggest buy a share, sell.
        #                   - if you don't, wait to buy
        #                If price increases tomorrow:
        #                   - if you suggest buy a share, buy.
        #                   - if you do, wait to sell
        #  @parameters :
        #             stockHistory  - stock History data
        #             name          - stock name
        # //////////////////////////////////////////////////////////////////////////////
        def suggestTradesPaths(self,stockHistory,name):

            trades = []  # List of trades
            share = 0  # boolean
            trades_x = []

            for i in range(len(stockHistory) - 1):

                if not share:  # Share not held
                    if stockHistory.loc[i + 1]['Open'] > stockHistory.loc[i]['Open']:  # Increasing tomorrow
                        trades.append([i])  # Buy and add new trade
                        trades_x.append([stockHistory.loc[i]['Date'], stockHistory.loc[i]['Open'], 'BUY', name])
                        share = 1

                else:  # Share held
                    if stockHistory.loc[i + 1]['Open'] < stockHistory.loc[i]['Open']:  # Decreasing tomorrow
                        trades[len(trades) - 1].append(i)  # Add sell day to existing trade
                        trades_x.append(
                            [stockHistory.loc[i]['Date'], stockHistory.loc[i]['Open'], 'SELL', name])
                        share = 0

            df_trades = pd.DataFrame(trades_x, columns=['Date', 'Price', 'Action', 'Stock'])
            return df_trades
