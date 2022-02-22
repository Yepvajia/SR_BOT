# import os

# here = os.path.dirname(os.path.abspath(__file__))
# print(here)

import tweepy
# import pandas as pd

API_KEY = "SuIU8eOMLgxolVWdZ4Z157pDR"
API_KEY_SECRET = "EBFMPIN32XDZxKNG5fORCGQL257maOmnVTVOutDzCvXDPVUAVE"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADVJZQEAAAAAgZ54%2BMB9Vj3iTce5uNu1MN9xLyM%3DYZ1eJNZlqsHdrkHkKamPycBpTuKX5HsgNHIKMmL4ZMVdZxWszA"
ACCESS_TOKEN = "1494133144173387779-OFCW33JvaeOo3m6BqAJfxEyDsIyxO0"
ACCESS_TOKEN_SECRET = "jdc5DV6cEOQtG2G3fV6oHEpEWg0HFLexWylraZ7cLdICf"

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def tweet_dick():
    yep_tweet = api.user_timeline(screen_name="yepperdev", count=3, 
    tweet_mode="extended", include_rts=False)
    for info in yep_tweet:
            return info.full_text


print(tweet_dick())