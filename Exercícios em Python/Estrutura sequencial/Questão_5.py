# 5. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = input("Digite seu sexo [Masculino = M, Feminino = F]: ").lower()
altura = float(input("Digite sua altura em metros: "))
if sexo == "m":
    print(f"O peso idel do indivíduo seria: {(73.7 * altura) - 58}")
elif sexo == "f":
    print(f"O peso idel do indivíduo seria:{(62.1 * altura) - 44.7}")