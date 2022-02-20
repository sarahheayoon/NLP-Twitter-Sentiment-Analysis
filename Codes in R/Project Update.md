Project Update:

1. Have you already collected, or do you have access to, all of the data that you will need in order to complete your project? If not, please estimate the percentage of the data that you have, describe any issues that you are having, and what your plan is for getting the rest of the data. 

We have all the access to stock data and have most of our Twitter data ready for the project. We know how to access and wrangle the data from specific Twitter accounts/hashtags. However, we are currently having a problem with retrieving replies from each Twitter post. Our plan is to use Python to get the replies, export it in csv file, and read it in R. 


2. What is the single biggest unresolved issue you are having? Please describe it briefly, and what your plan is for resolving this issue. 

The biggest unresolved issue so far is obtaining the replies from twitter posts. I thought that there would be a function in one of the twitter R packages but there isn’t. Python, on the other hand, does have functions for those. So, we plan on using python to acquire that data and then import it into R.

Furthermore, we worked on getting data on the retweets for each tweet of interest. After looking at the results of my sample, I observed that the retweets don’t contain any comments with their retweets, meaning that people just share a post and don’t add any comments of their own. So, getting data on retweets is quite useless - only the number of retweets could be helpful.


3. What are the elements from outside of the course, if any, that you plan to incorporate into your project? 

We plan to incorporate Sentiment Analysis. Up to now, we learned how to clean up the punctuations in users’ replies, break up the text into single words and generate word clouds based on the frequency of words. To evaluate the positivity/negativity of texts, we tried using the afinn dictionary that has sentiment scores for a few thousand words, and we are also looking into the “sentimentr” package. 

For the final product, we plan to use Shiny to create an interactive dashboard that shows the word cloud generated from a CEO’s tweets, the line graph of their followers’ sentiment scores evaluated from tweet replies, and the line graph of changes in the corresponding company’s stock price. We plan to analyze around 5 companies.
