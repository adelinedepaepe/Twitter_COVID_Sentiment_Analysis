import numpy as np

hour = str(np.random.randint(24, size=1)[0])
if len(hour)<2:
    hour= '0'+hour

min = str(np.random.randint(60, size=1)[0])
if len(hour)<2:
    hour= '0'+hour

sec = str(np.random.randint(60, size=1)[0])
if len(hour)<2:
    hour= '0'+hour

print(f"{hour}:{min}:{sec}")

print ("______________________________")
import datetime

a = datetime.datetime.strptime ( f'2020-12-10 {hour}:{min}:{sec}', '%Y-%m-%d %H:%M:%S' )


dDay = str ( a - datetime.timedelta ( days=1 ) )
dayAfter = str ( a - datetime.timedelta ( days=1 - 1 ) )

print(dDay)
print(dayAfter)

print("-------------------------------------------------")

import twint

#nom du fichier json qui sera produit
filename = "test.json"
#
# #lancement de l’objet twint
c = twint.Config()
#
# Recherche des twwets contenant le mot covid
c.Search = "covid"
# ## Paramétrage Twint
# On veut créer un fichier par jour
c.Since = "2020-12-06 13:45:25"
c.Until = "2020-12-07 05:12:25"
c.Popular_tweets = True
c.Min_likes = 1000
c.Lang = "fr"
c.Lang = "en"
c.Limit = 100
# Nombre de tweets récupérés
c.Count = True
# Nous désirons stocker un fichier json contenant l’ensemble des tweets récupérés
c.Store_json = True
# Nom du fichier json dans lequel les tweets seront enregistrés
c.Output = '.\\Data\\'+filename
# Stockage dans elasticsearch
#c.Elasticsearch = "localhost:9200"

# Lancement de la recherche
twint.run.Search(c)