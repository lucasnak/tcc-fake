from asyncio.format_helpers import _format_callback_source
from preprocess import utils

p = utils.preprocessor()

fake = ["teste de frase sem imaginação", "gosto de fazer tcc"]
print(fake)

listaf = []
aux = []
for text in fake:
    aux.append(p.prep(text))
    print(aux)
    listaf.append(aux)
        
print(listaf)

#listaf = []
#for text in fake:
#    text = p.prep(text)
#    for word in text.split():  
#        listaf.append(word)


#for i in listaf[0]:
#    print(i)

