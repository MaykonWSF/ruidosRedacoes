import random
import re

# Adiciona ruídos que são considerados desvios de convenções da escrita
def adicionar_ruido_convencoes_paragrafos(paragrafos, num_palavras_ruidosas):
   
    def distribuir_ruidos(num_palavras_ruidosas, num_paragrafos):
        distribuicao = [num_palavras_ruidosas // num_paragrafos] * num_paragrafos
        for i in range(num_palavras_ruidosas % num_paragrafos):
            distribuicao[i] += 1 
        random.shuffle(distribuicao) 
        return distribuicao
    
    distribuicao_ruidos = distribuir_ruidos(num_palavras_ruidosas, len(paragrafos))
    
    paragrafos_com_ruido = [adicionar_ruido_convencoes(paragrafo, distribuicao_ruidos[i]) for i, paragrafo in enumerate(paragrafos)]
    return paragrafos_com_ruido

def adicionar_ruido_convencoes(texto, num_palavras_ruidosas):
    palavras = texto.split()
    palavras_alteradas = set() 
    tentativas_testadas = set()
    
    while len(palavras_alteradas) < min(num_palavras_ruidosas, len(palavras)):
        if len(tentativas_testadas) == len(palavras):
            break 
        
        indice = random.choice(range(len(palavras)))
        if indice in tentativas_testadas:
            continue 
        
        tentativas_testadas.add(indice)  
        palavra_original = palavras[indice]
        palavra_modificada = aplicar_ruido(palavra_original)
        
        if palavra_modificada != palavra_original:
            palavras[indice] = palavra_modificada
            palavras_alteradas.add(indice)
    
    #Mostrar palavras alteradas
    palavras_alteradas = [palavras[i] for i in palavras_alteradas]
    print("Palavras alteradas:", palavras_alteradas)

    return ' '.join(palavras)

def aplicar_ruido(palavra):
    opcoes_ruido = ['acento', 'capitalizacao', 'hifen']
    for escolha in opcoes_ruido:
        if escolha == 'acento' and tem_acento(palavra):
            return remover_acentos(palavra)
        elif escolha == 'capitalizacao' and tem_maiuscula(palavra):
            return introduzir_erro_capitalizacao(palavra)
        elif escolha == 'hifen' and tem_hifen(palavra):
            return lidar_com_hifen(palavra)
    return palavra

def tem_acento(palavra):
    return bool(re.search(r'[À-ÿ]', palavra))

def tem_maiuscula(palavra):
    return any(char.isupper() for char in palavra)

def tem_hifen(palavra):
    return '-' in palavra

def remover_acentos(palavra):
    substituicoes_acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 
                             'â': 'a', 'ê': 'e', 'ô': 'o', 'ã': 'a', 'õ': 'o', 
                             'ç': 'c', 'à': 'a'}
    for acentuada, sem_acento in substituicoes_acentos.items():
        palavra = palavra.replace(acentuada, sem_acento).replace(acentuada.upper(), sem_acento.upper())
    return palavra

def introduzir_erro_capitalizacao(palavra):
    return ''.join([char.lower() if char.isupper() else char for char in palavra])

def lidar_com_hifen(palavra):
    return palavra.replace('-', ' ')