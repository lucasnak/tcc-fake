from ast import Index
from operator import index
from socket import NI_NUMERICHOST
from tkinter.tix import COLUMN
from novometodoV3 import *
import numpy as np
import string

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


#analisando o df
print(melhores_palavras)

#Somar melhores palavras iguais para formação dos pesos
melhores_palavras_agrupadas = melhores_palavras.groupby('palavras').sum()


#analisando o df
print(melhores_palavras_agrupadas)

mpao = melhores_palavras_agrupadas.sort_values("quantidade",ascending=False)


individuo = mpao['quantidade'].tolist()  #mpao = melhores palavras agrupadas ordenadas


#print(individuo)



#Ideia de como codificar o AG

#Objetivo do AG = acertar 1000 notícias como true ou fake
#Quanto mais notícas o AG acertar, melhor é a população e o indivíduo

#O que o AG terá que fazer para atingir esses objetivos:

#Identificar cada palavra preprocessada de uma nóticia específica
#As palavras que ele identificar como críticas, associar o peso delas numa soma
#Se ao final da soma o valor for positivo, o AG classifica a notícia como True, se a soma for negativa, a notícia é fake
#O indivíduo que atingir a maior pontuação é o melhor de todos e um nova geração deve recomeçar com  devida mutação


#Identificar cada palavra preprocessada de uma notícia específica

    # O rol de palavras de teste será as notícias ture e fake de 5201 a 6200

#Identificação das palavras críticas
#print(mpao)


###Transformando cada notícia de teste em uma lista de palavras e colocar essas listas em uma lista "notícias"
## Abrindo as notícias de teste
fake =[]
for i in range(3001,3002):
    with open('Corpus-alternativo\\fake\\'+str(i)+'.txt',encoding='utf8') as f:
        fake.append(f.read())

true =[]
for i in range(3001,3002):
    with open('Corpus-alternativo\\true\\'+str(i)+'.txt',encoding='utf8') as t:
        true.append(t.read())

## Preprocessando as palavras e colocando na lista "notícias"
p = utils.preprocessor()

noticias = []
aux = []
for text in fake:
    aux.append(p.prep(text))
    noticias.append(aux)

for text in true:
    aux.append(p.prep(text))
    noticias.append(aux)

#print(noticias)

#Localização dessas palavras nas notícias teste
lista =[]
listanova =[]
soma = 0

conta_fake = 0
conta_true = 0

escolhidas = melhores_palavras['palavras'].tolist()
for noticia1 in noticias:  #vai analisar as 200 notícias teste
    noticia=str(noticia1)
    for word in noticia.split():
        lista.append(word)
        listanova = np.array(lista)
    print (listanova)
    
    
    for word in escolhidas: #para cada notícia, ele vai rodar cada palavras para as escolhidas como referência           
        aux2 = np.where(listanova == word) #vai procurar a palavra de referência na notícia analisada
        aux3 = list(aux2)
        aux4 = (aux3[0])
        #print(len(aux4))
        if len(aux4) != 0: 
            indice = melhores_palavras.index[melhores_palavras['palavras'] == word]
            print(indice)
            numero = melhores_palavras.loc[indice,'quantidade'] # mpao[] ==word encontra a palavra analisada no df das palavras de referencia. mpao. index acha a posisão dessa palavra no df mpao e mpao.loc encontra o valor "quantidade na posisão da palavra"
            print(numero)
            numero_num = int(numero)
            soma = soma + numero_num 
        print(soma)
    if soma > 0:
        print('notícia verdadeira')
        conta_true = conta_true + 1
    else:
        print('notícia falsa')
        conta_fake = conta_fake + 1


# Resultado da geração

# A ideia é fazer o contador de true e fake ficar o mais próximo possível da contagem real  