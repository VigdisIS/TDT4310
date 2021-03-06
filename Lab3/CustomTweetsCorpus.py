from __future__ import division

from Lab3_2 import preprocess_tweet
from tweepy import OAuthHandler, API
from nltk import *
from nltk.corpus import stopwords
import csv

stop_words = set(stopwords.words('english'))

# Personal tokens

consumer_key = []
consumer_secret = []
access_token = []
access_token_secret = []

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)


def createTweetsTxt(userID):
    tweets = api.user_timeline(screen_name=userID,
                               count=200,
                               include_rts=False,
                               tweet_mode='extended'
                               )

    all_tweets = [tweet.full_text for tweet in tweets]
    test_tweets = all_tweets[:5]
    all_tweets = all_tweets[5:]

    for tweet in test_tweets:
        with open(f'{userID}_tests.txt', 'a', encoding='utf-8') as f:
            f.write(tweet)
            f.write('\n')
            f.close()

    for tweet in all_tweets:
        tweet_re = preprocess_tweet(tweet)
        with open(f'all_tweets.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['User', 'Tweet']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'User': f'{userID}', 'Tweet': f'{tweet_re}'})
            csvfile.close()


createTweetsTxt("xQc")
createTweetsTxt("RichardDawkins")
