# É muito comum que os títulos de documentos como avisos, declarações, atestados, etc., apareçam em letras maiúsculas
# separadas por um espaço em branco. Escreva uma função que receba uma palavra e a retorne no formato acima.

def Palavra(string):
    palavraMaiúscula = ""
    for i in string:
        palavraMaiúscula += i.upper()
        palavraMaiúscula += " "
    return palavraMaiúscula

print(Palavra("O Nome do Vento") )