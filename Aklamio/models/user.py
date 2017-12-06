
class user :

    def __init__(self,name,):
        self.name=name
        self.portfolio =portfolio()
        self.minimumStocks = 3

    def updatePortfolioShares(share):
        self.portfolio.shares.append(share)

    def updatePortfolioBalance(self,amount,action):
        if action=='Sub':
            self.portfolio.balance = self.portfolio.balance - amount
        if action=='Add':
            self.portfolio.balance = self.portfolio.balance + amount

class portfolio :
    def __init__(self):
        self.shares=[]
        self.balance=0
