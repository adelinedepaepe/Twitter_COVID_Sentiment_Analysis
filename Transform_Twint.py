import os
from os import walk
import pandas as pd

for (dirpath, dirnames, filenames) in walk ("C:\\Users\\Administrateur\\PycharmProjects\\Data_Twitter_COVID_Sentiment_Analysis_Twint" ):
    for filename in filenames:
        if not os.path.exists (f"C:\\Users\\Administrateur\\PycharmProjects\\Data_Twitter_COVID_Sentiment_Analysis_transformed\\{filename}" ):
            print(f"C:\\Users\\Administrateur\\PycharmProjects\\Data_Twitter_COVID_Sentiment_Analysis_Twint\\{filename}")
            df = pd.read_json(f"C:\\Users\\Administrateur\\PycharmProjects\\Data_Twitter_COVID_Sentiment_Analysis_Twint\\{filename}", lines=True )
            df_transformed = df[['id','user_id','username','place','language','tweet','likes_count','retweets_count','created_at']]
            df_transformed = df_transformed.rename ( columns={'id':'tweet_id','username': 'user_name', 'place': 'location', 'language':'coordinates', 'tweet':'text', 'likes_count':'favorite_count','retweets_count':'retweet_count'} )
            df_transformed['coordinates']=''
            df_transformed.to_json(f"C:\\Users\\Administrateur\\PycharmProjects\\Data_Twitter_COVID_Sentiment_Analysis_transformed\\{filename}", orient='records')