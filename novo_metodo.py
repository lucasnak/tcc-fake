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


#Leitura das notícias fakes e adicionando essas notícias em uma lista - lista de notícias
fake =[]
for i in range(1,3603):
    with open('Corpus-alternativo\\fake\\'+str(i)+'.txt',encoding='utf8') as f:
        fake.append(f.read())

#Texto recebe o preprocessamento do utils - fakenilc e cada palavra de cada texto se torna um item da lista "lista"
p = utils.preprocessor()
lista = []
for text in fake:
    text = p.prep(text)
    for word in text.split():  
        lista.append(word)
#print(lista)


#A Biblioteca String possuí o atributo .count que conta quantas vezes a "substring" aparece na lista "lista"
substring = []
qntpalavra = []
for word in lista:
    substring = word
    qntpalavra.append(lista.count(substring))
    #print(qntpalavra)

#"Lista" é convertida em uma série do Pandas 
listapd = pd.Series(lista)

data = {'palavras': listapd, 'quantidade': qntpalavra}

df = pd.DataFrame(data, columns=['palavras','quantidade'])

#printando a tabela de palavras 
print(df)

#exportando dados para Excel
#file_name = 'relacao_palavras_3602.xlsx'
#df.to_excel(file_name)