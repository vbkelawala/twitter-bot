import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECREt = os.getenv('ACCESS_SECRET')


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECREt)

api = tweepy.API(auth)

tweet_list = api.favorites(screen_name='vatsalbk', count=5)
# print(tweet_list)

# for tweet in tweet_list:
#     print(tweet.id)

# Retweet a Tweet ID
# tweet_id = 1180813350931841024
# api.retweet(tweet_id)

# Retweet each Tweet