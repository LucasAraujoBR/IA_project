import pandas as pd


class DataSet:
    def __init__(self, filename, qtd_particoes):
        self.data = pd.read_csv(filename)
        self.target = "sertanejo"
        self.data_matrix = self.data.values
        lista = []
        for i in range(self.data_matrix.shape[0]):
            palavras = str(self.data_matrix[i, 0]).split()
            print(len(palavras))
            qtd_palavras = len(palavras)
            qtd_palavras_particao = int(int(qtd_palavras) / int(qtd_particoes))
            for x in range(0, qtd_palavras, qtd_palavras_particao):
                lista.append(' '.join(palavras[x:x+qtd_palavras_particao]))
            self.data_matrix[i, 0] = lista