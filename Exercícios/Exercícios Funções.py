def exercicio_1(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    print(f'A soma da lista é: {soma}')
    return soma


def exercicio_2(lista_num):
    indice_maior = 0
    maior = lista_num[indice_maior]
    for i in range(len(lista_num)):
        if lista_num[i] > maior:
            maior = lista_num[i]
    print(f'O maior número da lista é {maior}')
    return maior


def exercicio_3(lista_de_strings):
    lista_apenas_a = []
    for i in range(len(lista_de_strings)):
        if lista_de_strings[i][0] == 'a':
            lista_apenas_a.append(lista_de_strings[i])
    print(f'A lista final é: {lista_apenas_a}')
    return lista_apenas_a


def exercicio_4(lista):
    pares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
    print(f'Os pares dentro da lista {lista} são: {pares}')

    # One Liner
    # pares = [lista[i] for i in range(len(lista)) if lista % 2 == 0]
    return pares


def exercicio_5(lista_palavras):
    numero_letras = []
    for i in range(len(lista_palavras)):
        numero_letras.append(len(lista_palavras[i]))
    print(f'A lista com o tamanho de cada palavra é: {numero_letras}')
    return numero_letras


def exercicio_6(lista1, lista2):
    elementos_comuns = []
    if len(lista1) >= len(lista2):
        for i in range(len(lista1)):
            if lista1[i] in lista2:
                elementos_comuns.append(lista1[i])
    else:
        for i in range(len(lista2)):
            if lista2[i] in lista1:
                elementos_comuns.append(lista2[i])
    print(f'A lista com os elementos comuns entre as duas listas é: {elementos_comuns}')
    return elementos_comuns


def exercicio_7(lista_num):
    for i in range(len(lista_num) - 1):
        if lista_num[i] > lista_num[i + 1]:
            return False
    return True


def exercicio_8(lista_num):
    ultimo = len(lista_num) - 1
    for i in range(len(lista_num) // 2):
        guardar_valor = lista_num[i]
        lista_num[i] = lista_num[ultimo - i]
        lista_num[ultimo - i] = guardar_valor
    print(f'A lista invertida é {lista_num}')
    return lista_num


def exercicio_9(lista_strings):
    lista_ordem_alfabetica = []
    while lista_strings:
        menor_string = lista_strings[0]
        menor_index = 0
        for i in range(len(lista_strings)):
            if lista_strings[i] < menor_string:
                menor_string = lista_strings[i]
                menor_index = i
        lista_ordem_alfabetica.append(menor_string)
        lista_strings.pop(menor_index)
    print(f'A lista em ordem alfabética é: {lista_ordem_alfabetica}')
    return lista_ordem_alfabetica


def exercicio_10(lista_num):
    soma = 0
    for i in range(len(lista_num)):
        soma += lista_num[i]
    print(f'A média aritmética dos elementos na lista é: {soma / len(lista_num)}')
    return soma / len(lista_num)

# exercicio_1([2, 3, 4, 6])
# Retorna a soma dos elementos em uma array

# exercicio_2([2, 4, 5, 6, 1, 41, 78, 98])
# Retorna o maior número em uma array

# exercicio_3(['ana', 'andre', 'caio', 'jonas', 'amei'])
# Retorna uma array com as palavras que começam com 'a'

# exercicio_4([2, 4, 5, 6, 1, 41, 78, 98])
# Retorna uma array com os pares de outra array

# exercicio_5(['ana', 'andre', 'caio', 'jonas', 'amei'])
# Retorna uma array com a quantidade de letras de cada palavra

# exercicio_6(['ana', 'andre', 'caio', 'jonas', 'amei'], ['andre', 'ana', 'anao', 'seila', 'amei'])
# Retorna uma lista com os elementos em comum entre duas listas

# exercicio_7([1, 2, 3, 4, 5, 10, 7])
# Retorna True se estiver em ordem crescente e False se não

# exercicio_8([1, 2, 3, 4, 5, 10, 7])
# Retorna a ordem inversa da array passada

# exercicio_9(['bu', 'ana', 'caio', 'jonas', 'opa'])
# Retorna a array em ordem alfabética

# exercicio_10([1, 2, 3, 4])
# Retorna a média aritmética dos números em uma array
