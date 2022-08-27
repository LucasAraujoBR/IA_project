from reading_txt import data_formated
from treino import data_pre_processing
from bag_of_words import bag_words
from train import train
import numpy as np
##Return lis content lyrics

#print(len(data_formated()))

#y generos das musicas 
y = np.array(['Jazz', 'R&B/Soul', 'R&B/Soul', 'Rock', 'Pop','Electronic','Pop','Country','Reggae','Pop',
'Rock','Pop','Rock','Rock'])


#Dados brutos dos txt com as letras retornado em uma lista
data_list = data_formated()

x = []
for count in range(len(data_list)):
    data_adjs = data_pre_processing(data_list[count])
    print(data_adjs)
    bag = bag_words(data_adjs)
    x.append(bag)


print(len(x))
#train(X,y)



