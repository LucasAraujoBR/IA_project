from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score



def funcao_resultado(func,lyric_train,label_train,lyric_test,label_test):
    #Chama a função de limpeza, usa a tfidf para classicar as palavras importantes e aplica o alg svc
    pipelineSVC = Pipeline([('bow',CountVectorizer(analyzer=func)),('tfidf',TfidfTransformer()),('svc',SVC())])

    pipelineSVC.fit(lyric_train,label_train)

    #predição 
    predictions = pipelineSVC.predict(lyric_test)
    print(classification_report(label_test,predictions))
    
    return predictions, accuracy_score(label_test, predictions)