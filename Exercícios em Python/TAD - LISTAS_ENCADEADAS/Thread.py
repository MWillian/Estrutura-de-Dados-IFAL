import threading
from Lista_Encadeada import *
from Noh import *
import time
import random

ListaExemplo = ListaNaoOrdenada()

def inserirXVezes(lista:ListaNaoOrdenada,quant):
    for i in range(0,quant):
        time.sleep(5)
        print(f"Adicionando o {i}º nó.")
        lista.add_fim(random.randint(0,50))
        lista.print_lista()
    print("Inserção concluída")

def removerXVezes(lista:ListaNaoOrdenada,quant):
    for i in range(0,quant):
        time.sleep(5)
        print(f"Removendo o {i}º nó.")
        lista.remove_first()
        lista.print_lista()
    print("Remoção concluída")

Thread1 = threading.Thread(target=inserirXVezes,args=(ListaExemplo, 5))
Thread2 = threading.Thread(target=inserirXVezes,args=(ListaExemplo, 5))
Thread3 = threading.Thread(target=removerXVezes,args=(ListaExemplo, 6))
Thread4 = threading.Thread(target=removerXVezes,args=(ListaExemplo, 6))


# inicializando as threads

Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()

# finalizando as threads

Thread1.join()
Thread2.join()
Thread3.join()
Thread4.join()
