# 7. Escreva uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número. O
# fatorial duplo é definido como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N.
# Assim, o fatorial duplo de 5 é 5!! == 1 * 3 * 5 = 15

def FatorialDuplo(n):
    if n <= 0:
        return False
    if n == 1:
        return 1
    if n % 2 != 0:
        return n * FatorialDuplo(n-2)
    else:
        return(FatorialDuplo(n-1))
print(FatorialDuplo(8))