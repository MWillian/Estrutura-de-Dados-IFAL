# 4. Faça um programa que leia 5 números e informe o maior número.

maior = 0
cont = True
for i in range(1,6):
    numero = float(input(f"Digite o {i}º número: "))
    while cont:
        maior = numero
        cont = False
    if numero > maior:
        maior = numero
print(f"O maior número digitado foi: {maior}")