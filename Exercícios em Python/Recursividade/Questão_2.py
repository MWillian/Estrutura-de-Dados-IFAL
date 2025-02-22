# 2. Escreva uma função recursiva que permita inverter uma palavra N. "Python" -->> "nohtyP"

palavra = "Python"
def InversaoPalavra(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + InversaoPalavra(string[:-1])

print(InversaoPalavra(palavra))