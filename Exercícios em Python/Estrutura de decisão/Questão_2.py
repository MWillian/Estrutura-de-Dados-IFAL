# 2. Faça um Programa que leia três números e mostre o maior e o menor deles.

maior = 0
menor = 0
cont = True

for i in range(1,4):
    numero = int(input(f"Digite o {i}º número: "))
    while cont:
        menor = numero
        maior = numero
        cont = False
    if numero < maior:
        menor = numero
    elif numero > maior:
        maior = numero
print(f"O maior número digitado é {maior}.\nO menor número digitado é {menor}")

