# Um dos recursos disponibilizados pelos editores de texto mais modernos é a determinação do número de palavras de um
# texto. Escreva um programa que determine o número de palavras de um texto dado.
def espaco (palavra):
    cont = 1
    for i in range(0,len(palavra)):
        if palavra[i] == " ":
            cont+=1
    print(f"O texto tem {cont} palavras.")

texto = input("Digite o texto: ")
espaco(texto)