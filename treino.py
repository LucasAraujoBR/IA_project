import numpy as np
import pandas as pd
from nltk.corpus import stopwords
import string
from sklearn.model_selection import train_test_split


def treina_maquina():
    #dataframes
    bossa = pd.read_csv('dataset/bossa_nova.csv')
    funk = pd.read_csv('dataset/funk.csv')
    gospel = pd.read_csv('dataset/gospel.csv')
    sertanejo = pd.read_csv('dataset/sertanejo.csv')

    #Atribuir colunas a generos
    bossa['Gen'] = 'Bossa Nova'
    funk['Gen'] = 'Funk'
    gospel['Gen'] = 'Gospel'
    sertanejo['Gen'] = 'Sertanejo'

    datasets = [bossa,funk,gospel,sertanejo]

    lyrics = pd.concat(datasets)

    lyrics.reset_index(drop=True,inplace=True)

    lyrics = lyrics.replace(r'\r',' ', regex=True) 
    lyrics.reset_index(drop=True,inplace=True)
    
    lyric_train,lyric_test,label_train,label_test = train_test_split(lyrics['lyric'],lyrics['Gen'],test_size=0.3)

    #Retorna uma lista com as variáveis treinadas para serem usadas na função resultado
    return [lyric_train,lyric_test,label_train,label_test]


    