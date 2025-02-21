    # Escreva uma função que gere logins para usuários de um sistema de computação baseado na seguinte regra: o login é
    # composto pelas letras iniciais do nome do usuário.

nome = input("Digite seu nome de usuário: ")
def Login(nomeUsuario):
    inicias = nomeUsuario[0]
    for i in range(1,len(nomeUsuario)):
        if nomeUsuario[i] == " " and (i + 1) < len(nomeUsuario):
            inicias += nomeUsuario[i+1]
    return inicias

print(Login(nome))