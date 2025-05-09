import threading
from Lista_Encadeada import *
from Noh import *
import time
import random

# função para inserir nós na lista. A quantidade de nós é recebida como parâmetro na função. 
# os valores dos Nós são gerados aleatóriamente entre 0 e 50.
# para visualizar o estados da lista, o valores de cada Nó é retornado a cada inserção e remoção 

def inserirXVezes(lista:ListaNaoOrdenada,quant):
    for i in range(1,quant+1):
        time.sleep(5)
        print(f"Adicionando o {i}º nó.")
        lista.add_fim(random.randint(0,50))
        lista.print_lista()
    print("Inserção concluída")


#função para remover o Nó da lista. A remoção ocorre no começo da lista.

def removerXVezes(lista:ListaNaoOrdenada,quant):
    for i in range(1,quant+1):
        time.sleep(5)
        print(f"Removendo o {i}º nó.")
        lista.remove_first()
        lista.print_lista()
    print("Remoção concluída")


# Instância da lista 
ListaExemplo = ListaNaoOrdenada()


# Criação das Threads. Cada Thread recebe como parãmetro a função que deve ser executada, e seus argumentos.
Thread1 = threading.Thread(target=inserirXVezes,args=(ListaExemplo, 3))
Thread2 = threading.Thread(target=inserirXVezes,args=(ListaExemplo, 3))
Thread3 = threading.Thread(target=removerXVezes,args=(ListaExemplo, 5))
Thread4 = threading.Thread(target=removerXVezes,args=(ListaExemplo, 5))


# inicializando as threads
Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()

# finalizando as threads
# o método .join impede que a mesma Thread instânciada seja chamada sem que esta mesma Thread seja finalizada.
Thread1.join()
Thread2.join()
Thread3.join()
Thread4.join()

