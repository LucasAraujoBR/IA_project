from genetics.chromosome import Chromosome
import random
import copy


class Population:
    def __init__(self, data_matrix, targets, feature_variable_prob, num_genes, num_chromosomes, operators_prob):
        # set the variables
        self.data_matrix = data_matrix
        self.targets = targets
        self.constants_prob = 1. - operators_prob - feature_variable_prob
        self.feature_variable_prob = feature_variable_prob
        self.num_feature_variables = len(self.data_matrix['lyric'][0])  # Tem de ter a mesma quantidade de termos dentro de cada lista
        self.num_genes = num_genes
        self.num_chromosomes = num_chromosomes
        self.operators_prob = operators_prob

        # TODO: take in
        self.crossover_prob = 0.9
        self.mutation_prob = 0.1

        # the chromosomes
        self.chromosomes = None

    def initialize(self):
        self.chromosomes = [Chromosome.generate_random_chromosome(self.constants_prob,
                                                                  self.feature_variable_prob,
                                                                  self.num_feature_variables, self.num_genes,
                                                                  self.operators_prob)
                            for _ in range(self.num_chromosomes)]
        
        for chromosome in self.chromosomes:
            chromosome.evaluate(self.data_matrix, self.targets)
        
        self.chromosomes.sort()

    def random_tournament_selection(self, tournament_size):
        best_chromosome = None
        for _ in range(tournament_size):
            chromosome = random.choice(self.chromosomes)
            if best_chromosome is None or chromosome.error < best_chromosome.error:
                best_chromosome = chromosome

        return best_chromosome

    def one_cut_point_crossover(self, parent1, parent2):
        offspring1 = Chromosome([])
        offspring2 = Chromosome([])

        cutting_point = random.randint(0, self.num_genes)
        
        offspring1.genes = parent1.genes[:cutting_point] + parent2.genes[cutting_point:]
        offspring2.genes = parent2.genes[:cutting_point] + parent1.genes[cutting_point:]

        return offspring1, offspring2

    def next_generation(self):
        for _ in range(0, len(self.chromosomes), 2):
            chromosome1 = self.random_tournament_selection(2)
            chromosome2 = self.random_tournament_selection(2)

            if random.random() < self.crossover_prob:
                offspring1, offspring2 = self.one_cut_point_crossover(chromosome1, chromosome2)
            else:
                offspring1 = copy.copy(chromosome1)
                offspring2 = copy.copy(chromosome2)
            
            offspring1.mutate(self.mutation_prob, self.constants_prob,
                              self.feature_variable_prob,
                              self.num_feature_variables, self.num_genes,
                              self.operators_prob)
            offspring1.evaluate(self.data_matrix, self.targets)
            offspring2.mutate(self.mutation_prob, self.constants_prob,
                              self.feature_variable_prob,
                              self.num_feature_variables, self.num_genes,
                              self.operators_prob)
            offspring2.evaluate(self.data_matrix, self.targets)

            insert_index = -1

            for chromosome_index, chromosome in enumerate(self.chromosomes):
                if offspring1.error < chromosome.error:
                    insert_index = chromosome_index
                    break

            if insert_index > -1:
                self.chromosomes[insert_index] = offspring1

            insert_index = -1

            for chromosome_index, chromosome in enumerate(self.chromosomes):
                if offspring2.error < chromosome.error:
                    insert_index = chromosome_index
                    break

            if insert_index > -1:
                self.chromosomes[insert_index] = offspring2
