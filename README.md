# NLP-Twitter-Sentiment-Analysis
# Using Machine Learning Methods to Assess the Imapact of Twitter Sentiment on a Company's Stock Prices
# Group Members: 
 Sarah: Project Manager
 Arturo: Facilitator
 Pipi: Task Manager
 
# Abstract
Our project goal is to understand to what extent Twitter can reflect a company’s value. We wanted to examine the value of a company from two approaches. One way was to examine how the influential figures of each company, such as the CEOs, utilize Twitter space to promote values of a company. Our finding was that not all CEO use Twitter space to promote their brand values. Second approach was to look at the stock value of a company. We were curious to see to what extent the public sentiment of a company is reflected on Twitter, and how these sentiments may or may not influence the companies' stock prices. We concluded that Twitter sentiments alone cannot capture or influence the rise or the fall of company stock prices. However, we were able to conclude that the Twitter volume is a significant predictor of stock price rise or fall.

# Introduction
The importance of numerous social media platforms has risen over the past years. As more people spend time online, the more information about people’s preferences, dislikes, societal trends, and opinions have been collected in these platforms in real time. There are numerous social media platforms, such as Twitter, Facebook, Reddit, Youtube etc, that allow people to openly share their opinions and values. We chose Twitter as our main social media platform to gain insights about real-time information regarding current societal trends and opinions about companies. As of 2021, Twitter has 396.5 million users among which 206 million users access Twitter daily. Twitter is a rich source of real-time information regarding current trends and opinions. Our project will provide relavant insights to whether Twitter sentiment can bring light to the stock market trend. 

The motivating question for our project was “to what extent does Twitter capture the value of a company?” Our goal was to analyze social media data about different companies and predict its future stock trend using sentiment analysis and machine learning methods. We were interested to see how influential figures like CEO's utilizes Twitter space to promote company values. We also wanted to examine to what extent Twitter sentiments influence the stock market trend for these companies. We examined this problem in three parts:

First, we will be looking at the Twitter contents and comments for several companies of our choice, such as Apple, Microsoft, Amc, Amazon, and Twitter. Looking into each CEO’s Twitter posts and their comments, we will be building Wordclouds to visualize the most frequently used words on their Twitter spaces in order to gauge to what extent these influential figures utilize the Twitter space to promote values of their company. 

Second, we will conduct sentiment analysis on the public’s discussions of the hashtags for each companies’ stock code from the CEO’s Twitter posts. We are curious to see whether the Twitter sentiment on these posts and hashtags reflect the change in stock market prices for these companies. Our hypothesis is that Twitter is a pivotal factor in influencing and shaping perceptions; therefore, Twitter sentiment will affect stock market trends. 

Finally, we looked at two different datasets to verify our hypothesis. (More information about our data will be explained in the next section "Data"). Due to the limitation of the Twitter API, we were only able to look at the change in Twitter sentiment and stock prices for only a week. One week is too short to generalize the validity of our hypothesis for all time; therefore, we also looked at a Kaggle dataset that already contains information about twitter sentiment and stock prices for Apple Inc from the period 2016 to 2019. We then created classification models to verify our hypothesis.

## Conclusion and Ethical Considerations
Prediction of stock price is an extremely complex and very challenging task because there are a lot more factors involved such as company scandals, macroeconomic policies, political events, and other factors (i.e. 2020 Covid-19 pandemic) which may impact the stock price. Due to these factors, it is difficult to find out the dependence of a single factor on future prices and trends. 

In addition, we have to admit that our data is limited. Twitter API has limitations on the amount of data that can be accessed. It only allows us to retrieve the most recent tweets. If there are thousands of tweets with a certain hashtag every day, with our limited number of requests we can make, we are not able to get tweets from previous days and thus not use it with our stock data. Although we ended up using a Kaggle dataset with Twitter information regarding Apple stock. The Kaggle dataset also has limited data (Jan'16 - Aug'19) which restricted our analysis to limited number of trading days. In addition, because we got the pre-processed dataset from the Kaggle, we cannot access the original texts from Twitter, which means we do not know how exactly these polarity, or sentiment scores, were calculated.

From our project, we can conclude several findings. 

(1) Generating wordclouds and analyzing comments obtained from each CEO's Twitte account, we were able to conclude that Twitter space may not be the best platform to capture an accurate depiction of the public perception toward a company. There are a lot more irrelevant comments that makes our data noisy. And the amount of replies were too small that we could not really parse signal from the noise. Even though Twitter may not be the accurate description of a company, we could see that they do potentiallly capture what each company is striving towards, since the wordclouds do reflect the most frequently used words on each CEO's Twitter space. 

(2) With Twitter sentiment analysis and machine learning methods, we were able to conclude that, to our surprise, Twitter sentiment does not reflect the trends of stock prices. This could be because only limited people tweets about their stock purchase/sales under the stock ticker hashtags. People who tweet about these stocks are not the comprehensive representation of all shareholders. 

For future models, we would consider conducting NLP on other text sources, such as newspapers and forums. Studies have shown there are successful models that predicts stock trends using text sources from news and forums, instead of social media (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7959635/). We do not want to downplay the power of NLP. We still do believe that public sentiment and how people feel about the market is an important factor of stock price trends. We may want to consider ways to capture a broader crowd of users that better represents a larger population.

The importance of numerous social media platforms in business field has risen drastically over the past years. Many social media platforms have abundant resource about the consumer activities and market trends. Twitter network can be a helpful tool to find the right target audience or to follow the latest marketing trends; however, it may just not be so adequate for predicting stock price trends. 

