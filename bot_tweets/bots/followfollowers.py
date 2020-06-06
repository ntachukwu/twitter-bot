#!/user/bin/env python

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

def main():  #creates a Tweepy API object
    api = create_api() #using the create_api from the config module
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()