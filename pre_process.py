##pre processamento das letras musicais 
import numpy as np
import pandas as pd

#Leitura dos datasets
bossa = pd.read_csv('datasets/bossa_nova.csv')
funk = pd.read_csv('datasets/funk.csv')
gospel = pd.read_csv('datasets/gospel.csv')
sertanejo = pd.read_csv('datasets/sertanejo.csv')

# rap = pd.read_csv('datasets/drake_data.csv')
#all_bossa_nova =  pd.read_csv('datasets/bossa_nova_songs_dataset.csv')
# rock_country_reb =  pd.read_csv('datasets/rock_country_R&B.csv')
# songs =  pd.read_csv('datasets/songs_normalize.csv')



# rap_lyrics = pd.DataFrame(rap['lyrics'])  #OK
# rap_lyrics.rename(columns={'lyrics': 'lyric'}, inplace = True) #OK

# all_bossa = pd.DataFrame(all_bossa_nova['song_lyrics']) #OK
# all_bossa.rename(columns={'song_lyrics': 'lyric'}, inplace = True) #OK

# rock = pd.DataFrame(rock_country_reb['lyrics'].loc[(rock_country_reb['type'] == 'rock')]) #OK
# rock.rename(columns={'lyrics': 'lyric'}, inplace = True) #OK

# country = pd.DataFrame(rock_country_reb['lyrics'].loc[(rock_country_reb['type'] == 'country')]) #OK
# country.rename(columns={'lyrics': 'lyric'}, inplace = True) #OK

# reb = pd.DataFrame(rock_country_reb['lyrics'].loc[(rock_country_reb['type'] == 'R&B')]) #OK
# reb.rename(columns={'lyrics': 'lyric'}, inplace = True) #OK

##Criando a coluna correspondete ao genero

bossa['gen'] = 'Bossa Nova'
funk['gen'] = 'Funk'
gospel['gen'] = 'Gospel'
sertanejo['gen'] = 'Sertanejo'
# rap_lyrics['gen'] = 'Rap'
#all_bossa['gen'] = 'Bossa Nova'
# rock['gen'] = 'Rock'
# country['gen'] = 'Sertanejo'
# reb['gen'] = 'R&B'

datasets = [bossa,funk,gospel,sertanejo] #,rap_lyrics,,rock,country,reb
lyrics = pd.concat(datasets)
lyrics.reset_index(drop=True,inplace=True)

#rint(lyrics)

#PARTE CLEANIG

#Palavras de parada são as palavras em uma lista de parada que são filtradas
#antes ou depois do processamento de dados de linguagem natural porque são insignificantes
from nltk.corpus import stopwords
#Para remover pontuação
import string


def processamento_texto(txt):
    # remover quebras de linha
    txt = txt.replace('\n',' ')
    # remover símbolos de pontuação, resultando em um array de caracteres
    txt = [char for char in txt if char not in string.punctuation]
    # depois, juntar os caracteres em palavras novamente e separá-los em uma lista de tokens
    txt = ''.join(txt).split()
    # por fim, remover as stopwords da lista
    txt = [word for word in txt if word.lower() not in stopwords.words('portuguese')]
    # and word.lower() not in stopwords.words('english')
    
    return txt


#Separando o conjunto de dados em conjunto de treino e de teste
from sklearn.model_selection import train_test_split
lyric_train,lyric_test,gen_train,gen_test = train_test_split(lyrics['lyric'],lyrics['gen'],test_size=0.4)

#Imports padrão para construção da pipeline de dados
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
pipeline = Pipeline([
    ('bow',CountVectorizer(analyzer=processamento_texto)),
    ('tfidf',TfidfTransformer()),
    ('nb',MultinomialNB())
])

print(pipeline.fit(lyric_train,gen_train))