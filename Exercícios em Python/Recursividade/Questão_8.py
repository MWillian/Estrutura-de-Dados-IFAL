# Escreva uma função recursiva que informa se uma String é palíndroma ou não. Um palíndromo é uma string que é lida da
# mesma maneira da esquerda para a direita e da direita para a esquerda. Alguns exemplos de palíndromo são "E até o
# papa poeta é" (se os espaços, pontuação e acentos forem ignorados).

def Palíndroma (string):
    if len(string) <= 1:
        return "A palavra é palíndroma"
    else:
        if string[0] == string[-1]:
            return Palíndroma(string[1:-1])
        else:
            return "A palavra não é palíndroma"
print(Palíndroma("ararab"))