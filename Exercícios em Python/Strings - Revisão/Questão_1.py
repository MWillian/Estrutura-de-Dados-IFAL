# 1. Uma palavra é palíndroma se ela não se altera quando lida da direita para esquerda. Por exemplo, raiar é palíndroma.
# Escreva um programa que verifique se uma palavra dada é palíndroma.

def palindroma(string):
    cont = 0
    for i in range(0,len(string)):
        if string[i] != string[-(i+1)]:
            cont = 1
    if cont == 0:
        print("A palavra é palíndroma.")
    else:
        print("A palavra não é palíndroma.")
palavra = input("Digite a palavra: ")
palindroma(palavra)