def comparacao_bouleanos ():
    n1 = 2
    n2 = 3
    n3 = 4
    n4 = 5
    print(f'A comparação {n1} > {n2} ou {n3} > {n4}, ou seja: {n1>n2} ou {n3>n4} dá {n1>n2 or n3>n4}'
        f'\nA comparação {n1} != {n2} ou {n3} < {n4}, ou seja: {n1!=n2} ou {n3<n4} dá {n1!=n2 or n3<n4}'
        f'\nA comparação {n1} > {n2} ou {n3} != {n4}, ou seja: {n1>n2} ou {n3!=n4} dá {n1>n2 or n3!=n4}'
        f'\nA comparação {n1} < {n2} ou {n3} > {n4}, ou seja: {n1<n2} ou {n3>n4} dá {n1<n2 or n3>n4}')
    print('-'*100)
    print(f'A comparação {n1} > {n2} e {n3} > {n4}, ou seja: {n1>n2} e {n3>n4} dá {n1>n2 and n3>n4}'
        f'\nA comparação {n1} != {n2} e {n3} < {n4}, ou seja: {n1!=n2} e {n3<n4} dá {n1!=n2 and n3<n4}'
        f'\nA comparação {n1} > {n2} e {n3} != {n4}, ou seja: {n1>n2} e {n3!=n4} dá {n1>n2 and n3!=n4}'
        f'\nA comparação {n1} < {n2} e {n3} > {n4}, ou seja: {n1<n2} e {n3>n4} dá {n1<n2 and n3>n4}')

def idoso_ou_nao ():
    a = str(input('Você é idoso?: '))
    if a == 'sim' or a == 'Sim':
        print('Você pode estacionar!')
    else:
        print('SAI DAQUI MENÓ')
    
def vogal_ou_nao ():
    letra = str(input('Digite uma letra: '))
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('A sua letra é uma vogal')
    else:
        print('A sua letra não é uma vogal')

    letra = str(input('Digite uma letra: '))
    if letra == 'a':
        print(f'A letra {letra} é uma vogal')
    elif letra == 'e':
        print(f'A letra {letra} é uma vogal')
    elif letra == 'i':
        print(f'A letra {letra} é uma vogal')
    elif letra == 'o':
        print(f'A letra {letra} é uma vogal')
    elif letra == 'u':
        print(f'A letra {letra} é uma vogal')
    else:
        print(f'A letra {letra} não é uma vogal')

def salario_e_aumento ():
    salario = float(input('Diga seu salário: '))
    if salario < 1903.98:
        ali = 0
    elif salario <= 2826.65:
        ali = 0.075
    elif salario <= 3751.05:
        ali = 0.15
    elif salario <= 4664.68:
        ali = 0.225
    else:
        ali = 0.275
    print(f'Seu desconto é {salario*ali:.2f} e seu novo salário é: {salario - (salario*ali):.2f}')

# comparacao_bouleanos ()
# Comparação para entender bouelanos

# idoso_ou_nao ()
# Verificar se é idoso ou não

# vogal_ou_nao ()
# Verificar se é vogal ou não

# salario_e_aumento ()
# Adicionar salário do usuario e aumento conforme o seu aumento
