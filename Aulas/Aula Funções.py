def verificar_par (numero):
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} não é par')
    return

def verifica_vogal (letra):
    vogais = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    if letra in vogais:
        print(f'{letra} é uma vogal!')
        return True
    else:
        print(f'{letra} é consoante')
        return False

def soma_lista (lista):
    soma = 0
    for i in range (len(lista)):
        soma += lista[i]
    print(f'A soma é {soma}')
    return soma

def media_lista (lista):
    soma = soma_lista(lista) # Usando outra função para ajudar
    print(f'A média entre {lista}, é {soma / len(lista)}')
    return soma / len(lista)

def conta_vogal (string):
    qtd_vogal = 0
    for i in range (len(string)):
        if verifica_vogal(string[i]): # Usando outra função para ajudar
            qtd_vogal += 1
    print(f'A quantidade de vogais na frase: {string} é {qtd_vogal} vogais')
    return qtd_vogal

def criar_lista_pares (lista):
    pares = []
    for i in range (len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
    print(f'Os pares dentro da lista {lista} são: {pares}')

    # One Liner
    # pares = [lista[i] for i in range(len(lista)) if lista % 2 == 0]
    return pares

def verificar_numero (msg):
    num = input(msg)
    while True:
        if num.isnumeric():
            break
        else:
            print('Isso não é um número')
            num = input(msg)
    return int(num)

def forcar_opcao (msg, lista):
    opcoes = ''
    for i in range (len(lista)):
        opcoes += f'\n{lista[i]}'
    print(f'As nossas opções são: {opcoes}')

    opcao_selecionada = input(msg)
    while True:
        if opcao_selecionada in lista:
            break
        else:
            print('Não é uma opção válida!')
            opcao_selecionada = input(msg)
    return opcao_selecionada

def verificar_nome_em_lista (lista, nome):
    for i in range (len(lista)):
        if lista[i] is nome:
            return True
    return False

def exercicio_2 (lista_num):
    indice_maior = 0
    maior = lista_num[indice_maior]
    for i in range (len(lista_num)):
        if lista_num[i] > maior:
            maior = lista_num[i]
    print(f'O maior número da lista é {maior}')
    return maior

def exercicio_3 (lista_de_strings):
    lista_apenas_a = []
    for i in range (len(lista_de_strings)):
        if lista_de_strings[i][0] == 'a':
            lista_apenas_a.append(lista_de_strings[i])
    print(f'A lista final é: {lista_apenas_a}')
    return lista_apenas_a

def exercicio_5 (lista_palavras):
    numero_letras = []
    for i in range (len(lista_palavras)):
        numero_letras.append(len(lista_palavras[i]))
    print(f'A lista com o tamanho de cada palavra é: {numero_letras}')
    return numero_letras

def exercicio_6 (lista1, lista2):
    elementos_comuns = []
    if len(lista1) >= len(lista2):
        for i in range (len(lista1)):
            if lista1[i] in lista2:
                elementos_comuns.append(lista1[i])
    else:
        for i in range (len(lista2)):
            if lista2[i] in lista1:
                elementos_comuns.append(lista2[i])
    print(f'A lista com os elementos comuns entre as duas listas é: {elementos_comuns}')
    return elementos_comuns

def exercicio_7 (lista_num):
    for i in range (len(lista_num) - 1):
        if lista_num[i] > lista_num[i + 1]:
            return False
    return True


# verificar_par(n)
# Verifica se um número é par ou não

# verifica_vogal(letra)
# Verifica se uma letra passada é uma vogal ou não

# soma_lista([2, 3, 4, 6])
# Retorna a soma dos elementos em uma array

# media_lista([2, 3, 4, 6])
# Retorna a média dos elementos em uma array

# conta_vogal('Andre')
# Conta a quantidade de vogais em uma frase

# criar_lista_pares([2, 4, 5, 6, 1, 41, 78, 98])
# Cria uma array com os pares de uma outra array

# verificar_numero('Digite seu ano de nascimento: ')
# Verifica se o input de uma frase qualquer é um número

# forcar_opcao('Digite o vinho que deseja: ', ['Vinho 1', 'Vinho 2', 'Vinho 3', 'Vinho 4'])
# Verificar se o input está dentro de uma array

# verificar_nome_em_lista (['Matheus', 'André', 'Linard', 'Caio'], 'Roberto')
# Verifica se um nome está em uma array, ambos passados como parâmetros

# Exercício 1
# soma_lista([2, 3, 4, 6])
# Retorna a soma dos elementos em uma array

# exercicio_2([2, 4, 5, 6, 1, 41, 78, 98])
# Retorna o maior número em uma array

# exercicio_3(['ana', 'andre', 'caio', 'jonas', 'amei'])
# Retorna uma array com as palavras que começam com 'a'

# Exercício 4
# criar_lista_pares([2, 4, 5, 6, 1, 41, 78, 98])
# Retorna uma array com os pares

# exercicio_5(['ana', 'andre', 'caio', 'jonas', 'amei'])
# Retorna uma array com a quantidade de letras de cada palavra
                
# exercicio_6(['ana', 'andre', 'caio', 'jonas', 'amei'], ['andre', 'ana', 'anao', 'seila', 'amei'])
# Retorna uma lista com os elementos em comum entre duas listas

# exercicio_7([1, 2, 3, 4, 5, 10, 7])
# Retorna True se estiver em ordem crescente e False se não
