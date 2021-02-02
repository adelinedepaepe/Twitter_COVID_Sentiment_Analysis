import twint
#
# # Configure
# c = twint.Config()
# c.Search = "covid"
# c.Since = "2020-07-01"
# c.Store_csv = True
# c.Output='covid_tweets_6months.csv'
#
# # Run
# twint.run.Search(c)
## Liste des dates
import datetime
import numpy as np
import os

numdays = 365
dateList = []


    # # Détermine une heure de collecte random pour éviter les biais dus aux fuseaux horaires
    # hour = str ( np.random.randint ( 24, size=1 )[0] )
    # if len ( hour ) < 2:
    #     hour = '0' + hour
    #
    # min = str ( np.random.randint ( 60, size=1 )[0] )
    # if len ( hour ) < 2:
    #     hour = '0' + hour
    #
    # sec = str ( np.random.randint ( 60, size=1 )[0] )
    # if len ( hour ) < 2:
    #     hour = '0' + hour
a = datetime.datetime.strptime ( f'2021-01-07 15:00:00', '%Y-%m-%d %H:%M:%S' )

for x in range (0,numdays):
    dDay = str ( a.date () - datetime.timedelta ( days=x ) )
    #dDay_and_Hour = str ( a - datetime.timedelta ( days=x ) )
    dayAfter = str ( a.date () - datetime.timedelta ( days=x - 1 ) )
    #dayAfter_and_Hour = str ( a - datetime.timedelta ( days=x - 1 ) )
    dateList.append ( (dDay, dayAfter) )

print (dateList)

#
# ##Extraction TWINT
for (dDay, dayAfter) in dateList:
    print(dDay)
    print(dDay, dayAfter)
    if not os.path.exists ( f"C:\\Users\\Administrateur\\PycharmProjects\\Data_Twitter_COVID_Sentiment_Analysis\\{dDay}.json" ):

        # #nom du fichier json qui sera produit dans le dossier Data
        filename = dDay+".json"
        #
        # #lancement de l’objet twint
        c = twint.Config()
        #
        # Recherche des twwets contenant le mot covid
        c.Search = "covid"
        # ## Paramétrage Twint
        # On veut créer un fichier par jour
        c.Since = dDay
        c.Until = dayAfter
        c.Lang = "fr"
        c.Lang = "en"
        c.Min_likes=25
        c.Limit = 10000
        # Affichage du nombre de tweets récupérés
        c.Count = True
        # Nous désirons stocker un fichier json contenant l’ensemble des tweets récupérés
        c.Store_json = True
        # Nom du fichier json dans lequel les tweets seront enregistrés
        c.Output = 'C:\\Users\\Administrateur\\PycharmProjects\\Data_Twitter_COVID_Sentiment_Analysis\\'+filename
        # Stockage dans elasticsearch
        #c.Elasticsearch = "localhost:9200"

        # Lancement de la recherche
        twint.run.Search(c)
        print(c.Output)