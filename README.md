# Impact of Recession on Retail Sector

# Business Objective

* Predict who is likely to shop next month. Highlight factors that impact likelihood of customer shopping next month. 

* For each customer shopped during 12/1/2010 till 11/9/2011, you must predict the likelihood of customer shopping next month

![image](https://user-images.githubusercontent.com/71720761/113479584-8796eb80-94ad-11eb-84da-c5dc751d4134.png)

![image](https://user-images.githubusercontent.com/71720761/113479604-a5fce700-94ad-11eb-9148-1358e209834c.png)

Many investors around the world decided that they wanted to invest in US home mortgages to earn higher interest rates and mortgages  were considered pretty safe.
Banks pushed their customers to buy more property with mortgages. Home prices soared, because people who could never afford to pay off those mortgages got the loans; the banks expected home prices to increase forever.
But, house prices stopped rising, mortgage holders could not pay the mortgage or sell the homes
A small number of smart and brave people knew that many mortgage holders would default and that the bonds backed by those mortgages would become worthless. So they sold those mortgage-backed bonds short(selling it without owning it) and the short sellers made a bundle.

![image](https://user-images.githubusercontent.com/71720761/113479610-b2813f80-94ad-11eb-9c08-e24d704c3294.png)

![image](https://user-images.githubusercontent.com/71720761/113479613-b7de8a00-94ad-11eb-9d38-82934c391c5f.png)

![image](https://user-images.githubusercontent.com/71720761/113479616-bca33e00-94ad-11eb-9c04-7091f3bab117.png)

The Big Short is a 2015 American biographical comedy-drama film 
Plot
The film consists of three separate but concurrent stories, loosely connected by their actions in the years leading up to the 2007 housing market crash.

# UK recession: winners and losers

![image](https://user-images.githubusercontent.com/71720761/113479634-dd6b9380-94ad-11eb-835e-5503a158f812.png)

***BANKS

Investment banks are judged to have been one of the main causes of the recession

RETAIL

Thousands of shops were closed and household names disappeared. Sectors such as furniture and homewares perished as consumers deferred big purchases. supermarkets and value chains gathered momentum as consumers traded down.

TRANSPORT

Transport companies have been among the biggest losers

MANUFACTURING

What is left of UK manufacturing suffered several blows as banks stopped lending

PROPERTY

The boom in commercial and residential property prices came to an abrupt halt with house prices down 20% year-on-year. the market took an unexpected turn as the year progressed with prices pushed up as buyers fought over a small number of properties. 

ENERGY

The oil price has stayed higher than in previous downturns and cushioned the oil companies

FUN

The economic gloom put mass escapism on the menu with the buzz around James Cameron's sci-fi move Avatar, as well as blockbuster films such as Harry Potter and the Half-Blood Prince and Star Trek, putting the UK's box offices on track for record takings of £1bn in 2009.***

# Dataset details

![image](https://user-images.githubusercontent.com/71720761/113479726-4b17bf80-94ae-11eb-8150-fff0ccac8b07.png)

![image](https://user-images.githubusercontent.com/71720761/113479731-523ecd80-94ae-11eb-8640-2dd6477fd02d.png)

* Data Type

![image](https://user-images.githubusercontent.com/71720761/113479737-58cd4500-94ae-11eb-8a2b-75ef511ad3a7.png)

* Unique Values

![image](https://user-images.githubusercontent.com/71720761/113479849-ec9f1100-94ae-11eb-8690-aed165b75c77.png)

* Null Values

![image](https://user-images.githubusercontent.com/71720761/113479856-f3c61f00-94ae-11eb-9d15-da974258fa17.png)

* Summary

![image](https://user-images.githubusercontent.com/71720761/113479859-f7f23c80-94ae-11eb-93f5-3143efb3fa74.png)

* Missing Values

Customer ID = 0.2493 ~ 24.93%

Description  = 0.0027 ~ 00.27%

# Dataset details after cleaning

![image](https://user-images.githubusercontent.com/71720761/113479930-4ef81180-94af-11eb-8f27-b21b810e7cea.png)

# EDA

* Histogram of InvoiceDate

![image](https://user-images.githubusercontent.com/71720761/113479947-659e6880-94af-11eb-930e-d8e6a637c633.png)

* The Number of orders from each of the Countries

![image](https://user-images.githubusercontent.com/71720761/113479961-7d75ec80-94af-11eb-95f1-3cd792cb4050.png)

* The number of purchases (in the top50 largest baskets)

![image](https://user-images.githubusercontent.com/71720761/113479981-99798e00-94af-11eb-863a-5104a0969f6b.png)

* The total amount spend per country

![image](https://user-images.githubusercontent.com/71720761/113480244-02153a80-94b1-11eb-9ecc-57e8514830e9.png)

* The no. of customers in each month

![image](https://user-images.githubusercontent.com/71720761/113480262-122d1a00-94b1-11eb-9999-622f99d59efe.png)

# RFM (recency, frequency, monetary) 

* A marketing technique 

* used to determine quantitatively which customers are the best ones by examining how recently a customer has purchased (recency),

* how often they purchase (frequency), and 

* how much the customer spends (monetary)

For this project, we have selected our feature candidates like below:	

- RFM scores & clusters

- Days between the last three purchases

- Mean & standard deviation of the
			  
- difference 	between purchases in days

# The new data frame

![image](https://user-images.githubusercontent.com/71720761/113480388-9da6ab00-94b1-11eb-8c13-b40cba91a422.png)

![image](https://user-images.githubusercontent.com/71720761/113480394-a13a3200-94b1-11eb-8dc8-3e255610ef86.png)

# Recency, frequency & monetary

![image](https://user-images.githubusercontent.com/71720761/113480409-b0b97b00-94b1-11eb-9cee-e09464c25a1b.png)

![image](https://user-images.githubusercontent.com/71720761/113480411-b4e59880-94b1-11eb-8c8b-75f600a5fc12.png)

![image](https://user-images.githubusercontent.com/71720761/113480412-b7e08900-94b1-11eb-92aa-ff0fade879d6.png)

![image](https://user-images.githubusercontent.com/71720761/113480418-c038c400-94b1-11eb-8cf9-385eddf6801b.png)

![image](https://user-images.githubusercontent.com/71720761/113480422-c3cc4b00-94b1-11eb-854a-79b7174bce83.png)

![image](https://user-images.githubusercontent.com/71720761/113480424-c6c73b80-94b1-11eb-9859-fd5366de421f.png)

![image](https://user-images.githubusercontent.com/71720761/113480431-caf35900-94b1-11eb-925b-d84eb1e9aaa2.png)

# Model Building

![image](https://user-images.githubusercontent.com/71720761/113480448-de062900-94b1-11eb-8598-9fd344e45f51.png)

![image](https://user-images.githubusercontent.com/71720761/113480451-e3fc0a00-94b1-11eb-8d15-ca674e09b79c.png)

# DEPLOYMENT

![image](https://user-images.githubusercontent.com/71720761/113480466-f9713400-94b1-11eb-8c58-a69356d2f1ca.png)

![image](https://user-images.githubusercontent.com/71720761/113480468-fd04bb00-94b1-11eb-9e17-3a50ce0e0ec7.png)

![image](https://user-images.githubusercontent.com/71720761/113480473-02620580-94b2-11eb-8b2f-8e7b62f86d6f.png)

![image](https://user-images.githubusercontent.com/71720761/113480480-0857e680-94b2-11eb-968c-f4967c8a56ec.png)

![image](https://user-images.githubusercontent.com/71720761/113480487-0db53100-94b2-11eb-8993-5ee1bf5ab030.png)

![image](https://user-images.githubusercontent.com/71720761/113480491-1279e500-94b2-11eb-9d7b-5df304ce382e.png)

![image](https://user-images.githubusercontent.com/71720761/113480499-1d347a00-94b2-11eb-8c4b-3210f108a098.png)

