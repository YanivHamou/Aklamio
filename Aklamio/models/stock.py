import functools as ft
import itertools as it
import utils
import pandas as pd
import errno
import datetime


class stock (object):

    def __init__(self,name):
        self.name=name
        self.symbol=name

        #load History data
        stockHistory = stockdata(name)
        self.history= stockHistory.getHistoricalData()


class stockdata:

        def __init__(self,name):
            self.name= name
            self.records = []
            self.n_records = 0


        def add_record(self, rec):
            self.records.append(rec)
            self.n_records += 1

        # Read Data from Csv files based on Company Name
        def getHistoricalData(self):

            df = pd.read_csv(utils.getfullpath(self.name), sep=',')

            # New column represent the change in stock Price
            df['MinimumLoss']=df['Open'].diff()

            #convert to Date Type
            df['Date']=df['Date'].apply(lambda x: utils.convertDate(x,"%m/%d/%Y"))

            #fill None type with zero
            df.fillna(0,inplace=True)

            df.MinimumLoss = df.MinimumLoss.astype(float).fillna(0.0)

            #df.to_csv('f.csv')

            return df


            try:
                print(x)

            except:
                raise KeyError (errno.ENOENT,'Error create History model for Stock :' + name)
                return  self.records



