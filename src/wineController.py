import pandas as pd


data = pd.read_csv('ressources/external_data.csv')

def getWine(id):
  wine = data[data['ID'] == id]
  return wine.to_dict('records')[0]

def searchWine(query):
  # SEARCH IN NOM , APPELLATION, PAYS, PRODUCTEUR, ANNEE
  wine = data[data['NOM'].str.contains(query, case=False)]
  wine = wine.append(data[data['APPELLATION'].str.contains(query, case=False)])
  wine = wine.append(data[data['PAYS'].str.contains(query, case=False)])
  wine = wine.append(data[data['PRODUCTEUR'].str.contains(query, case=False)])
  

  # remove duplicates
  wine = wine.drop_duplicates()
  
  # take the first 20 results
  wine = wine.head(20)

  return wine.to_dict('records')

