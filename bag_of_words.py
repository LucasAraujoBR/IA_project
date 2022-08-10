from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer

def bag_words(lista):
    tfidfconverter = TfidfTransformer()
    vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
    x = vectorizer.fit_transform(lista).toarray()
    x_x = tfidfconverter.fit_transform(x).toarray()
    return x_x