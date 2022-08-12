import pandas as pd


class DataSet:
    def __init__(self, filename, qtd_particoes):
        self.data = pd.read_csv(filename)
        self.target = self.data.target.values
        self.data_matrix = self.data.drop("target", 1).values
        lista = []
        for i in self.data_matrix.shape[0]:
            palavras = self.data_matrix['lyric'][i].split()
            qtd_palavras = len(palavras)
            qtd_palavras_particao = int(int(qtd_palavras) / int(qtd_particoes))
            for x in range(0, qtd_palavras, qtd_palavras_particao):
                lista.append(' '.join(palavras[x:x+qtd_palavras_particao]))
            self.data_matrix['lyric'][i] = lista