# 9. O MDC de dois números inteiros é o maior número inteiro que divide ambos sem deixar resto. O MDC pode ser calculado
# através do algoritmo de Euclides. Abaixo uma função iterativa que calcula o MDC. Reescreva a função abaixo de forma
# recursiva.

# def MDC(a, b):
# while (b != 0):
# r = a % b
# a = b
# b = r
# return a

def MDC(a,b):
    if b==0:
        return a
    else:
        r = a % b
        a = b
        b = r
    return MDC(a,b)

print(MDC(15,10))