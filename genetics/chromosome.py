import numpy as np
from collections import deque
from genetics.gene import Gene, VariableGene, OperatorGene
from genetics.operator import AdditionOperator, MultiplicationOperator, SubtractionOperator, DivisionOperator, MinOperator, MaxOperator
from random import random, randint, choice


class Chromosome:
    # valid operators
    operators_family = [operadores]

    def __init__(self, genes):
        self.genes = genes
        self.error = float('inf')
        self.best_gene_index = -1

    @classmethod
    def generate_random_chromosome(cls, constants_prob, feature_variable_prob, num_variables, num_genes, operators_prob):
        genes = []
        sum_prob = constants_prob + feature_variable_prob
        if random() * sum_prob <= feature_variable_prob:
            genes.append(VariableGene(randint(0, num_variables - 1), is_feature=True))
        else:
            genes.append(VariableGene(randint(0, num_variables - 1), is_feature=False))
        
        for gene_index in range(1, num_genes):
            prob = random()
            if prob <= operators_prob:
                genes.append(OperatorGene(choice(Chromosome.operators_family)(),
                                          randint(0, gene_index - 1), randint(0, gene_index - 1)))
            elif prob <= operators_prob + feature_variable_prob:
                genes.append(VariableGene(randint(0, num_variables - 1), is_feature=True))
            else:
                genes.append(VariableGene(randint(0, num_variables - 1), is_feature=False))

        # construct and return the chromosome
        return Chromosome(genes)

    def evaluate(self, data_matrix, targets):
        # Quantidade de músicas
        num_examples = data_matrix.shape[0]
        
        #       Musicas (coluna)  
        # Genes
        #(linha)
        eval_matrix = np.zeros((len(self.genes), num_examples))
        for gene_index, gene in enumerate(self.genes):
            error = gene.evaluate(gene_index, eval_matrix, data_matrix, targets)
            if error < self.error:
                self.error = error
                self.best_gene_index = gene_index

    def predict(self, data_matrix):
        num_examples = data_matrix.shape[0]
        eval_matrix = np.zeros((len(self.genes), num_examples))
        dummy_targets = [0] * num_examples
        for gene_index, gene in enumerate(self.genes):
            gene.evaluate(gene_index, eval_matrix, data_matrix,  dummy_targets)
            if self.best_gene_index == gene_index:
                return eval_matrix[gene_index, :]  # Retorna os resultados do melhor Gene

    def mutate(self, gene_mutation_prob, constants_prob, feature_variable_prob, num_feature_variables, num_genes, operators_prob):
        random_chromosome = Chromosome.generate_random_chromosome(constants_prob,
                                                                  feature_variable_prob,
                                                                  num_feature_variables, num_genes,
                                                                  operators_prob)
        for gene_index in range(len(self.genes)):
            if random() <= gene_mutation_prob:
                self.genes[gene_index] = random_chromosome.genes[gene_index]

    def __str__(self):
        return "Chromosome({}, {})".format(self.genes, self.constants)

    def pretty_string(self, stop_at_best=True):
        program = "CONSTANTS = [{}]\n".format(",".join([str(c) for c in self.constants]))

        for gene_index, gene in enumerate(self.genes):
            program += "{}:{}\n".format(gene_index, gene.pretty_string())
            if self.best_gene_index == gene_index and stop_at_best:
                return program

        return program

    def prune(self):
        gene_indices_in_use = set()
        visited = set()

        genes_indices_to_visit = deque()
        genes_indices_to_visit.appendleft(self.best_gene_index)
        gene_indices_in_use.add(self.best_gene_index)

        while len(genes_indices_to_visit) > 0:
            gene_index = genes_indices_to_visit.pop()
            visited.add(gene_index)
            gene = self.genes[gene_index]
            if isinstance(gene, OperatorGene):
                genes_indices_to_visit.appendleft(gene.address1)
                genes_indices_to_visit.appendleft(gene.address2)
                gene_indices_in_use.add(gene.address1)
                gene_indices_in_use.add(gene.address2)
        # Agora removeremos os Genes que não estão sendo utilizados
        gene_indices_in_use = list(gene_indices_in_use)
        gene_indices_in_use.sort()
        self.genes = [self.genes[i] for i in gene_indices_in_use]

        # TODO: This could be done in the list comprehension but it is clearer to just do another pass
        # re-map the address to the new index
        for gene in self.genes:
            if isinstance(gene, OperatorGene):
                gene.address1 = gene_indices_in_use.index(gene.address1)
                gene.address2 = gene_indices_in_use.index(gene.address2)
        self.best_gene_index = len(self.genes) - 1

    def to_python(self):
        python_program = """
import sys

# define operator/functions
{}

if __name__ == "__main__":
    # now the genes
    {}

    # print out the final answer
    {}
    """
        # define all the function/operators
        operator_def_str = "\n".join([operator().function_python_definition() for operator in self.operators_family])

        # genes
        genes_str = "program = [0] * {}\n".format(len(self.genes))
        for gene_index, gene in enumerate(self.genes):
            genes_str += "    program[{}] = ".format(gene_index)
            if isinstance(gene, VariableGene):
                genes_str += "float(sys.argv[{}])".format(gene.index + 1)
            elif isinstance(gene, OperatorGene):
                genes_str += "{}(program[{}], program[{}])".format(gene.operation.function_name(),
                                                                   gene.address1, gene.address2)
            genes_str += "\n"

        # print statement
        python_program = python_program.format(operator_def_str, genes_str,
                                               "print(program[{}])".format(len(self.genes)-1))

        # return it
        return python_program

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.error < other.error
