from textblob  import  TextBlob
import tweepy

consumer_key='Z9Ghgwv0iVrd6o7berSQVoIKD'
consumer_secret='vtDEJjzJBB6k13gKSJCX7knQlOy0kvHvhjS8HtBlV9gjfGXWEL'
access_token='61558046-e9QNJlXfpX7zxwhaEP27pTZfYh7r51sSSgc1l4wZC'
access_token_secret='gpDiYRxjQmbiB3VODrKvxsUKSmPTgWWltxF4w0P5Cm3D3'
auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)


def getTweets(api):
    tweets=api.search('Oscars')
    return tweets

def allTweet(tweets):
    for tweet in tweets:
        print(tweet.text)
        analysis=TextBlob(tweet.text)
        print(analysis.sentiment)




tweets=getTweets(api)

allTweet(tweets)