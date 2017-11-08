#Programs function:
#1. Retweet tweets that cointains certain keywords posted within the last 10 minutes by cchosen accounts

# Importing Tweepy libary (Libary for Twitter API) + Textblob (Market Sentiment)
import tweepy

#Twitter API
consumer_key = 'MYCONSUMERKEY'
consumer_secret = 'MYCONSUMERSECRET'

access_token = 'MYACCESSTOKEN'
access_token_secret = 'MYACCESSTOKENSECRET'

#Tweepy Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Twitter-bot
user = api.get_user('Bitcoin', 'ethereumproject')
public_tweets = api.search('release', 'new', 'roadmap', 'listing', 'news')

for tweet in public_tweets:
    print(tweet.text)


