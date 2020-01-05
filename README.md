# Stock-Market-Prediction
Stock Market Prediction using S&amp;P 500.

Stocks are traded daily, and the price can rise or fall from the beginning of a trading day to the end based on demand.Indexes aggregate the prices of multiple stocks together, and allow you to see how the market as a whole is performing.

The S&P500 Index aggregates the stock prices of 500 large companies. When an index fund goes up or down, you can say that the underlying market or sector it represents is also going up or down.

The dataset contains index prices from 1950 to 2015. Data from 1950 to 2013 will be used to train the model and values from 2013 to 2015 will be predicted.

The columns of the dataset are:

- Date -- The date of the record.
- Open -- The opening price of the day (when trading starts).
- High -- The highest trade price during the day.
- Low -- The lowest trade price during the day.
- Close -- The closing price for the day (when trading is finished).
- Volume -- The number of shares traded.
- Adj Close -- The daily closing price, adjusted retroactively to include any corporate actions.


Error Metric: Mean Absolute Error (MAE)

### Iteration 1:

Indicators used:

1. The average price from the past 5 days.
2. The average price for the past 30 days.
3. The average price for the past 365 days.


Algorithm used: Linear Regression

Error: 16.1422

### Iteration 2:









