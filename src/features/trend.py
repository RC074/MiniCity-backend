import tweepy # tweeter auth library

# KEYS
consumer_key = "u4tKvnKfwIDLLFwkOctP7MLMP"
consumer_secret = "BjVdVSYtpal1f4INyOrACeXTfP2YpLIE7fDd2bLk7lHMxI5jgN"
access_token = "1307707458090160128-saz9xr7r5cmSaLOQhQ2GW3LKd2w55J"
access_token_secret = "oM6Q2vL1JObggmnWmyslcRbgfI4fdCH0ghNGMAmvVY2py"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def get_tweets(query):
    '''
    parameter: query - the keywords to search
    returns a list of tweets ids
    '''

    # start the query
    rawTweets = api.search(q=query+'-filter:retweets', count=10)

    # empty dictionary to store username and their tweet
    # to avoid same user spamming tweets
    tweets = {}
    for tweet in rawTweets:
        # retrieve relevant data from the response obj
        tweets[tweet.user.name] = str(tweet._json['id'])
    return list(tweets.values())

if __name__ == '__main__': # for testing purposes
    print(get_tweets("Hawaiian Gardens USA"))