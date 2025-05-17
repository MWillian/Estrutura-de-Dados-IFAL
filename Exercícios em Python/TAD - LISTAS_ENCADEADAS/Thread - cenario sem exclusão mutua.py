import threading
from Lista_Encadeada import *
from Noh import *
import time


# Variáveis simbólicas para exibir a ordem dos Nós adicionados e removidos
contador_insercao = 1
contador_remocao = 1


# Função para inserir Nós no fim na lista. A quantidade de Nós é recebida como parâmetro na função. 
# Para visualizar o estado da lista, os valores de cada Nó são retornados a cada inserção ou remoção.
def inserirXVezes(lista:ListaNaoOrdenada,quant,numeroThread):
    global contador_insercao
    for i in range(1,quant+1):
        time.sleep(5)
        print(f"Thread: {numeroThread}.\nAdicionando o {contador_insercao}º nó.")
        lista.add_fim(i)
        lista.print_lista()
        print()
    print("Inserção Finalizada")


# Função para remover o Nó da lista. A remoção ocorre no começo da lista.
def removerXVezes(lista:ListaNaoOrdenada,quant,numeroThread):
    global contador_remocao
    for i in range(1,quant+1):
        time.sleep(5)
        print(f"Thread: {numeroThread}\nRemovendo o {contador_remocao}º nó.")
        lista.remove_first()
        lista.print_lista()
        print()
    print("Remoção Finalizada")


# Instância da lista encadeada
ListaExemplo = ListaNaoOrdenada()


# Criação das Threads. Cada Thread recebe como parãmetro a função que deve ser executada, e seus argumentos.
Thread1 = threading.Thread(target=inserirXVezes,args=(ListaExemplo, 50,"1"))
Thread2 = threading.Thread(target=inserirXVezes,args=(ListaExemplo, 50,"2"))
Thread3 = threading.Thread(target=removerXVezes,args=(ListaExemplo, 60,"3"))
Thread4 = threading.Thread(target=removerXVezes,args=(ListaExemplo, 60,"4"))


# Inicialização das threads de forma simultânea
# O método .join impede que a mesma Thread instânciada seja chamada sem que esta mesma Thread seja finalizada.
Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()


# Finalização das threads
Thread1.join()
Thread2.join()
Thread3.join()
Thread4.join()