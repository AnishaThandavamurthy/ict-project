#max value in list 
#numeric values
stock_prices = [ 23 , 55, 62 , 90, 45]

#find max value
print(max(stock_prices))


#character 
stocks = {"anu" , "harshi" , "nisu" , "kav"}
print(max(stocks))

#sorted list 
print(sorted(stocks))
print(sorted(stock_prices))

#sorted and min , max cannot be done in heterogeneous list 

del(stock_prices[4])
print(stock_prices)