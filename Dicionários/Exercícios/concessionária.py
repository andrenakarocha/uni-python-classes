carros = {
    'Honda Civic': {
        'potência': '155 cv',
        'consumo (km/l)': 11.5,
        'cor': 'Prata',
        'ano': 2022,
        'estoque': 5,
        'preço (R$)': 125000 
    },
    'Toyota Corolla': {
        'potência': '177 cv',
        'consumo (km/l)': 12.0, 
        'cor': 'Preto',
        'ano': 2023,
        'estoque': 3,
        'preço (R$)': 145000 
    },
    'Ford EcoSport': {
        'potência': '137 cv',
        'consumo (km/l)': 9.5,
        'cor': 'Branco',
        'ano': 2021,
        'estoque': 4,
        'preço (R$)': 99000
    },
    'Chevrolet Onix': {
        'potência': '116 cv',
        'consumo (km/l)': 14.0,
        'cor': 'Vermelho',
        'ano': 2022,
        'estoque': 7,
        'preço (R$)': 75000 
    },
    'Volkswagen Golf': {
        'potência': '150 cv',
        'consumo (km/l)': 10.5, 
        'cor': 'Azul',
        'ano': 2023,
        'estoque': 2,
        'preço (R$)': 135000
    }
}

carrinho = {
    'Carros': {},
    'Valor total': 0,
    'Informações': {
            'Rua': '',
            'Numero': '',
            'CEP': '',
            'Complemento': ''
    }
}

usuarios = ['Cliente', 'Funcionário']

def forca_opcao (msg, lista, msg_erro):
    resp = input(msg)
    while resp not in lista:
        resp = input(msg_erro)
    return resp

def verificar_numero(msg, msg_erro):
    resp = input(msg)
    while not resp.isnumeric():
        resp = input(msg_erro)        
    return int(resp)

def listar_carros():
    for elem in carros.keys():
            print(f"{elem} - Estoque: {carros[elem]['estoque']} - Valor: {carros[elem]['preço (R$)']}")

def comprar():
    while True:
            listar_carros()
            escolha = forca_opcao('\nQual o carro que deseja? ', carros.keys(), '\nEsse carro não está no catálogo! ')
            if carros[escolha]['estoque'] == 0:
                print(f'\nNão temos mais {escolha} no nosso estoque! Por favor, escolha outro carro! ')
                continue

            qtd = verificar_numero(f'\nQuantas unidades de {escolha} você deseja? ', '\nResposta Inválida, insira um número! ')
            while qtd > carros[escolha]['estoque']:
                print(f'\nNão há essa quantidade no nosso estoque! ')
                qtd = verificar_numero(f'\nQuantas unidades de {escolha} você deseja? ', '\nResposta Inválida, insira um número! ')

            if escolha in carrinho['Carros'].keys():
                carrinho['Carros'][escolha] += qtd
            else:
                carrinho['Carros'][escolha] = qtd

            carros[escolha]['estoque'] -= qtd
            carrinho['Valor total'] += carros[escolha]['preço (R$)'] * qtd

            print('\nAdicionado ao carrinho!')
            continuar = forca_opcao('\nDeseja continuar comprando? ', ['Sim', 'Não'], '\nResposta inválida! (Sim/Não)')    

            if continuar == 'Sim':
                continue
            else:
                for atual in carrinho['Informações'].keys():
                    inpt = input(f'\nDiga o(a) seu(a) {atual}: ')
                    carrinho['Informações'][f'{atual}'] = inpt

                print(f'------------- \nSeu carrinho:')
                for carro in carrinho['Carros'].keys():
                    print(f'{carro} - Quantidade : {carrinho["Carros"][carro]}\n')
                print(f'\nValor total: {carrinho["Valor total"]}')
                print(f'\nA entrega será feita no endereço abaixo: \nRua: {carrinho["Informações"]["Rua"]}\nNúmero: {carrinho["Informações"]["Numero"]}\nCEP: {carrinho["Informações"]["CEP"]}')
                break

def remover_carro_admin():
    listar_carros()
    carro = forca_opcao('\nQual o carro que deseja remover? ', carros.keys(), '\nEsse carro não existe!, digite um carro válido: ')
    carros.pop(carro, None)
    print('\nCarro removido!')

def adicionar_carro_admin():
    nome = input('\nDigite o nome do carro: ')
    carros[nome] = {}
    for info in carros['Chevrolet Onix'].keys():
        inpt = input(f'\nDigite o(a) {info} do carro: ')
        carros[nome][info] = inpt
    print('\nCarro adicionado!') 

def atualizar_carro_admin():
    listar_carros()
    carro = forca_opcao('\nQual carro você deseja atualizar? ', carros.keys(), '\nEsse carro não está no catálogo!')
    
    print('\nInformações atuais do carro: ')
    for info in carros[carro].keys():
        print(f'\n{info} = {carros[carro][info]}')

    infos_escolhidas = []
    while True:
        info_escolhida = forca_opcao('\nQual informação você deseja alterar? ', carros[carro].keys(), '\nEssa não é uma informação válida! Digite novamente: ')
        infos_escolhidas.append(info_escolhida)
        continuar = forca_opcao('\nDeseja alterar mais alguma informação? ', ['Sim', 'Não'], '\nResposta Inválida! (Sim/Não)')
        if continuar == 'Sim':
            continue
        else:
            break

    for info in infos_escolhidas:
        inpt = input(f'\nQual será o(a) novo(a) {info}: ')
        carros[carro][info] = inpt
    
    print('\nCarro atualizado!')
    

def admin():
    while True:
        print('''
Admin Menu:
    1 - Remover Carro
    2 - Adicionar Carro
    3 - Atualizar Carro
''')

        escolha = forca_opcao('\nQual a opção que deseja? ', ['1', '2', '3'], '\nNão está na lista, digite o número correto')
    
        match escolha:
            case "1":
                remover_carro_admin()
                continue
            case "2":
                adicionar_carro_admin()
                continue
            case "3":
                atualizar_carro_admin()
                continue
                
def main():    
    usuario = forca_opcao('O que você é? (Cliente / Funcionário): ', usuarios, 'Resposta inválida! Escolha um usuário: ')
    if usuario == 'Cliente':
        comprar()
    else:
        admin()

if __name__ == '__main__':
    main()
    