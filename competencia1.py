import random
import re
import string
from nltk import word_tokenize


class Competencia1:
    
    def __init__(self, text, porcentagem_ruidos):
        self.text = text
        self.palavras = word_tokenize(text, language='portuguese')
        self.porcentagem_ruidos = porcentagem_ruidos
        self.dicionario = {}

    def remove_pontuacao(self):
        # Remove pontuação e caracteres especiais
        self.palavras = [palavra for palavra in self.palavras if palavra not in string.punctuation]

    def indice_palavras(self):
        # Cria um dicionário com as palavras e seus índices
        self.dicionario = {i: palavra for i, palavra in enumerate(self.palavras)}
    
    def adicionar_ruido(self):
        self.remove_pontuacao()
        self.indice_palavras()
        print(self.dicionario)
    
        num_palavras = len(self.dicionario)
        num_palavras_ruidosas = num_palavras * self.porcentagem_ruidos // 100

        indices_ruidosos = random.sample(list(self.dicionario.keys()), num_palavras_ruidosas)
        print(indices_ruidosos)
                                                                                                                                                                                                                                                    
        # Adiciona ruído às palavras selecionadas
        # palavras = [Competencia1.aplicar_ruido(dicinario[indice]) for indice in indices_ruidosos]
        for indice in indices_ruidosos:
            Competencia1.aplicar_ruido(self.dicionario, indice)
        print(self.dicionario)

    @staticmethod
    def aplicar_ruido(dicionario, indice):
        if Competencia1.tem_acento(dicionario[indice]):
            Competencia1.remover_acentos(dicionario, indice)
        elif Competencia1.tem_maiuscula(dicionario[indice]):
            Competencia1.introduzir_erro_capitalizacao(dicionario, indice)
        elif Competencia1.tem_hifen(dicionario[indice]):
            Competencia1.lidar_com_hifen(dicionario, indice)
        
    
    @staticmethod
    def tem_acento(palavra):
        return bool(re.search(r'[À-ÿ]', palavra))
    
    @staticmethod
    def tem_maiuscula(palavra):
        return any(char.isupper() for char in palavra)
    
    @staticmethod
    def tem_hifen(palavra):
        return '-' in palavra
    
    @staticmethod
    def remover_acentos(dicionario, indice):
        substituicoes_acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 
                                'â': 'a', 'ê': 'e', 'ô': 'o', 'ã': 'a', 'õ': 'o', 
                                'ç': 'c', 'à': 'a'}
        for acentuada, sem_acento in substituicoes_acentos.items():
            dicionario[indice] = dicionario[indice].replace(acentuada, sem_acento).replace(acentuada.upper(), sem_acento.upper())
        
    @staticmethod
    def introduzir_erro_capitalizacao(dicionario, indice):
        for char in dicionario[indice]:
            if char.isupper():
                dicionario[indice] = dicionario[indice].replace(char, char.lower())

    @staticmethod
    def lidar_com_hifen(dicionario, indice):
        dicionario[indice] = dicionario[indice].replace('-', ' ')