# Importing Tweepy libary (Libary for Twitter API)
import tweepy

# Twitter API
consumer_key = 'XXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXX'

access_token = 'XXXXXXXXXX-XXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXX'

# Tweepy Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

# Getting last tweet from accounts below
# users = ['rihanna','BarackObama']
# for user in users:
#     stuff = api.user_timeline(screen_name = user, count = 1, include_rts = True)
#     for status in stuff:
#         print(status.text)

# Getting newly tweeted tweets from users below


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(follow=['12521521', '2312313', '123123'])

