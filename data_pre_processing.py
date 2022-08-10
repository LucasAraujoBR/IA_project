import re


def data_pre_processing(X):
    lyrics = []
    for sen in range(0, len(X)):
        # Remove all the special characters
        lyrics = re.sub(r'\W', ' ', str(X[sen]))
        
        # remove all single characters
        lyrics = re.sub(r'\s+[a-zA-Z]\s+', ' ', lyrics)
        
        # Remove single characters from the start
        lyrics = re.sub(r'\^[a-zA-Z]\s+', ' ', lyrics) 
        
        # Substituting multiple spaces with single space
        lyrics = re.sub(r'\s+', ' ', lyrics, flags=re.I)
        
        # Removing prefixed 'b'
        lyrics = re.sub(r'^b\s+', '', lyrics)
        
        # Converting to Lowercase
        lyrics = lyrics.lower()
        
        # Lemmatization
        lyrics = lyrics.split()

        #lyrics = [stemmer.lemmatize(word) for word in lyrics]
        lyrics_final = ' '.join(lyrics)
        
        lyrics.append(lyrics_final)
    return lyrics