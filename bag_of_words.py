from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords


def bag_words(lista):
    vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
    X = vectorizer.fit_transform(lista).toarray()
    return X