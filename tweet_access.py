from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream

import credentials

class TwitterClient():
    def __init__(self, user = None):
        self.auth = TwitterAuthenticator().authenticate_twitter_api()
        self.twitter_client = API(self.auth)
        self.twitter_user = user

    def get_twitter_client_api(self):
        return self.twitter_client


    def get_searched_tweets(self, query, num_tweets,api):
        searched_tweets=[]
        for tweet in Cursor(self.twitter_client.search, q = (query), lang = 'en', tweet_mode='extended').items(num_tweets):
            id = tweet.id
            status = api.get_status(id, tweet_mode="extended")
            lang = api.get_status(id).lang
            if hasattr(status, "retweeted_status") and lang == 'en':
                try:
                    #print(status.retweeted_status.extended_tweet["full_text"])
                    searched_tweets.append(status.retweeted_status.extended_tweet["full_text"])
                except AttributeError:
                    #print('error')
                    searched_tweets.append(status.retweeted_status.full_text)
            elif lang == 'en':
                try:
                    #print(status.extended_tweet["full_text"])
                    searched_tweets.append(status.extended_tweet["full_text"])
                except AttributeError:
                    #print(status.text)
                    searched_tweets.append(status.full_text)

            #if lang == 'en':
            #    searched_tweets.append(tweet.full_text)

        return searched_tweets


class TwitterAuthenticator():

    def authenticate_twitter_api(self):
        auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
        return auth


if __name__ == '__main__':
    tc = TwitterClient()
    api = tc.get_twitter_client_api()

    tweets = tc.get_searched_tweets(query='#COVID19', num_tweets= 1, api = api)
    print(tweets)
