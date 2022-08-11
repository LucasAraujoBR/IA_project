import numpy as np
from genetics.population import Population


class MEPModel:
    def __init__(self, num_constants: int, constants_min: float, constants_max: float,
                 feature_variables_probability: float, code_length: int, population_size: int,
                 operators_probability: float, num_generations: int):

        self.num_constants = num_constants
        self.constants_min = constants_min
        self.constants_max = constants_max
        self.feature_variables_probability = feature_variables_probability
        self.code_length = code_length
        self.population_size = population_size
        self.operators_probability = operators_probability
        self.num_generations = num_generations

        self.best_chromosome = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        population = Population(X, y, self.num_constants,
                                self.constants_min, self.constants_max,
                                self.feature_variables_probability,
                                self.code_length, self.population_size,
                                self.operators_probability)

        population.initialize()

        for generation in range(self.num_generations):
            self.best_chromosome = population.chromosomes[0]
            if self.best_chromosome.error == 0:
                break
            population.next_generation()

        self.best_chromosome.prune()

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.best_chromosome.predict(X)

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        y_pred = self.predict(X)
        u = ((y - y_pred) ** 2).sum()
        v = ((y - y.mean()) ** 2).sum()

        return 1 - u/v

    def to_python(self):
        if self.best_chromosome is None:
            raise ValueError("The model hasn't been fit.")

        return self.best_chromosome.to_python()
