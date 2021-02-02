import tweepy
import pandas as pd
import datetime
import numpy as np
import os


numdays = 365
dateList = []

#Authentification Twitter
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler("EEPcCh8aVpLqhAJWsa4Xak5T7", "mGZQ0e0KumWfIMi7htwP3CMmCh2AI342KKqJIAbhljdGqmaBG8" )
    auth.set_access_token("1334519801818066950-AulNhmPKQtkeDvuDm7L4XQZ4A3cS7A","Y7T5ACV6Xz9UjkAR0nyfxEXJVzzw0HL9UjAWTbZP6JyKQ")
    api = tweepy.API ( auth, wait_on_rate_limit=True,
                       wait_on_rate_limit_notify=True )
    return api

#test de l'authentification
#try:
#    api.verify_credentials()
#    print("Authentication OK")
#except:
#    print("Error during authentication")

#Création de l'objet Twitter
api = connect_to_twitter_OAuth()

#COllecte de tweets
a = datetime.datetime.strptime ( f'2021-02-01 15:00:00', '%Y-%m-%d %H:%M:%S' )

for x in range (0,numdays):
    dDay = str ( a.date () - datetime.timedelta ( days=x ) )
    #dDay_and_Hour = str ( a - datetime.timedelta ( days=x ) )
    dayAfter = str ( a.date () - datetime.timedelta ( days=x - 1 ) )
    #dayAfter_and_Hour = str ( a - datetime.timedelta ( days=x - 1 ) )
    dateList.append ( (dDay, dayAfter) )

print (dateList)

#
def extract_tweet_attributes(tweet_object):
    # create empty list
    tweet_list = []
    # loop through tweet objects
    for tweet in tweet_object:
        if tweet.place is None:
            tweet_id = tweet.id  # unique integer identifier for tweet
            user_id = tweet.user.id
            user_name = tweet.user.name
            location = tweet.user.location
            coordinates = ''
            text = tweet.text  # utf-8 text of tweet
            favorite_count = tweet.favorite_count
            retweet_count = tweet.retweet_count
            created_at = tweet.created_at  # utc time tweet created
            source = tweet.source  # utility used to post tweet
            reply_to_status = tweet.in_reply_to_status_id  # if reply int of orginal tweet id
            reply_to_user = tweet.in_reply_to_screen_name  # if reply original tweetes screenname
            retweets = tweet.retweet_count  # number of times this tweet retweeted
            favorites = tweet.favorite_count  # number of time this tweet liked
        else:
            tweet_id = tweet.id  # unique integer identifier for tweet
            user_id = tweet.user.id
            user_name = tweet.user.name
            location = tweet.place.country
            coordinates = tweet.place.bounding_box.coordinates[0][0]
            text = tweet.text  # utf-8 text of tweet
            favorite_count = tweet.favorite_count
            retweet_count = tweet.retweet_count
            created_at = tweet.created_at  # utc time tweet created
            source = tweet.source  # utility used to post tweet
            reply_to_status = tweet.in_reply_to_status_id  # if reply int of orginal tweet id
            reply_to_user = tweet.in_reply_to_screen_name  # if reply original tweetes screenname
            retweets = tweet.retweet_count  # number of times this tweet retweeted
            favorites = tweet.favorite_count  # number of time this tweet liked

        # append attributes to list
        tweet_list.append ( {'tweet_id': tweet_id,
                             'user_id': user_id,
                             'user_name': user_name,
                             'location': location,
                             'coordinates': coordinates,
                             'text': text,
                             'favorite_count': favorite_count,
                             'retweet_count': retweet_count,
                             'created_at': created_at,
                             'source': source,
                             'reply_to_status': reply_to_status,
                             'reply_to_user': reply_to_user,
                             'retweets': retweets,
                             'favorites': favorites} )
    # create dataframe
    df = pd.DataFrame ( tweet_list, columns=['tweet_id',
                                             'user_id',
                                             'user_name',
                                             'location',
                                             'coordinates',
                                             'text',
                                             'favorite_count',
                                             'retweet_count',
                                             'created_at',
                                             'source',
                                             'reply_to_status',
                                             'reply_to_user',
                                             'retweets',
                                             'favorites'] )
    return df

# ##Extraction TWINT
for (dDay, dayAfter) in dateList:
    print(dDay)
    print(dDay, dayAfter)

    if not os.path.exists ( f"C:\\Users\\Administrateur\\PycharmProjects\\Data_Twitter_COVID_Sentiment_Analysis_API\\{dDay}.json" ):
        filename = dDay + ".json"

        covid_tweets = tweepy.Cursor(api.search, q='covid', since= dDay, until=dayAfter, lang="en").items(1000)

        df = extract_tweet_attributes(covid_tweets)
        print(df)

        df.to_json(f"C:\\Users\\Administrateur\\PycharmProjects\\Data_Twitter_COVID_Sentiment_Analysis_API\\{dDay}.json", orient='records')