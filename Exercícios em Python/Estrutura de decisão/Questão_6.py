# 6. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
# mesma é uma data válida.

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if dia <= 0 or dia > 32:
    print("Valor inválido para o dia!")
else:
    print(f"Dia digitado: {dia}")

if mes <= 0 or mes > 12:
    print("Valor inválido para mês!")
else:
    print(f"Mês digitado: {mes}")

if ano <= 0 or ano > 2025:
    print("Valor inválido para ano!")
else:
    print(f"Ano digitado: {ano}")
print()
print(f"Data informada: {dia}/{mes}/{ano}.")

