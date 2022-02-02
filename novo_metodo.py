# -*- coding: utf-8 -*-
from preprocess import utils
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import string

fake =[]
for i in range(1,11):
    with open('testes\\fake'+str(i) + '.txt',encoding='utf8') as f:
        fake.append(f.read())

p = utils.preprocessor()

#print(p.removePonctuation("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
#print(p.removeNumbers("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
#print(p.removeStopWords("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
#print(p.lemmatize("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
#print(p.prep("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))

lista = []
for text in fake:
    text = p.prep(text)
    for word in text.split():  
        lista.append(word)
#print(lista)

listapd = pd.Series(lista)
#print(listapd)

#substring = "bolsonaro"
#qntpalavra = lista.count(substring)
#print(qntpalavra)

substring = []
qntpalavra = []
for word in lista:
    substring = word
    qntpalavra.append(lista.count(substring))
    #print(qntpalavra)

data = {'palavras': listapd, 'quantidade': qntpalavra}

df = pd.DataFrame(data, columns=['palavras','quantidade'])

#print(data['quantidade'])
print(df)

#exportando dados para Excel
#file_name = 'relacao_palavras.xlsx'
#df.to_excel(file_name)