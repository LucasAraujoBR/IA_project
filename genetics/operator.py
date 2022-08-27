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
=======


class func1(Operator):
    def __call__(self, *args, **kwds):
        txt = str(args[0])
        return re.sub(r'\n', ' ', txt)
        
    
    def function_name(self):
        return "sub_barra_n"

    def function_python_definition(self):
        return """
def sub_barra_n(letra):
    txt = str(args[0])
    return re.sub(r'\n', ' ', txt)
        """

class func2(Operator):
    def __call__(self, *args, **kwds):
        txt = str(args[0])
        return re.sub(r'\r', ' ', txt)
        
    
    def function_name(self):
        return "sub_barra_r"

    def function_python_definition(self):
        return """
def sub_barra_r(letra):
    txt = str(args[0])
    return re.sub(r'\r', ' ', txt)
        """

class func3(Operator):
    def __call__(self, *args, **kwds):
        txt = str(args[0])
        return re.sub(r'\W', ' ', txt)
        
    
    def function_name(self):
        return "sub_barra_W"

    def function_python_definition(self):
        return """
def sub_barra_W(letra):
    txt = str(args[0])
    return re.sub(r'\W', ' ', txt)
        """

class func4(Operator):
    def __call__(self, *args, **kwds):
        txt = str(args[0])
        return re.sub(r'\s+[a-zA-Z]\s+', ' ', txt)
        
    
    def function_name(self):
        return "sub_barra_all_single_char"

    def function_python_definition(self):
        return """
def sub_barra_all_single_char(letra):
    txt = str(args[0])
        return re.sub(r'\s+[a-zA-Z]\s+', ' ', txt)
        """

class func5(Operator):
    def __call__(self, *args, **kwds):
        txt = str(args[0])
        return re.sub(r'\^[a-zA-Z]\s+', ' ', txt)
        
    
    def function_name(self):
        return "sub_barra_start_single_char"

    def function_python_definition(self):
        return """
def sub_barra_start_single_char(letra):
    txt = str(args[0])
        return re.sub(r'\^[a-zA-Z]\s+', ' ', txt)
        """
>>>>>>> e2a1a78f60c8bc53b6830b148bb7e61899374016
