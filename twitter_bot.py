import json, random, tweepy, credentials, sys
from os import environ

CONSUMER_KEY    = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY      = environ['ACCESS_KEY']
ACCESS_SECRET   = environ['ACCESS_SECRET']

def get_tweets():
    with open('occupy_tweets.json') as f:
        tweets = json.load(f)
    return tweets['tweets']

def get_random_tweet():
    tweets = get_tweets()
    random_tweet = random.choice(tweets)
    return random_tweet

def post_tweet():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    tweet = get_random_tweet()
    api.update_status(tweet)
    
if __name__ == "__main__":
    post_tweet()