# Escreva uma função recursiva que calcule e retorne o fatorial de um número inteiro N. Fat(4) = 4 * 3 * 2 * 1


def Fatorial (numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero*Fatorial(numero-1)

print(Fatorial(4))
