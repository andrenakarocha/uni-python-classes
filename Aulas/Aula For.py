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

# comidas_favoritas ()
# Manipulação de 2 arrays para achar a "comida favorita" de cada professor

# senha_com_for ()
# Testa uma senha 3 vezes usando FOR, caso a senha náo seja a certa, pede a senha novamente e printa a quantidade de tentativas restantes

# achar_maior_preco ()
# Encontra o maior preço em uma tabela.

# inverter_lista ()
# Inverte uma array.