# percorre toda a lista trocando os elementos quando o próximo for maior

def bubbleSort(uma_lista):
    for varredura in range(len(uma_lista)-1,0,-1):
        for i in range(varredura):
            if uma_lista[i]>uma_lista[i+1]:
                temp = uma_lista[i]
                uma_lista[i] = uma_lista[i+1]
                uma_lista[i+1] = temp

# Se não houver mais trocas, a lista está ordenada, então pode parar as varreduras

def shortBubbleSort(uma_lista):
    trocas = True
    varreduras = len(uma_lista)-1
    while varreduras > 0 and trocas:
        trocas = False
        for i in range(varreduras):
            if uma_lista[i]>uma_lista[i+1]:
                trocas = True
                temp = uma_lista[i]
                uma_lista[i] = uma_lista[i+1]
                uma_lista[i+1] = temp
        varreduras = varreduras-1
# aqui temos O(n²)


# selection sort: faz uma troca por vez a cada varredura da lista

def selectionSort1(uma_lista):
    for posicao_verificada in range(len(uma_lista)-1,0,-1):
        posicao_maior = 0
        for posicao in range(1,posicao_verificada+1):
            if uma_lista[posicao]>uma_lista[posicao_maior]:
                posicao_maior = posicao
        temp = uma_lista[posicao_verificada]
        uma_lista[posicao_verificada] = uma_lista[posicao_maior]
        uma_lista[posicao_maior] = temp

# continua O(n²)

def insertionSort(uma_lista):
    for index in range(1,len(uma_lista)):
        valor_atual = uma_lista[index]
        posicao = index
        while posicao>0 and uma_lista[posicao-1]>valor_atual:
            uma_lista[posicao]=uma_lista[posicao-1]
            posicao = posicao-1
        uma_lista[posicao]=valor_atual
        
# continua O(n²)




def shellSort(uma_lista):
    contador_sublista = len(uma_lista)//2
    while contador_sublista > 0:
        for posicao_inicial in range(contador_sublista):
            InsertionSortComGap(uma_lista,posicao_inicial,contador_sublista)
        print("Após incrementos de tamanho",contador_sublista,"a lista é",uma_lista)
        contador_sublista = contador_sublista // 2

def InsertionSortComGap(uma_lista,inicio,gap):
    for i in range(inicio+gap,len(uma_lista),gap):
        currentvalue = uma_lista[i]
        position = i
        while position>=gap and uma_lista[position-gap]>currentvalue:
            uma_lista[position]=uma_lista[position-gap]
            position = position-gap
        uma_lista[position]=currentvalue