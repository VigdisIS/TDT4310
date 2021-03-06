from tweepy import OAuthHandler, API

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

    for tweet in tweets:
        tweet = tweet.full_text
        f = open(f'{userID}s tweets.txt', 'a', encoding="utf-8")
        f.write(tweet + ' ')
        f.close()


# Twitch streamers

createTweetsTxt("xQc")
createTweetsTxt("Sodapoppintv")
createTweetsTxt("adeptthebest")
createTweetsTxt("nmplol")
createTweetsTxt("REALMizkif")
createTweetsTxt("39daph")
createTweetsTxt("Trainwreckstv")
createTweetsTxt("nymnion")
createTweetsTxt("m0xyOW")
createTweetsTxt("pokelawls")
