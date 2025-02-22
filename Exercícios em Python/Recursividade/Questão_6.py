# 6. Escreva uma função recursiva que calcule o Nésimo 10 termo da sequencia de Fibonacci. A sequência de Fibonacci é
# 0,1, 1, 2, 3, 5, 8, 13, 21,...

def Fibonnaci (n):
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        return Fibonnaci(n-1) + Fibonnaci(n-2)
print(Fibonnaci(7))