#https://towardsdatascience.com/step-by-step-twitter-sentiment-analysis-in-python-d6f650ade58d

import textblob

from textblob import TextBlob
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_json('C:\\Users\\Administrateur\\PycharmProjects\\Data_Twitter_COVID_Sentiment_Analysis\\2021-01-07.json', lines=True)
tweets = df['tweet']

noOfTweet = df['tweet'].count()

positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []

for tweet in tweets:
    #print(tweet)
    tweet_list.append ( tweet )
    analysis = TextBlob ( tweet )
    score = SentimentIntensityAnalyzer ().polarity_scores ( tweet )
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']
    polarity += analysis.sentiment.polarity

    if neg > pos:
        negative_list.append ( tweet )
        negative += 1
    elif pos > neg:
        positive_list.append ( tweet )
        positive += 1

    elif pos == neg:
        neutral_list.append ( tweet )
        neutral += 1

positive = (positive/ noOfTweet )*100
negative = ( negative/ noOfTweet )*100
neutral = ( neutral/ noOfTweet )*100
polarity = (polarity/noOfTweet )*100
positive = format ( positive, '.1f')
negative = format ( negative, '.1f')
neutral = format ( neutral, '.1f')

tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)
print("total number: ",len(tweet_list))
print("positive number: ",len(positive_list))
print("negative number: ", len(negative_list))
print("neutral number: ",len(neutral_list))

labels = ['Positive ['+str(positive)+'%]' , 'Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'blue','red']
patches, texts = plt.pie(sizes,colors=colors, startangle=90)
plt.style.use('default')
plt.legend(labels)
plt.title("Sentiment Analysis Result for COVID" )
plt.axis("equal")
plt.show()

#Cleaning Text (RT, Punctuation etc)
#Creating new dataframe and new features
tw_list = pd.DataFrame(tweet_list)
tw_list['text'] = tw_list[0]
#Removing RT, Punctuation etc
remove_rt = lambda x: re.sub('RT @\w+: '," ",x)
rt = lambda x: re.sub("(@[A-Za-z0–9]+)|(\w+:\/\/\S+)"," ",x)
tw_list["text"] = tw_list.text.map(remove_rt).map(rt)
tw_list["text"] = tw_list.text.str.lower()
print(tw_list.head(10))

#Calculating Negative, Positive, Neutral and Compound values
tw_list[['polarity', 'subjectivity']] = tw_list['text'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
print(tw_list)
for index, row in tw_list['text'].iteritems():
    
    score = SentimentIntensityAnalyzer().polarity_scores(row)

    tw_list.loc[index, 'neg'] = score['neg']
    tw_list.loc[index, 'neu'] = score['neu']
    tw_list.loc[index, 'pos'] = score['pos']
    tw_list.loc[index, 'comp'] = score['compound']
    if neg > pos:
        tw_list.loc[index, 'sentiment'] = 'negative'
    elif pos > neg:
        tw_list.loc[index, 'sentiment'] = 'positive'
    else:
        tw_list.loc[index, 'sentiment'] = 'neutral'
        tw_list.loc[index, 'neg'] = neg
        tw_list.loc[index, 'neu'] = neu
        tw_list.loc[index, 'pos'] = pos
        tw_list.loc[index, 'compound'] = comp
print(tw_list.head(10))