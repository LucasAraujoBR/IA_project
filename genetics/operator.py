from abc import ABCMeta, abstractmethod
import re

class Operator(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, *args, **kwds):
        """
        Chama a operação e retorna seu resultado
        """
    
    @abstractmethod
    def function_name(self):
        """
        Retorna o nome da função
        """

    @abstractmethod
    def function_python_definition(self):
        """
        Retorna a definição da função em PYTHON
        """
    
    def __str__(self) -> str:
        return self.function_name()
    
    def __repr__(self) -> str:
        return str(self)
<<<<<<< HEAD

class removeTwoLessUsedWordsOperator(Operator):
    def __call__(self, *args, **kwds):
        lyric = str(args[0])
        lyric = re.sub(',', '', lyric)
        words = lyric.lower.split()
        
        return 
    
    def function_name(self):
        return "Substituição de Char Especial"
    
    def function_python_definition(self):
        return """
def reSubEspecialChar(lyric):
    return re.sub(r'\W', ' ', str(lyric))
    """


class reSubEspecialCharOperator(Operator):
    def __call__(self, *args, **kwds):
        return data_pre_processing(args)
    
    def data_pre_processing(X):
        lyrics = []
        
        # Remove all the special characters
        lyrics = re.sub(r'\W', ' ', str(X))
            
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
    
    def function_python_definition(self):
        return """
def reSubEspecialChar(lyric):
    return re.sub(r'\W', ' ', str(lyric))
    """
=======
>>>>>>> b731fc2a3620acb923f769d1e30e7277d9235953
