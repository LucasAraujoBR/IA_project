import pandas as pd


class DataSet:
    def __init__(self, filename):
        self.data = pd.read_csv(filename)
        self.target = self.data.target.values
        self.data_matrix = self.data.drop("target", 1).values
