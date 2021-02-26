from time import sleep
from datetime import date
from Lib import valida as val
from colorama import init
init()

default_ =  '\33[m'  ## cor padrão
green_ = '\33[0;32m' ## letra verde
green_bold = '\33[1;32m' ## letra verde bold
red_ = '\33[0;31m' ##  letra vermelha
red_bold = '\33[1;31m' ##  letra vermelha bold
yellow_ =  '\33[0;33m' ##  letra amarela
yellow_bold =  '\33[0;33m' ##  letra amarela bold
blue_ = '\33[0;34m' ##  letra azul
blue_bold = '\33[1;34m' ##  letra azul bold
inversion_ ='\33[7;37;40m' ## padrão reverso -  fundo branco, letra preta
title_ = '\33[1;33m' ## padrão  -  fundo preto, letra branca


def plin(tam=50, tipo='-'):
    ''' cria linha '''
    print( tipo*tam)


def imp_titulo(mensag, tam=50):
    ''' Imprime Cabeçalho '''
    plin(tam)
    print(f'{yellow_}{mensag:^{tam}}{default_}')
    plin(tam)


def menu(titulo, lista):
    ''' Cria menu através da lista   '''
    print()
    imp_titulo(titulo)
    for i, item in enumerate(lista):
        print(f' {yellow_}({i+1}){default_}: {blue_bold}{lista[i]}{default_}')
    plin()
    while True:
        opcao = val.leiainteiro(' Sua Opção: ')
        if opcao not in list(range(1,len(lista)+1)):
            print(f'{red_} Erro: Escolha uma opção válida{green_} {list(range(1, len(lista)+1))}{default_}')
            sleep(2)
        else:
            break
    return opcao


def print_title(titulo, tipo = '-', cor = title_):
    ''' imprime titulo centrado '''
    tam = len(titulo)+12
    print(f'{tipo}'*tam)
    typewriter(f'{titulo:^{tam}}', cor = cor )
    print(f'{tipo}'*tam)
    print()


def typewriter(palavra, tempo = 0.1, cor = default_):
    ''' O programa digita letra por letra com delay
    '''
    print(f'{cor}', end='')
    for letra in palavra:
        print(letra, end='')
        sleep(tempo)
        if letra in ',:"=!.':
            sleep(0.5)
    print(f'{default_}')


def efim():
    print()
    if str(input(' Quer continuar? [S/N]: ')).upper()[0] in 'N':
        return True
    else:
        return False


def print_end():
    print()
    typewriter(f'  .... {green_}Mais uma conquista, siga em frente !!{default_}  .....', 0.001)
    print()