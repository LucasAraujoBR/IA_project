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