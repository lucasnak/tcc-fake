#Importações
# -*- coding: utf-8 -*-
from preprocess import utils
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import string

#Teste do utils - fakenilc modificado
#print(p.removePonctuation("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
#print(p.removeNumbers("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
#print(p.removeStopWords("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
#print(p.lemmatize("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
#print(p.prep("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))


#Leitura das notícias fakes e true e adicionando essas notícias em uma lista - lista de notícias
fake =[]
for i in range(1,6):
    with open('Corpus-alternativo\\fake\\'+str(i)+'.txt',encoding='utf8') as f:
        fake.append(f.read())

true =[]
for i in range(1,6):
    with open('Corpus-alternativo\\true\\'+str(i)+'.txt',encoding='utf8') as t:
        true.append(t.read())


#Texto recebe o preprocessamento do "utils - fakenilc" e cada palavra de cada texto se torna um item da lista "listaf" ou "listat"
p = utils.preprocessor()

listaf = []
for text in fake:
    text = p.prep(text)
    for word in text.split():  
        listaf.append(word)

listat = []
for text in true:
    text = p.prep(text)
    for word in text.split():  
        listat.append(word)


#A Biblioteca String possuí o atributo .count que conta quantas vezes a "substring" aparece na lista "listaf" ou "listat"
#Poderiamos simplesmente transformas as listas acima em df e usar values_counts() que conta quantas vezes um mesmo item aparece na coluna desejada
substringf = []
qntpalavraf = []
for word in listaf:
    substringf = word
    qntpalavraf.append(listaf.count(substringf))
    #print(qntpalavraf)

substringt = []
qntpalavrat = []
for word in listat:
    substringt = word
    qntpalavrat.append(listat.count(substringt))
    #print(qntpalavrat)


#"listaf" e "listat" é convertida em uma série do Pandas 
listafpd = pd.Series(listaf)
listatpd = pd.Series(listat)


#Criando e organizando DataFrames
def palavras_pesos(listafpd, qntpalavraf, listatpd, qntpalavrat):
    dataf = {'palavras': listafpd, 'quantidade': qntpalavraf}
    dff = pd.DataFrame(dataf, columns=['palavras','quantidade'])
    dff_unique = dff.drop_duplicates(subset="palavras")
    dff_unique['quantidade'] = dff_unique['quantidade']*-1 # multiplicação para que as palavras falsas tenham quantidades (pesos) negativas
    dff_ordenado = dff_unique.sort_values("quantidade", ascending=False)


    datat = {'palavras': listatpd, 'quantidade': qntpalavrat}
    dft = pd.DataFrame(datat, columns=['palavras','quantidade'])
    dft_unique = dft.drop_duplicates(subset="palavras")
    dft_ordenado = dft_unique.sort_values("quantidade", ascending=False)

    resultado = pd.merge(dft_ordenado,dff_ordenado, how = 'outer')
    return resultado



#exportando dados para Excel
#file_namef = 'relacao_palavras_f_3602.xlsx'
#dff.to_excel(file_namef)

#file_namet = 'relacao_palavras_t_685.xlsx'
#dft.to_excel(file_namet)

#Soma das palavras das duas listas

#df_total = pd.DataFrame()