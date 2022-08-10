from reading_txt import data_formated
from data_pre_processing import data_pre_processing
from bag_of_words import bag_words
##Return lis content lyrics
#data_formated()
#print(len(data_formated()))

print(bag_words(data_pre_processing(data_formated())))



