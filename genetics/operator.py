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
        return re.sub(r'\W', ' ', str(args[0]))
    
    def function_name(self):
        return "Substituição de Char Especial"
    
    def function_python_definition(self):
        return """
def reSubEspecialChar(lyric):
    return re.sub(r'\W', ' ', str(lyric))
    """
