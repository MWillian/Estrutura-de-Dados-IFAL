from Contas import *

class Lista_Contas:
    def __init__(self):
        self.TAMANHO = 5
        self.lista = [None,None,None,None,None]
        self.tamanho_lista = 0
    
    def AdicionaContaSeparadamente(self,conta):
        if self.tamanho_lista < self.TAMANHO:
            self.lista[self.tamanho_lista] = conta
            self.tamanho_lista += 1
        else:
            print("Lista cheia")

    def ColetaDados(self):
        while self.tamanho_lista < self.TAMANHO:
            numero_conta = input("Digite o número da conta ou 'sair' para encerrar: ")
            if numero_conta.lower() == 'sair':
                break
            nova_conta = Conta(numero_conta)
            self.AdicionaContaSeparadamente(nova_conta)
            print("Conta adicionada")
        else:
            print("A lista está cheia")

    def ExibeTodas(self):
        print("Contas cadastradas: ")
        for i in range(self.tamanho_lista):
            conta = self.lista[i]
            print(f"Número da conta: {conta}")

teste_conta = Conta("155")
print(teste_conta.numeroConta)
# listaContas = Lista_Contas()
# listaContas.ColetaDados()
# listaContas.ExibeTodas()    
