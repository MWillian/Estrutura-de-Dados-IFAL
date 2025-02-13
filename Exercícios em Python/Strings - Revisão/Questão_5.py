# 5. As normas para a exibição da bibliografia de um artigo científico, de uma monografia, de um livro texto, etc., exigem que o
# nome do autor seja escrito no formato último sobrenome, sequência das primeiras letras do nome e dos demais
# sobrenomes, seguidas de ponto final. Por exemplo, Antônio Carlos Jobim seria referido por Jobim, A. C.. Escreva um
# programa que receba um nome e o escreva no formato de bibliografia.

def NomeArtigo(palavra):
   nomeSeparado = SeparadorNomes(palavra) 
   ultimoNome = nomeSeparado[-1] + ", "
   nomeFinal = ultimoNome + PegarIniciaisMaiuscula(nomeSeparado)
   return nomeFinal

def SeparadorNomes(nomeCompleto):
    arrayString = []
    palavra = ""
    for letra in nomeCompleto:
        if letra == " ":
                arrayString.append(palavra)
                palavra = ""
        else:
            palavra += letra
    if palavra != "":
        arrayString.append(palavra)
    return arrayString

def PegarIniciaisMaiuscula(listaPalavras):
    inicial = ""
    for i in range(len(listaPalavras)-1):
        for palavra in listaPalavras[i]:
            for letra in palavra:
                if letra.isupper():
                    inicial += letra + ". "
    return inicial

print(NomeArtigo("Matheus da Silva Rodrigues"))