# 1. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
media = 0
for i in range(1,5):
    nota = int(input(f"Digite a {i}ª nota: "))
    media += nota
print(media/i)
