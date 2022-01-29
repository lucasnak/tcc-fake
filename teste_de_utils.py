from preprocess import utils


p = utils.preprocessor()

#print(p.removePonctuation("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
#print(p.removeNumbers("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
#print(p.removeStopWords("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
#print(p.lemmatize("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))
print(p.prep("Jogar bola é o esporte número 1 dos brasileiros! É uma pena que Kátia Abreu tenha vetado a bola no Maracanã"))