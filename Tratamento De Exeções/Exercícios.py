def chave_indice():
    dic = {'chave': ['valor1', 'valor2']}
    while True:
        try:
            chave = input('Digite uma chave do dicionário: ')
            num = int(input('Diga um índice da lista: '))
            print(dic[chave][num])
            break
        except KeyError:
            print('A chave não corresponde a nenhuma!')
        except ValueError:
            print('O índice precisa ser um número!')
        except IndexError:
            print('O índice precisa estar entre 0 e 1!')


chave_indice()