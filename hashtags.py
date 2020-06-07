import tweepy
from time import sleep
from config import create_api

# Access and authorize our Twitter credentials from credentials.py
api = create_api()
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
