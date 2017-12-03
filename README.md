# EC601-Project
**_Team Member: Jiahao Zhang, Fengjun Li, Hongtao Zhao, Abhi Vora_** <br> 
---
In this project, our purpose is to establish a individual stock management system. Its main function is to predict next-day stock price based on today's New's Articles.  <br>This is our website: https://hongtaoz.wixsite.com/stock .
### Target Groups:
- Individuals 
- Investment Companies
### User Stories:
- Users may want to know next-day stock price of some specific companies.
- Users may check the past stock price trend of some specific companies.
- Users may want to get some stock suggestions.
### Minimum Valuable Product:
- PREDICT the NEXT-DAY STOCK PRICE AS ACCURATE AS POSSIBLE.
### Tools:
- Programming Language: Python, Html, PHP
- API: AYLIEN API to extract news sentiments.
- Database: MYSQL
### Algorithms:
Linear Regression model is the first machine learning model we used to train the dataset, and we used two features (daily news sentiment score and past daily close stock price percentage changes).However, the relationship is weak so that it cannot reflect the stock price trend well. To modify that, we changed to Random Forest Regression model and  we added more features (high price, low price, open price, Dow Jones index, S&P 500 index and NASDAQ index). Fortunately, it showed a much better relationship.






