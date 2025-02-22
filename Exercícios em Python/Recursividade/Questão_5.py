# 5. Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em
# ordem decrescente.

def OrdemDecrescente (numero):
    if numero < 0:
        return "Valor negativo"
    else:
        OrdemDecrescente(numero - 1)
        return print(numero)

print(OrdemDecrescente(5))