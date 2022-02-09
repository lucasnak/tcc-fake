from ast import Index
from operator import index
from novometodoV3 import *


#1 - implementar em novo método.py
    # - Soma das quantidades de palavras iguais entre a lista de true e fake
    # Ex:   Palavras    #True   #Fake   #peso
    #       presidente   1000    1300   -300


# -  Importar do novo método o dataframe de palavras e peso

# -  Associar cada palavra ao seu índice para que quando o código análise a notícia de treino e teste, haja identificação entre palavra e peso


tabela = palavras_pesos(listafpd, qntpalavraf, listatpd, qntpalavrat)

pontuacao_true = 0
n_cromossomos = 100
n_geracoes = 100


#Criação da População

#def individual(n_de_itens):
#    """Cria um membro da populacao"""
#    return [ getrandbits(1) for x in range(n_de_itens) ]

#def population(n_de_individuos, n_de_itens):
#    """"Cria a populacao"""
#    return [ individual(n_de_itens) for x in range(n_de_individuos)


#individuo = tabela.index.isin([0,1,2,3,4,5,6,7,8,9,10])
#individuo = tabela.drop(index=3)

cond = (tabela.quantidade > 6)
melhores_palavras_true = tabela[cond]

cond = (tabela.quantidade < -6)
melhores_palavras_fake = tabela[cond]

melhores_palavras = pd.merge(melhores_palavras_true,melhores_palavras_fake, how='outer')


#Somar melhores palavras iguais para formação dos pesos
melhores_palavras_agrupadas = melhores_palavras.groupby('palavras').sum()
melhores_palavras_agrupadas_ordenadas = melhores_palavras_agrupadas.sort_values("quantidade",ascending=False)


individuo = melhores_palavras_agrupadas_ordenadas['quantidade'].tolist()

print(melhores_palavras_agrupadas_ordenadas)
print(individuo)
