#!/usr/bin/env python3
import tweepy
from time import sleep
import os

# Access and authorize our Twitter credentials from credentials.py
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

for tweet in tweepy.Cursor(api.search, q=('#HNG OR #owerritech OR #dsc OR #DSC OR #dscowerri OR #intern OR #blacklivesmatter OR #hng #python #programming #programmer OR #internship -filter:retweets'), lang='en').items(5):
    try:
            # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

            # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')
        sleep(10)

    except tweepy.TweepError as error:
        print('n\Error. Retweet not successful. Reason')
        print(e.reason)

    except StopIteration:
        break
