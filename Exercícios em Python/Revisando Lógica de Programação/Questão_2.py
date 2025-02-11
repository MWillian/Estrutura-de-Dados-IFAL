# Armazena em uma lista todos os múltiplos de 3,entre 1 e 100. Imprima cada elemento da lista, um por linha.
lista = []

for i in range(1,101):
    if i % 3 == 0:
        lista.append(i)
for i in range(len(lista)):
    print(lista[i])