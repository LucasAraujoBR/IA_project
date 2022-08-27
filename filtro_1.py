import numpy as np
import pandas as pd
from nltk.corpus import stopwords
import string
from sklearn.svm import SVC


def processamento_texto(txt):
    # remover quebras de linha
    txt = txt.replace('\n',' ')
    # remover símbolos de pontuação, resultando em um array de caracteres
    txt = [char for char in txt if char not in string.punctuation]
    # depois, juntar os caracteres em palavras novamente e separá-los em uma lista de tokens
    txt = ''.join(txt).split()
    # por fim, remover as stopwords da lista
    txt = [word for word in txt if word.lower() not in stopwords.words('portuguese')]
    
    return txt



#dataframes
bossa = pd.read_csv('dataset/bossa_nova.csv')
funk = pd.read_csv('dataset/funk.csv')
gospel = pd.read_csv('dataset/gospel.csv')
sertanejo = pd.read_csv('dataset/sertanejo.csv')

#Atribuir colunas a generos
bossa['Genero'] = 'Bossa Nova'
funk['Genero'] = 'Funk'
gospel['Genero'] = 'Gospel'
sertanejo['Genero'] = 'Sertanejo'

#lista de datasets
datasets = [bossa,funk,gospel,sertanejo]

lyrics = pd.concat(datasets)

print(lyrics)

# É preciso usar reset_index para que os indexes sejam ajustados ao novo conjunto
lyrics.reset_index(drop=True,inplace=True)
#stopwords.words('portuguese')

print(processamento_texto(lyrics))