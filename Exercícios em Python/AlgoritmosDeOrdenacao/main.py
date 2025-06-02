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