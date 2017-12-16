# EC601-Project : Stock Predictor Based on News Sentiment and Past Trend of Stock
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
### Poster:
![image](https://github.com/jiahaozh/EC601-Project/raw/master/poster.png)
### Test:
This is autotest from https://monkeytest.it/test/d30533c9-d051-4664-bb93-546500132577
![image](https://github.com/jiahaozh/EC601-Project/raw/master/TEST/monkeytest1.png)
![image](https://github.com/jiahaozh/EC601-Project/raw/master/TEST/monkeytest2.png)
![image](https://github.com/jiahaozh/EC601-Project/raw/master/TEST/monkeytest3.png)
This is autotest from http://www.webpagetest.org/result/171215_RG_ca0cbadba7137b7eb608ca968baaae52/
![image](https://github.com/jiahaozh/EC601-Project/raw/master/TEST/webpagetest1.png)
![image](https://github.com/jiahaozh/EC601-Project/raw/master/TEST/webpagetest2.png)
![image](https://github.com/jiahaozh/EC601-Project/raw/master/TEST/webpagetest3.png)
![image](https://github.com/jiahaozh/EC601-Project/raw/master/TEST/webpagetest4.png)
![image](https://github.com/jiahaozh/EC601-Project/raw/master/TEST/webpagetest5.png)
And the test document is Test_Case_WebUI document.
