Although our work is very limited, the takeaways are that there are powerful tools out there and that it’s up to us to make the right decisions on which sources and tools to use in order to create more powerful predictive models. 


## Packages

Kearney, M. W. (2019). rtweet: Collecting and analyzing Twitter data, Journal of Open Source
Software, 4, 42. 1829. doi:10.21105/joss.01829 (R package version 0.7.0)

H. Wickham. ggplot2: Elegant Graphics for Data Analysis. Springer-Verlag New York, 2016.

Hadley Wickham, Romain François, Lionel Henry and Kirill Müller (2021). dplyr: A Grammar of Data Manipulation. R package version 1.0.7. https://CRAN.R-project.org/package=dplyr

Silge J, Robinson D (2016). “tidytext: Text Mining and Analysis Using Tidy Data Principles in R.”_JOSS_, *1*(3). doi: 10.21105/joss.00037 (URL: https://doi.org/10.21105/joss.00037), <URL:http://dx.doi.org/10.21105/joss.00037>.

Garrett Grolemund, Hadley Wickham (2011). Dates and Times Made Easy with lubridate. Journal of Statistical Software, 40(3), 1-25. URL https://www.jstatsoft.org/v40/i03/.

Rinker, T. W. (2021). sentimentr: Calculate Text Polarity Sentiment version 2.9.0.
https://github.com/trinker/sentimentr

Hadley Wickham (2019). stringr: Simple, Consistent Wrappers for Common String Operations. R package version 1.4.0. https://CRAN.R-project.org/package=stringr

Ingo Feinerer and Kurt Hornik (2020). tm: Text Mining Package. R package version 0.7-8.
https://CRAN.R-project.org/package=tm

Ingo Feinerer, Kurt Hornik, and David Meyer (2008). Text Mining Infrastructure in R. Journal of Statistical Software 25(5): 1-54. URL: https://www.jstatsoft.org/v25/i05/.

Milan Bouchet-Valat (2020). SnowballC: Snowball Stemmers Based on the C 'libstemmer' UTF-8 Library. R package version 0.7.0. https://CRAN.R-project.org/package=SnowballC

Ian Fellows (2018). wordcloud: Word Clouds. R package version 2.6.
https://CRAN.R-project.org/package=wordcloud

Erich Neuwirth (2014). RColorBrewer: ColorBrewer Palettes. R package version 1.1-2.
https://CRAN.R-project.org/package=RColorBrewer

Dawei Lang and Guan-tin Chien (2018). wordcloud2: Create Word Cloud by 'htmlwidget'. R package version 0.2.1. https://CRAN.R-project.org/package=wordcloud2

Stephen Milborrow (2021). rpart.plot: Plot 'rpart' Models: An Enhanced Version of 'plot.rpart'. R
package version 3.1.0. https://CRAN.R-project.org/package=rpart.plot

Kuhn et al., (2020). Tidymodels: a collection of packages for modeling and machine learning using tidyverse principles. https://www.tidymodels.org

Wickham et al., (2019). Welcome to the tidyverse. Journal of Open Source Software, 4(43), 1686, https://doi.org/10.21105/joss.01686

Jacob Kaplan (2020). fastDummies: Fast Creation of Dummy (Binary) Columns and Rows from Categorical Variables. R package version 1.6.3. https://CRAN.R-project.org/package=fastDummies

Brandon M. Greenwell and Bradley C. Boehmke (2020). Variable Importance Plots—An Introduction to the vip Package. The R Journal, 12(1), 343--366. URL https://doi.org/10.32614/RJ-2020-013.

Alexandros Karatzoglou, Alex Smola, Kurt Hornik, Achim Zeileis (2004). kernlab - An S4 Package for Kernel Methods in R. Journal of Statistical Software 11(9), 1-20. URL http://www.jstatsoft.org/v11/i09/

Matt Dancho and Davis Vaughan (2020). alphavantager: Lightweight R Interface to the Alpha Vantage API. R package version 0.1.2. https://CRAN.R-project.org/package=alphavantager


## Bibliography

Effrosynidis, Dimitris. “How I Created a Real-Time Twitter Sentiment Analysis Tool for Covid.” Medium, Towards Data Science, 16 Apr. 2020, https://towardsdatascience.com/how-i-created-a-real-time-twitter-sentiment-analysis-tool-for-covid-292ff6a6323b.

Kolasani, Sai Vikram, and Rida Assaf. “Predicting Stock Movement Using Sentiment Analysis of Twitter Feed with Neural Networks.” Journal of Data Analysis and Information Processing, vol. 08, no. 04, 2020, pp. 309–319., https://doi.org/10.4236/jdaip.2020.84018.

Robinson, Julia Silge and David. “2 Sentiment Analysis with Tidy Data: Text Mining with R.” 2 Sentiment analysis with tidy data | Text Mining with R, September 2, 2021. https://www.tidytextmining.com/sentiment.html.

Rul, Céline Van den. “How to Generate Word Clouds in R.” Medium, Towards Data Science, 20 Oct. 2019, https://towardsdatascience.com/create-a-word-cloud-with-r-bde3e7422e8a.

## Kaggle Dataset 

Sirimevan, N. (2019). "Twitter Sentiments AAPL stock". Retrieved December 10, 2021 from https://www.kaggle.com/nadun94/twitter-sentiments-aapl-stock

