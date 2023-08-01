"""!pip install tweepy
"""

import os
import tweepy as tw
import pandas as pd

# Define the search term and the date_since date as variables
search_words = "#IPL"
date_since = "2022-04-16"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)