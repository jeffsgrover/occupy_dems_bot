import json, random, tweepy, sys
from os import environ

# oauth_ID      = credentials.oauth_2_0_client_ID
# oauth_secret  = credentials.oauth_2_0_client_ID_secret
# access_token  = credentials.access_token
# access_secret = credentials.access_token_secret
# bearer_token  = credentials.bearer_token
# api_key       = credentials.API_key
# api_secret    = credentials.API_key_secret

access_token  = environ['access_token']
access_secret = environ['access_token_secret']
bearer_token  = environ['bearer_token']
api_key       = environ['API_key']
api_secret    = environ['API_key_secret']

def get_tweets():
    with open('occupy_tweets.json') as f:
        tweets = json.load(f)
    return tweets['tweets']

def get_random_tweet():
    tweets = get_tweets()
    random_tweet = random.choice(tweets)
    return random_tweet['tweet']


client = tweepy.Client(bearer_token=bearer_token)

client = tweepy.Client(
    consumer_key        = api_key,
    consumer_secret     = api_secret,
    access_token        = access_token,
    access_token_secret = access_secret
)

if __name__ == "__main__":
    client.create_tweet(text=get_random_tweet())