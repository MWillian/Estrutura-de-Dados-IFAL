# 4. Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em
# ordem crescente.
valor = 7

def OrdemCrescente(numero):
    if numero < 0:
        return "valor negativo"
    else:
        OrdemCrescente(numero - 1)
        return print(numero) 
print(OrdemCrescente(valor))