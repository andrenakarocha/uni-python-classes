from typing import final


def bubble_sort(lista):
    for i in range(len(lista)):
        numero_de_trocas = 0
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                numero_de_trocas += 1
        if numero_de_trocas == 0:
            return lista



def raiz_cu(inicio, final, numero):
    chute = (inicio + final) / 2
    if chute ** 2 > numero:
        final = chute
    else:
        inicio = chute
    if final - inicio > 0.001:
        chute = raiz_cu(inicio, final, numero)
    return chute


def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[0]

    lista_maiores = [num for num in lista if num > pivot]
    lista_menores = [num for num in lista if num < pivot]

    lista_ordenada_maiores = quick_sort(lista_maiores)
    lista_ordenada_menores = quick_sort(lista_menores)

    return lista_ordenada_menores + [pivot] + lista_ordenada_maiores


def achar_numero(lista, numero):
    if len(lista) <= 1:
        print("NAO TA NA LISTA DAHHNNNN rOblOx eDgE")
        return

    inicio = 0
    final = len(lista) - 1
    chute = (inicio + final) // 2

    if lista[chute] == numero:
        return chute
    if lista[chute] < numero:
        return achar_numero(lista[chute + 1:], numero)
    else:
        return achar_numero(lista[:chute - 1], numero)

print(achar_numero([1, 2, 3, 4, 6, 7, 8, 9], 5))
