import functools as ft
import itertools as it
import utils
import pandas as pd
import errno

from models import stock

class market(object):

    def __init__(self,name,users):
        #self.name=name
        self.users=''
        self.stocks=[]

        #initialized stocks available for Trade
        # include Past Data
        for stockName in name:
            self.stocks.append(stock.stock(stockName))

