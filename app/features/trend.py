import tweepy # tweeter auth library

# KEYS
consumer_key = "ASZ6kt5mBqRH1bsJ0GpvDxu1e"
consumer_secret = "lHY4ZhplH9Kz5bIgFMeUeDXBn7y2lK27xSLaXHZMyV4R7irYgT"
access_token = "1307707458090160128-7SBar0MtxNEXxIwGrDTFzkvoCfG4Ku"
access_token_secret = "ZqsQMp1Vo8cL3VjfbMjTpjOtS4JTXXB4EuSLt6B1g9vhc"

# Authenticate to Twitter
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# Create API object
# api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAAEkkgEAAAAAemlC68kWKwVFwKepZQ%2FiW0lb0BU%3DGNrc9ilbbttkJBzTaLR7iuXMkVMgE2PtW9G3kRn5LSNpgEcsFS", wait_on_rate_limit=True)

def get_tweets(query):
    '''
    parameter: query - the keywords to search
    returns a list of tweets ids
    '''
    # start the query
    rawTweets = client.search_recent_tweets(query=query, max_results=10)
    
    
    # to avoid same user spamming tweets
    
    return list(set([str(tweet.id) for tweet in rawTweets.data]))

if __name__ == '__main__': # for testing purposes
    print(get_tweets("waterloo"))