###Objective

Acquisition of exchange data using Oanda api and formatting to pandas.Dataframe

##Arguments

####token: *string*

​		your access token of oanda account

####instruments: *list*

​		List of training pairs. For instance, *["EUR_USD", "GBP_JPY"]*

####granularity: *string*

​		Data acquisition interval.  For instance,  *"H1", "H2", "H4"* each stands for data at 1, 2 , 4 hour intervals

####start_day, end_day:  *datetime.datetime(year, month, day)*

​		the bigining and the end of the data

#### candle:  *'str'*

​		price of transaction 

​		Any of *'o','h', 'l', 'c'*  (open price, high price , low(bottom) price, closing price)





