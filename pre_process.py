##pre processamento das letras musicais 
import numpy as np
import pandas as pd


#Leitura dos datasets
bossa = pd.read_csv('datasets/bossa_nova.csv')
funk = pd.read_csv('datasets/funk.csv')
gospel = pd.read_csv('datasets/gospel.csv')
sertanejo = pd.read_csv('datasets/sertanejo.csv')

rap = pd.read_csv('datasets/drake_data.csv')
all_bossa_nova =  pd.read_csv('datasets/bossa_nova_songs_dataset.csv')
rock_country_reb =  pd.read_csv('datasets/rock_country_R&B.csv')
songs =  pd.read_csv('datasets/songs_normalize.csv')



rap_lyrics = pd.DataFrame(rap['lyrics'])  #OK
rap_lyrics.rename(columns={'lyrics': 'lyric'}, inplace = True) #OK

all_bossa = pd.DataFrame(all_bossa_nova['song_lyrics']) #OK
all_bossa.rename(columns={'song_lyrics': 'lyric'}, inplace = True) #OK

rock = pd.DataFrame(rock_country_reb['lyrics'].loc[(rock_country_reb['type'] == 'rock')]) #OK
rock.rename(columns={'lyrics': 'lyric'}, inplace = True) #OK

country = pd.DataFrame(rock_country_reb['lyrics'].loc[(rock_country_reb['type'] == 'country')]) #OK
country.rename(columns={'lyrics': 'lyric'}, inplace = True) #OK

reb = pd.DataFrame(rock_country_reb['lyrics'].loc[(rock_country_reb['type'] == 'R&B')]) #OK
reb.rename(columns={'lyrics': 'lyric'}, inplace = True) #OK

##Criando a coluna correspondete ao genero

bossa['gen'] = 'Bossa Nova'
funk['gen'] = 'Funk'
gospel['gen'] = 'Gospel'
sertanejo['gen'] = 'Sertanejo'
rap_lyrics['gen'] = 'Rap'
all_bossa['gen'] = 'Bossa Nova'
rock['gen'] = 'Rock'
country['gen'] = 'Sertanejo'
reb['gen'] = 'R&B'

datasets = [bossa,funk,gospel,sertanejo,rap_lyrics,all_bossa,rock,country,reb]
lyrics = pd.concat(datasets)
lyrics.reset_index(drop=True,inplace=True)

print(lyrics)
