from --- import novo_metodov2


#1 - implementar em novo método.py
    # - Soma das quantidades de palavras iguais entre a lista de true e fake
    # Ex:   Palavras    #True   #Fake   #peso
    #       presidente   1000    1300   -300


# -  Importar do novo método o dataframe de palavras e peso

# -  Associar cada palavra ao seu índice para que quando o código análise a notícia de treino e teste, haja identificação entre palavra e peso


palavras_pesos = biblioteca_palavras_pesos

pontuacao_true = 0
n_cromossomos = 100
n_geracoes = 100

#Criação da População

def individual(n_de_itens):
    """Cria um membro da populacao"""
    return [ getrandbits(1) for x in range(n_de_itens) ]

def population(n_de_individuos, n_de_itens):
    """"Cria a populacao"""
    return [ individual(n_de_itens) for x in range(n_de_individuos)


def individuo(n_cromossomos):
    "Cria a população"
    return [pesos]

