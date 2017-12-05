
class user :

    def __init__(self,name):
        self.name=name
        self.portfolio =portfolio()

    def updatePortfolioShares(share):
        print(1)
        self.portfolio.shares.append(share)

    def updatePortfolioBalance(amount,action):
        print(1)
        if action=='Sub':
            self.portfolio.balance = self.portfolio.balance - amount
        if action=='Add':
            self.portfolio.balance = self.portfolio.balance + amount


class portfolio :
    def __init__(self):
        shares=[]
        balance=0