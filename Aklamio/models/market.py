import functools as ft
import itertools as it
import utils
import pandas as pd
import errno
from models import stock

class market(object):

    def __init__(self,name,stocks,users):
        self.name=name
        self.users=users
        self.stocks=[]
        self.tradeValue = 3 #EUR

        # init Stocks - include stockData 
        for s in stocks:
            self.stocks.append(stock.stock(s))
