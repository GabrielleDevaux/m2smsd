import pandas as pd


#1
df_meteo=pd.read_csv('meteo.csv',sep=";")
df_meteo.tail()
df_evenements=pd.read_csv('evenements.csv',sep=";")
df_evenements.tail()
