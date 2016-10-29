# Import the required libraries.
import tweepy
import pandas as pd
import matplotlib.pyplot as plt
consumer_key = 'qwiqIHfWWSEboTUSg99Lcyhkz'
consumer_secret = 'vQsenAmllieYjgpOR86WElkyeQkjduS8R7el1aim8r4CDoeDJv'
access_token = '276459705-rDTmtyWjjaddIPCh5ra1SWp1UAUCryqT5fDDdkML'
access_secret = 'anRi5K07z2xZE6BIeq4o0yO7vIMDksnN2C6Zo6l9L41Rc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
###for tweet in public_tweets:
###    print (tweet.text)
#user = api.get_user('@roomthinker')
##print(user)
#result = api.search(q='%ObamaInKenya') #%23 is used to specify '#'
#tweet = result[0] #Get the first tweet in the result
#print(tweet)

# Analyze the data in one tweet to see what we require
#for param in dir(tweet):
##The key names beginning with an '_' are hidden ones and usually not required, so we'll skip them
#    if not param.startswith("_"):
#        print ("%s : %s\n" % (param, eval('tweet.'+param)))

results = []

#Get the first 5000 items based on the search query
for tweet in tweepy.Cursor(api.search, q='%#YouAreNairobianIf').items(10):
    results.append(tweet)

# Verify the number of items returned
print (len(results))

# Create a function to convert a given list of tweets into a Pandas DataFrame.
# The DataFrame will consist of only the values, which I think might be useful for analysis...


def toDataFrame(tweets):

    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]


    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet in tweets]

    return DataSet

#Pass the tweets list to the above function to create a DataFrame
DataSet1 = toDataFrame(results)
print(DataSet1.head())
def save():
    DataSet1.to_csv("C:/Users/musa/Desktop/kot.csv")
save()
