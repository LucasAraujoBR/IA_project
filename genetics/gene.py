from resultado import funcao_resultado
from typing import Union, Callable
from abc import ABCMeta, abstractmethod
from genetics.operator import Operator

class Gene(metaclass=ABCMeta):

    @abstractmethod
    def evaluate(self, gene_index, eval_matrix, data_matrix, targets) -> float:
        raise NotImplementedError()
    
    @abstractmethod
    def pretty_string(self) -> str:
        raise NotImplementedError()

class VariableGene(Gene):
    def __init__(self, index: int, is_feature=True):
        self.index = index
        self.is_feature = is_feature

    def evaluate(self, gene_index, eval_matrix, data_matrix, targets, trained) -> float:
        """
        Este método modificará o eval_matrix neste índice de gene para cada exemplo no data_matrix.
        """

        num_examples = eval_matrix.shape[1]
        lyric_partition = []
        pop_partitions = []
        for example_index in range(0, num_examples):
            pop_partition = [""]
            letra = list(data_matrix[example_index, 0])
            if self.is_feature:
                pop_partition.append(letra.pop(self.index))
            pop_partitions.append(pop_partition)
            lyric_partition.append(' '.join(letra))
        result, acertos = funcao_resultado(lyric_partition, trained[0], trained[2], trained[1], trained[3])  # Definirá o Gênero

        for example_index in range(0, num_examples):
            eval_matrix[gene_index, example_index] = (pop_partition[example_index], result[example_index])
        return 1 - acertos

    def __str__(self):
        return "VariableGene({}, is_feature={})".format(self.index, self.is_feature)

    def pretty_string(self) -> str:
        if self.is_feature:
            return "FEATURES[{}]".format(self.index)
        else:
            return "NOT_FEATURES[{}]".format(self.index)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other) -> bool:
        if other is None or not isinstance(other, VariableGene):
            return False
        return self.index == other.index and self.is_feature == other.is_feature

class OperatorGene(Gene):
    def __init__(self, operation: Union[Callable, Operator], address1: int, address2: int):
        self.operation = operation
        # Esse indice será para a eval_matrix e de acordo com as operações que criaremos nós n precisaremos de 2 endereços mas só de 1
        self.address1 = address1
        self.address2 = address2
        

    def evaluate(self, gene_index, eval_matrix, data_matrix, targets, trained) -> float:
        """
        Este método modificará o eval_matrix neste índice de gene para cada exemplo no data_matrix.
        """

        num_examples = eval_matrix.shape[1]
        lyric_partition = []
        pop_partitions = []
        for example_index in range(0, num_examples):
            # Aplicando na Operação o valor contido no endereço passado
            eval_address1 = eval_matrix[self.address1][example_index]
            eval_address2 = eval_matrix[self.address2][example_index]
            letra = list(data_matrix['lyric'][example_index])
            pop_partition = [""]
            for i in range(len(eval_address1[0])):
                if letra.count(eval_address1[i]):
                    pop_partition.append(letra.pop(eval_address1[i]))
            for i in range(len(eval_address2[0])):
                if letra.count(eval_address1[i]):
                    pop_partition.append(letra.pop(eval_address1[i]))
            pop_partitions.append(pop_partition)
            lyric_partition.append(self.operation(' '.join(letra)))
        result, acertos = funcao_resultado(lyric_partition, trained[0], trained[2], trained[1], trained[3])  # Definirá o Gênero
        for example_index in range(0, num_examples):
            eval_matrix[gene_index, example_index] = (pop_partition[example_index], result[example_index])
        return 1 - acertos 

    def __str__(self):
        return "OperatorGene({}, {}, {})".format(self.operation, self.address1, self.address2)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if other is None or not isinstance(other, OperatorGene):
            return False
        return isinstance(self.operation, type(other.operation)) and self.address1 == other.address1 and self.address2 == other.address2

    def pretty_string(self) -> str:
        return "{}(PROGRAM[{}], PROGRAM[{}])".format(self.operation.function_name(), self.address1, self.address2)
