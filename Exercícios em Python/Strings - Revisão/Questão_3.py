# Escreva uma função que recebe uma string e imprime somente a última palavra da mesma. Exemplo: Se a string digitada
# for "José da Silva", deverá ser impresso na tela a substring "Silva".

def UltimaString(palavra):
    cont = 0
    quantidadeLetras = 0
    stringFinal = ""
    for i in range(0,len(palavra)):
        quantidadeLetras += 1
        if palavra[i] == " ":
            cont = quantidadeLetras
    for cont in range(cont,len(palavra)):
        stringFinal += palavra[cont]
    print(stringFinal)
frase = input("Digite sua frase: ")
UltimaString(frase)