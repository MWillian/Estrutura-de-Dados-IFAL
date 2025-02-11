# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
# pedir as informações.

nomeUsuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

while True:
    if nomeUsuario != senha:
        print("Usuário logado!")
        break
    else:
        print("O nome de usuário e senha não podem ser iguais!")
        nomeUsuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
