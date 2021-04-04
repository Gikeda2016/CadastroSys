
from colorama import init
init()

''' Cores ANSI - ativadas por Colorama em init()'''
default_ =  '\33[m'  ## cor padrão
white_bold =  '\33[1;30m'
green_ = '\33[0;32m' ## letra verde
green_bold = '\33[1;32m' ## letra verde bold
red_ = '\33[0;31m' ##  letra vermelha
red_bold = '\33[1;31m' ##  letra vermelha bold
yellow_ =  '\33[0;33m' ##  letra amarela
yellow_bold =  '\33[1;33m' ##  letra amarela bold
blue_ = '\33[0;34m' ##  letra azul
blue_bold = '\33[1;34m' ##  letra azul bold
inversion_ ='\33[7;37;40m' ## padrão reverso -  fundo branco, letra preta
title_ = '\33[1;33m' ## padrão  -  fundo preto, letra branca


def leiainteiro(mensag):
    ''' Valida o dado entrada para formato int
    '''
    while True:
        try:
            num = int(input(f'{mensag}{green_}')) 
            print(default_, end='')   
        except KeyboardInterrupt:
            print()
            print(f'{red_} ERRO: Usuário não informou o dado.{default_}')
            print()
            continue
        except:
            print(f'{red_} ERRO: por favor, digite um valor válido.{default_}')
            print()
            continue  

        else:
            break       
    return num 

def leiastring(mensag):
    ''' valida o dado de entrada para o formato string '''
    while True:
        try:
            palavra = str(input(f'{mensag}{green_}')).strip()
            print(default_, end='')
            if palavra.isnumeric():
                print(f'{red_} Somente número não é valido.{default_}')
                continue
        except KeyboardInterrupt:
            print()
            print(f'{red_} ERRO: Usuário não informou o dado.{default_}')
            print()
            palavra = ''
            break  
        except:            
            print(f'{red_} ERRO: por favor, digite um valor válido.{default_}')
            continue
        else:
            break

    return palavra