# As companhias de transportes aéreos costumam representar os nomes dos passageiros no formato último
# sobrenome/nome. Por exemplo, o passageiro Carlos Drumond de Andrade seria indicado por Andrade/Carlos. Escreva um
# programa que lê um nome e o escreve no formato acima.

def NomeContrario(palavra):
    primeiroNome = ""
    ultimoNome = ""
    quantidadeLetras = 0
    nomeCompleto = ""
    for i in range(0,len(palavra)):
        if palavra[i] != " ":
            primeiroNome += palavra[i]
        else:
            break
    for i in range(0,len(palavra)):
        quantidadeLetras += 1
        if palavra[i] == " ":
            cont = quantidadeLetras
    for cont in range(cont,len(palavra)):
        ultimoNome += palavra[cont]
    nomeCompleto += ultimoNome
    nomeCompleto += "/" + primeiroNome
    print(nomeCompleto)

frase = "Matheus Willian do Nascimento Oliveira"
NomeContrario(frase)
            