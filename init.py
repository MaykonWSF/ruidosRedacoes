import pandas as pd
import os
from competencia1 import *

corpusTeste = pd.read_csv('project\\splits\\testing.csv', converters={'essay': eval, 'competence': eval})

def get_essay(index):
    return corpusTeste['essay'][index]

def ruidos_convencao_escrita(index, num_palavras_ruidosas):

    paragrafos = get_essay(index)
    print("Redação original:")
    for paragrafo in paragrafos:
        print("     ",paragrafo)

    print("\nRedação com ruído:")
    paragrafos_com_ruido = adicionar_ruido_convencoes_paragrafos(paragrafos, num_palavras_ruidosas)
    for paragrafo_ruidoso in paragrafos_com_ruido:
        print("     ",paragrafo_ruidoso)

# Teste
ruidos_convencao_escrita(1, 10)