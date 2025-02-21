# Os editores de texto possuem um recurso que permite o usuário substituir uma palavra de um texto por outra palavra.
# Escreva um programa que realize esta ação numa frase dada.

texto1 = "Opa, como vocês estão ?"
palavraNova = input("Qual palavra você deseja substituir ? ")
palavraNova2 = input("Por qual palavra ? ")

def SubstituiçãoTextual(texto,novaPalavra,novaPalavra2):
    listaPalavras = []
    palavra = ""
    for letra in texto:
        if letra == " ":
                listaPalavras.append(palavra)
                palavra = ""
        else:
            palavra += letra
    if palavra != "":
        listaPalavras.append(palavra)
    
    for i in range(0,len(listaPalavras)):
        if listaPalavras[i] == palavraNova2:
            listaPalavras[i] = ""
            for j in palavraNova2:
                listaPalavras[i] += j
    return listaPalavras


print(SubstituiçãoTextual(texto1,palavraNova,palavraNova2))