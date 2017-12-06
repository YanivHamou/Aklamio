# Aklamio
Home Task - Data engineer @Aklamio

Task: Build a simple stock trading tool in python:

Download Historical Stock data for some DAX-components (at least 5 different) for the years 2015 and 2016 from yahoo finance.
Link to DAX - https://finance.yahoo.com/quote/%5EGDAXI?p=^GDAXI

Download the files manually and just read the downloaded files with the program. 

Assume that you have 10.000 EUR available. 
  Build a tool that finds the optimal (or nearly optimal) order of trades to maximize the value of your portfolio (collection of stocks + cash).

Your program should meet the following requirements
- You have no stocks in your portfolio at the start and the end of the trading cycle.
- At any other moment you have at least stocks of three types (e.g. 100x RWE.DE, 200xSAP.DE 30xSIE.DE).
  This means, on the first day you buy at least 3 stocks, on the last day you sell all your stocks.
- Your cash can never fall below 0.
- Every trade (buy/sell) costs 3 EUR (e.g. buying 100x LHA.DE for 2,30 EUR costs 100x 2,30 + 3 = 233 EUR, selling it costs another 3 EUR)
- Don't build a prediction system. We don't care for the future in this task. You know all historical courses. Just go through them and see what would have been good trades.
- Only use end-of-day courses. Ignore the rest (min, max, ...)

Description:
The DAX is a blue chip stock market 
index consisting of the 30 major German companies trading on the Frankfurt Stock Exchange

Project Structure:
	Data	- Hold Csv files - one Year History
	Models	- Hold Models for rpresent the Stock market 
			 - stock
			 - stockData
				suggestTradesPaths()
				getHistoricalData()
				add_record()
			 - user
				updatePortfolioShares()
				updatePortfolioBalance()
			 - portfolio
			 - market
	scripts  -utils - holds  utils function
			 -main - main script - execute all the logic

Missing :
Create unit testing
Apply error handling

	