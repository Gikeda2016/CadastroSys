from colorama import init
init()

default_ =  '\33[m'     ## cor padrão
green_ = '\33[0;32m'    ## letra verde
green_bold = '\33[1;32m'    ## letra verde bold
red_ = '\33[0;31m'      ##  letra vermelha
red_bold = '\33[1;31m'  ##  letra vermelha bold
yellow_ =  '\33[0;33m'  ##  letra amarela
yellow_bold =  '\33[0;33m'  ##  letra amarela bold
blue_ = '\33[0;34m'     ##  letra azul
blue_bold = '\33[1;34m' ##  letra azul bold
inversion_ ='\33[7;37;40m' ## padrão reverso -  fundo branco, letra preta
title_ = '\33[1;33m'    ## padrão  -  fundo preto, letra branca


def leiainteiro(mens):
    ''' Valida o dado entrada para formato int
        :[mens] - [string] - mensagem para input
    '''
    while True:
        try:
            print(f'{mens}{green_}', end ='')
            num = int(input())
            print(f'{default_}')

        except KeyboardInterrupt:
            print(f'\n{red_} ERRO: Usuário não informou o dado.{default_}')
            continue

        except:
            print(f'\n{red_} ERRO: por favor, digite um valor válido.{default_}')
            continue
        else:
            break
    return num


def leiastring(mens):
    ''' valida o dado de entrada para o formato string 
        [mens] - [string] mensagem para input
    '''
    while True:
        palavra =''
        try:
            print(f'{mens}{green_}', end='')
            palavra = str(input()).strip()
            print(f'{default_}')
            if palavra.isnumeric():
                print(f'\n{red_} Somente número não é valido.{default_}')
                continue

        except KeyboardInterrupt:
            print(f'\n{red_} ERRO: Usuário não informou o dado.{default_}')
            break
        except:
            print(f'\n{red_} ERRO: por favor, digite um valor válido.{default_}')
            continue
        else:
            break

    return palavra
