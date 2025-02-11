# 5. Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for i in range(5):
    numero = float(input("Digite um número: "))
    soma += numero
print(f"A média dos valores digitados é: {soma/5}")
