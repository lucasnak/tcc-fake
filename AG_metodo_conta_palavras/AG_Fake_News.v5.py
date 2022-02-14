#Área de importações

from ast import Index
from operator import index
from random import randint
from socket import NI_NUMERICHOST
from tkinter.tix import COLUMN
from analisador import *
import numpy as np
import string

#---------------------------- PARÂMETROS DE TUNAGEM------------------------------------------------

# Elementos de avaliação e tunagem----------------------------------------------------------------- 
nota_corte_pesos = 1000
respostas_real =[] # Armazena a informação se a notícia a ser classificada é true ou fake para cálculo de acurácia - Recebe 1 ou 0 dependendo se a notícia que será classificada é true ou fake
n_cromossomos = 100
n_geracoes = 100

# Range de mutação
aum_peso = 100
dim_peso = -100


# ---------------------------CRIAÇÃO DO PRIMEIRO INDIVÍDUO ----------------------------------------


# Importação de todas as palavras analisadas ------------------------------------------------------
tabela = palavras_pesos(listafpd, qntpalavraf, listatpd, qntpalavrat) # Importa do analisador as palavras com seus pesos (palavras_pesos é um def do outro arquivo)

# Seleção das melhores palavras com base no peso que cada palavra recebeu ------------------------- 
cond = (tabela.quantidade > nota_corte_pesos)
melhores_palavras_true = tabela[cond]

cond = (tabela.quantidade < nota_corte_pesos)
melhores_palavras_fake = tabela[cond]

melhores_palavras = pd.merge(melhores_palavras_true,melhores_palavras_fake, how='outer')

melhores_palavras.to_excel('mehores_palavras.xlsx')


# melhores_palavras_agrupadas = melhores_palavras.groupby('palavras').sum() - Está zuando o título da coluna palavra
# print(melhores_palavras_agrupadas)


#--------------------------------------------------------------------------------------------------

# --------------------------------- CRIAÇÃO DA PRIMEIRA GERAÇÃO -----------------------------------
                        # AINDA NÃO ESTÁ NO CÓDIGO - CÓDIGO RODA APENAS COM 1 INDIVÍDUO

mutacao = []
melhores_palavras_np = np.array(melhores_palavras)

for i in range(melhores_palavras):
    mutacao.append(randint(dim_peso,aum_peso))

for i in range(n_cromossomos):
    add_mutacao = np.append(melhores_palavras,mutacao,axis = 1) #Na verdade, preciso de várias lista de melhores palavras com pesos mutados

# -------------------------------------------------------------------------------------------------

#---------------------------------PREPARAÇÃO PARA CLASSIFICAÇÃO------------------------------------

###Transformando cada notícia de teste em uma lista de palavras e colocando essas listas em uma outra lista "notícias"

## Abrindo as notícias para classificação ---------------------------------------------------------

fake =[]
for i in range(3001,3201):
    with open('Corpus-alternativo\\fake\\'+str(i)+'.txt',encoding='utf8') as f:
        fake.append(f.read())
    respostas_real.append(0) #Armazena na variável que essa notícia é de fato fake

true =[]
for i in range(3001,3201):
    with open('Corpus-alternativo\\true\\'+str(i)+'.txt',encoding='utf8') as t:
        true.append(t.read())
    respostas_real.append(1) #Armazena na variável que essa notícia é de fato fake

## Preprocessando as palavras das notícias a serem classificadas e colocando na lista "notícias"
p = utils.preprocessor()

noticias = []
aux = []
for text in fake:
    noticias.append(p.prep(text))
    

for text in true:
    noticias.append(p.prep(text))
    

#--------------------------------------------------------------------------------------------------

# --------------------------------------ETAPA DE CLASSIFICAÇÃO-------------------------------------

# Setando variáveis -------------------------------------------------------------------------------
lista =[]
np_lista =[]
soma = 0
resultados = []

escolhidas = melhores_palavras['palavras'].tolist() # Pegando somente a coluna das palavras em "melhores_palavras"

for noticia in noticias:  # Objetivo é analisar a quantidade de notícias escolhidas para serem classificadas
    soma = 0 # Se ao final da análise feita pelo for, a variável soma for >0, a notiíca é true, caso contrário, fake
    noticia_str = str(noticia)
    print("print das notícias separadas uma a uma")
    print(noticia_str)
    
    #Este for abaixo separa as palavras de cada notícia para serem analisadas e atribuídas um peso mais adiante no código
    for word in noticia_str.split():
        lista.append(word)
        np_lista = np.array(lista)
    print("palavras de cada notícia sendo separadas")
    print (np_lista)
    
    i = 0
    for word in escolhidas: #Para cada notícia, esse for vai rodar cada palavras das melhores_escolhidas e comparar com as palavras que existem em cada notícia           
        comparador = np.where(np_lista == word) #vai procurar se a notícia tem alguma das palavras referência (melhores_escolhidas)
        print('este é comparador')
        print(comparador)
        lista_comparador = list(comparador)
        print('este é lista_comparador')
        print(lista_comparador)
        pos_comparadas = (lista_comparador[0]) # O bloco até aqui mostra em uma lista as posições das palavras nas notícias em que haja uma palavra de referencia
        print('este é pos_comparadas')
        print(pos_comparadas)
        #print(len(pos_comparadas))
        if len(pos_comparadas) != 0: # Só entra no if se exite pelo menos uma palavra de referência na notícia 
            indice = melhores_palavras.index[melhores_palavras['palavras'] == word]
            print(indice)
            numero = melhores_palavras.loc[indice,'quantidade'] # mpao[] ==word encontra a palavra analisada no df das palavras de referencia. mpao. index acha a posisão dessa palavra no df mpao e mpao.loc encontra o valor "quantidade na posisão da palavra"
            print(numero)
            numero_num = int(numero)
            soma = soma + numero_num
    resultados.append(soma) 
print(resultados)

# Armazena as respostas que o individuo deu para as notícias depois de analisá-las
respostas =[]
for resultado in resultados:
    if resultado > 0:
        respostas.append(1)
    
    else:
        respostas.append(0)
# -------------------------------------------------------------------------------------------------       

# ---------------------------------- Etapa de avaliação -------------------------------------------

dic_respostas_real = {"Avaliacao": respostas_real}
dic_respostas = {"Avaliacao": respostas}

df_respostas_real = pd.DataFrame(dic_respostas_real)
df_respostas = pd.DataFrame(dic_respostas)

print(df_respostas == df_respostas_real)

total_iguais = np.sum(df_respostas == df_respostas_real)
total = len(df_respostas)
acuracia = total_iguais/total
print(acuracia)

# Resultado da geração

# A ideia é fazer o contador de true e fake ficar o mais próximo possível da contagem real  

# -------------------------------------------------------------------------------------------------
