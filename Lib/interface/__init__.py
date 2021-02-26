from time import sleep
from Lib import valida as val
from colorama import init
init()

''' Cores ANSI - ativadas por Colorama em init()'''
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
    ''' Imprime mensagem entre linhas.
    '''
    plin(tam)
    print(f'{yellow_}{mensag:^{tam}}{default_}')
    plin(tam)


def menu(titulo, lista):
    ''' Cria menu através da lista.
        :titulo - cabeçalho
        :lista - opções numeradas 1,2,3..,9 para escolher
    '''
    print()
    imp_titulo(titulo)
    lt_opcao = list(range(1, len(lista)+1))   # numera as opções 1,2,3,..,9
    lt_opcao[-1] = 9   ## para definir 9 como saida
    dig = len(lista)//10 + 1
    for i, item in enumerate(lista):  
        print(f' {yellow_}({lt_opcao[i]:0d}){default_}: {blue_bold}{item}{default_}')
    plin()  
    while True:
        opcao = val.leiainteiro(' Sua Opção: ')
        if opcao not in lt_opcao:
            print(f'{red_} Erro: Escolha uma opção válida{green_} {lt_opcao}{default_}')
            sleep(2)
        else:
            break
    return opcao


def print_title(titulo, tipo = '-', cor = title_):
    ''' imprime titulo centrado.
        :titulo - cabeçalho
        :tipo - caracter da linha
        :cor - cores possuiveis ANSI ou green_, red_, ...
    '''

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
    ''' Pergunta se quer continuar.
        Retorna: True ou False
    '''
    print()
    if val.leiastring(' Quer continuar? [S/N]: ') in 'nN':
        return True
    else:
        return False


def print_end():
    ''' Mensagem de despedida - cor verde
    '''
    print()
    typewriter(f'  .... {green_}Mais uma conquista, siga em frente !!{default_}  .....', 0.001)
    print()