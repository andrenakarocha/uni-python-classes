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

def forcar_opcao (msg, lista, msg_erro):
    opcao_selecionada = input(msg)
    while opcao_selecionada not in lista:
        print(msg_erro)
        opcao_selecionada = input(msg)
    return opcao_selecionada

def retorna_indice_elem_lista (lista, elem):
    indice_elem = 0
    for i in range(len(lista)):
        if lista[i] == elem:
            indice_elem = i
    return indice_elem

def verificar_mais_caro_em_lista (lista_produtos, lista_precos):
    mais_caro = lista_precos[0]
    indice_mais_caro = 0
    for i in range (len(lista_precos)):
        if lista_precos[i] > mais_caro:
            mais_caro = lista_precos[i]
            indice_mais_caro = i
    print(f'O produto mais caro é o {lista_produtos[indice_mais_caro]}, custando {lista_precos[indice_mais_caro]}')
    return indice_mais_caro

def trazer_informações_produto (msg, lista_produtos, lista_precos, lista_estoque):
    produto_escolhido = forcar_opcao(msg, lista_produtos)
    indice_produto_escolhido = retorna_indice_elem_lista(lista_produtos, produto_escolhido)

    print(f'O produto escolhido foi {produto_escolhido}, seu preço é {lista_precos[indice_produto_escolhido]}, e tem {lista_estoque[indice_produto_escolhido]} deste produto no estoque')

def adicionar_valores (lista_produtos, lista_precos):
    valor_total = 0
    while True:
        produto_escolhido = forcar_opcao('Qual vinho você deseja? ', lista_produtos, 'Não é um produto do catálogo!')
        indice_produto_escolhido = retorna_indice_elem_lista(lista_produtos, produto_escolhido)
        qtd_produto = verificar_numero('Quantas garrafas você vai querer? ')
        valor_total += lista_precos[indice_produto_escolhido] * qtd_produto

        escolha = forcar_opcao('Você deseja continuar comprando?: ', ['s', 'n'], 'Apenas (s/n)!')
        if escolha == 's':
            continue
        else:
            break
    print(f'O valor total foi {valor_total}')
    return

def zeros_e_uns (lista_num, digitos):
    numeros_vezes_digitos_aparecem = 0
    for i in range (len(lista_num) - len(digitos)+1):
        qtd_corretos = 0
        for j in range (len(digitos)):
            if digitos[j] != lista_num[i + j]:
                break
            qtd_corretos += 1
        if qtd_corretos == 3:
            numeros_vezes_digitos_aparecem += 1
    print(f'A quantidade de vezes que os digitos {digitos} aparecem na lista {lista_num} é {numeros_vezes_digitos_aparecem}')

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

# retorna_indice_elem_lista (['Matheus', 'André', 'Linard', 'Caio'], 'Roberto')
# Retorna o indice de um elem dentro de uma array

# verificar_mais_caro_em_lista(['Pérgola', 'Sangue de Boi', 'Chapinha'], [150, 430, 200])
# Retorna o nome e preço do produto mais caro da array

# trazer_informações_produto('Escolha o vinho desejado: ', ['Pérgola', 'Sangue de Boi', 'Chapinha'], [150, 430, 200], [2, 5, 9])
# Mostra todas as informações de um produto usando seu índice

# adicionar_valores(['Pérgola', 'Sangue de Boi', 'Chapinha'], [150, 430, 200])
# Adiciona os valores de garrafas em um valor total, pode pedir mais garrafas

zeros_e_uns([1, 1, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1])