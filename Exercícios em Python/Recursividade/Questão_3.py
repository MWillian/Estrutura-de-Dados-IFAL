# 3. Escreva uma função recursiva que determine quantas vezes uma letra K ocorre em uma Palavra P. Por exemplo, a letra 'u'
# ocorre 2 vezes em "estrutura"

def LetraRecorrente(letra,palavra):
    if len(palavra) == 0: 
        return 0
    else:
        if letra == palavra[0]:
            return 1 + LetraRecorrente(letra,palavra[1:])
        else:
            return LetraRecorrente(letra,palavra[1:])
letra1 = "a"
nome = "banana"
print(LetraRecorrente(letra1,nome))