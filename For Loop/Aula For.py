def comidas_favoritas ():
    comidas = ['feijoada', 'lasanha', 'panqueca', 'miojo', 'pizza', 'strogonoff']
    nomes = ['Danilão', 'Lucas', 'Leandro', 'Wellington', 'Allen', 'Lucas Demetrius']
    for i in range (len(nomes)):
        if nomes[i] == 'Leandro':
            print(f'O {nomes[i]} come {comidas[i]}')

def senha_com_for ():
    for i in range (3):
        tentativa = input('Digite a senha: ')
        if tentativa != '1234':
            print('Senha incorreta!')
            if i < 2:
                print(f'Faltam {2 - i} tentativas!')
        else:
            print('Senha correta!')
    print ('Número de tentativas excedido!')

def achar_maior_preco ():
    carros = ['up', 'gol', 'celtinha', 'kombi', 'uno']
    precos = [10, 20, 100000, 15, 5]
    indice_maior = 0
    maior = precos[indice_maior]
    for i in range (len(carros)):
        if precos[i] > maior:
            maior = precos[i]
            indice_maior = i
    print(f'O {carros[indice_maior]} é o carro mais caro, custando: R${precos[indice_maior]:.2f}')

def inverter_lista ():
    lista = [3, 4, 5, 6, 7, 8, 9]
    ultimo = len(lista) - 1
    for i in range (len(lista) // 2):
        aux = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = aux
    print(lista)

def soma_10_numeros(num_list):
    sum = 0
    for number in num_list:
        sum += number
    print(sum)
    return

def tabuada(tabu_range, multi_range):
    for i in range(tabu_range):
        print(f'Tabuada do {i + 1}')
        for j in range(multi_range + 1):
            print(f'{i + 1} * {j + 1} = {(i + 1) * (j + 1)}')
    return

def odd_or_even(num_list):
    evens = 0
    for num in num_list:
        if num % 2 == 0:
            evens += 1

    odds = len(num_list) - evens
    print(f'Pares: {evens} \nÍmpares: {odds}')
    return


# comidas_favoritas ()
# Manipulação de 2 arrays para achar a "comida favorita" de cada professor

# senha_com_for ()
# Testa uma senha 3 vezes usando FOR, caso a senha náo seja a certa, pede a senha novamente e printa a quantidade de tentativas restantes

# achar_maior_preco ()
# Encontra o maior preço em uma tabela.

# inverter_lista ()
# Inverte uma array.

# soma_10_numeros([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Soma 10 números de uma array

# tabuada(5, 10)
# Cria tabuadas com os parâmetros passados

# odd_or_even([2, 4, 6, 5, 3, 1])
# Acha pares e ímpares