import creds
import requests
import json
from textblob import TextBlob

# Define your Twitter API v2 bearer token
bearer_token = creds.BEARER_TOKEN


# Define the keywords to search for
keywords = ["salt bae", 'restaurant']

# Define the endpoint for searching tweets
endpoint = 'https://api.twitter.com/2/tweets/search/recent'

# Define headers for the request
headers = {
    'Authorization': 'Bearer ' + bearer_token,
    'User-Agent': 'Sgnlp'
}

# Define the parameters for the request
params = {
    'query': ' '.join(keywords) + ' -is:retweet' + ' is:reply',
    'max_results': '10',
    'sort_order': 'recency'
}

# Make the request
response = requests.get(endpoint, headers=headers, params=params)

# Check if the request was successful
if response.status_code != 200:
    print(f'Request failed with status code {response.status_code}')
    print(response.text)
    exit()

# Parse the JSON response
data = json.loads(response.text)



nlpmodelinputs = []

if 'data' in data:
    for tweet in data['data']:
        tweet_text = tweet['text']
        lst = [] 
        for np in TextBlob(tweet['text']).noun_phrases:
            lst.append(np)
        dic = {}
        dic['sentence'] = tweet_text
        dic['aspects'] = lst
        nlpmodelinputs.append(dic)
else:
    print("No tweets found.")

return nlpmodelinputs



