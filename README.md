# naisc2022
Code for National AI Student Challenge 2022

What does each file do?

scrape.py utilises the twitter API to scrape tweets according to the pre-defined parameters and returns a list of dictionaries to be passed to be processed by nlp model.

senticgcnbert.py employs sgnlp's aspect-based sentiment analysis model to label each and every tweet according to positive, negative or neutral sentiments.

nlpoutputtocsv.py converts the output from the sgnlp to a csv file which is processed to produce the dashboard.

