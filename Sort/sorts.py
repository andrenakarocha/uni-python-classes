def achar_menor (lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    return indice_menor

def selection_sort(lista):
    lista_ordenada = []
    while lista:
        menor = achar_menor(lista)
        elemento = lista.pop(menor)
        lista_ordenada.append(elemento)
    return lista_ordenada

