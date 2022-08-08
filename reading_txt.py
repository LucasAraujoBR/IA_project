import os


def escreve_no_txt(name, content):
    cur_path = os.path.dirname(__file__)
    arquivo = open(
        f"{cur_path}\\lyrics\\{name}", "a"
    )
    texto = str(content)
    arquivo.writelines(texto + "\n")
    arquivo.close()


def clear_txt(name):
    cur_path = os.path.dirname(__file__)
    f = open(
        f"{cur_path}\\lyrics\\{name}", "w"
    )
    f.close()


def leitura_txt(name):
    cur_path = os.path.dirname(__file__)
    lista_arq = []
    with open(
        f"{cur_path}\\lyrics\\{name}"
    ,encoding="utf8") as f:
        for line in f:
            x = line.strip()
            lista_arq.append(x)
    return lista_arq


def archive_lyrics():
    cur_path = os.path.dirname(__file__)
    lista_arquivos = [
        arquivo
        for arquivo in os.listdir(f"{cur_path}/lyrics/")
        if arquivo.endswith(".txt")
    ]
    return lista_arquivos


def data_formated():
    lista = archive_lyrics()
    lista_result = []
    for count in range(len(lista)):
        lista_result.append(leitura_txt(lista[count]))
    return lista_result