# -*- coding: utf-8 -*-
from preprocess import utils

fake =[]
for i in range(1,4):
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
print(lista)