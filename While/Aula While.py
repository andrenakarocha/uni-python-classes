#Pares e Ímpares (While)
def pares_e_impares () :
    repeticoes = 0
    pares = 0
    while repeticoes < 5:
        num = int(input('Diga um número: '))
        if num%2==0:
            pares += 1
        repeticoes += 1
    impares = 5 - pares
    print(f'O número de pares foi {pares} e o número de ímpares foi {impares}')

#Testando senha com While
def teste_de_senha () :
    senha = input('Digite a senha: ')
    while senha != '1234':
        print ('Senha incorreta!')
        senha = input('Digite a senha: ')
    print('Senha correta!')

#Bloqueando o acesso com 3 senhas incorretas
def senha_acesso_bloqueado () :
    senha = input('Digite a senha: ')
    tentativas = 1
    while senha != '1234' and tentativas < 3:
        print (f'Senha incorreta! Você tem mais {3-tentativas} tentativas!')
        senha = input('Digite a senha: ')
        tentativas += 1
    if senha == '1234':
        print('Senha correta!')
    else:
        print('Acesso Negado!')

#Soma de 10 números pedidos com while
def soma_10_numeros () :
    quant_num = 0
    soma = 0
    while quant_num < 10:
        num = int(input('Digite um número: '))
        quant_num += 1
        soma += num
    print(f'A soma de todos os números é {soma}')

#Soma de 10 até 1 com while
def soma_10_ate_1 () :
    i = 11
    soma = 0
    while i > 0:
        i -= 1
        soma += i
        print(soma)

#Frase com 10 palavras com while
def frase_10_palavras () :
    i = 0
    frase = ''
    while i < 10:
        pal = input('Digite uma palavra: ')
        i += 1
        frase += ' ' + pal
        print(frase)

#Quantidade de vogais e consoantes
def contar_vogais_consoantes () :
    i = 0
    vogais = 0
    consoantes = 0
    while i < 10:
        letra = input('Digite uma letra: ')
        i += 1
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            vogais += 1
        else:
            consoantes += 1
    print(f"A quantidade de vogais é {vogais} e a quantidade de consoantes é {consoantes}")

#Verificar e transformar um número inteiro
def tratamento_de_numero () :
    n = input('Digite um número: ')
    while not n.isnumeric():
        print('Isso não é um número!')
        n = input('Digite um número: ')
    print('É numero')
    n = int(n)

# pares_e_impares ()
# Acha a quantidade de pares e ímpares conforme os inputs que o usuário deu

# teste_de_senha ()
# Teste de senha básico

# senha_acesso_bloqueado ()
# Mesmo código acima, porém, bloqueia o acesso caso ultrapasse 3 tentativas

# soma_10_numeros ()
# Soma de 10 números que o usuário forneceu
    
# soma_10_ate_1 ()
# Soma dos números 10 até 1, ou seja, 10+9+8...
    
# frase_10_palavras ()
# Somando palavras que pedidos ao usuário usando strings

# contar_vogais_consoantes ()
# Conta a quantidade de vogais e consoantes que o usuário forneceu
    
# tratamento_de_numero ()
# Entende quando um input é um número ou não, avisando o usuário quando não é um número
