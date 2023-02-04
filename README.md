# naisc2022
Code for National AI Student Challenge 2022

Our dashboard summarises different graphical representations of the data we obtained. The bar chart shows the distribution of the sentiment level from the tweets we scraped from Twitter.  Meanwhile, the pie chart represents the percentage of each category, namely negative, neutral and positive to show the distribution of consumers' sentiment against the company's products and services.



What does each file do?

scrape.py utilises the twitter API to scrape tweets according to the pre-defined parameters and returns a list of dictionaries to be passed to be processed by nlp model.

senticgcnbert.py employs sgnlp's aspect-based sentiment analysis model to label each and every tweet according to positive, negative or neutral sentiments.

nlpoutputtocsv.py converts the output from the sgnlp to a csv file which is processed to produce the dashboard.

dashboard.py takes the csv file as input and generates our final product - a comprehensive dashboard for businesses to make sense of consumer sentiment

requirements.txt contains the modules required to run the data scraping process
