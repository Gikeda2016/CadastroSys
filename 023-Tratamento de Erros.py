''' Erros e exceções (divisão por zero, variável não inicializada ...)
'''
from colorama import init
init()

from mod_valida import leiainteiro, leiastring
from mod_arquivo import *
import mod_mens as mens

from time import sleep



def div():
    ''' testando comando try para tratamento exception   
    '''
    try:
        print()
        a = int(input('Numerador: '))
        b = int(input('Denominador:'))
        r = a / b
    
    except (ValueError, TypeError):  ## mais de um tipo de erro
        print('Apresentou problema no tipo de dados.')
    
    except ZeroDivisionError:
        print('Apresentou divisão por zero.')

    except KeyboardInterrupt:
        print('Usuário não informou os dados.')

    except Exception as erro:      ## erro genérico
       print(f'Infelizmente houve problema é :{erro.__class__}')
       print()

    else:
        print(f'O resultado é {r:.1f}')
        print()

    finally:  ## 
        print('Finalizando ....., volte sempre !!!')

def leiaint():
    ''' Valida o dado entrada para formato int
    '''
    while True:
        try:
            num = int(input(' Digite um número Inteiro: '))
        except KeyboardInterrupt:
            print()
            print(f'{mens.red_} ERRO: Usuário não informou o dado.{mens.default_}')
            print()
            num = 0 
            break
        
        except (ValueError, TypeError):
            print(f'{mens.red_} ERRO: apresentou erro no tipo de dado{mens.default_}')
            print()
            continue

        except Exception as erro:
            print(f'{mens.red_} ERRO: por favor, digite um valor válido{mens.default_}')
            print()
            continue
        
        else:
            break
    return num       

def leiafloat():
    ''' Valida o dado entrada para formato float
    '''
    while True:
        try:
            num = float(input(' Digite um número Real: '))

        except KeyboardInterrupt:
            print()
            print(f'{mens.red_} ERRO: Usuário preferiu digitar esse número.{mens.default_}')
            print()
            num = 0
            break
        
        except (ValueError, TypeError):
            print(f'{mens.red_} ERRO: apresentou erro no tipo de dado{mens.default_}')
            print()
            continue

        except Exception as erro:
            print(f'{mens.red_} ERRO: por favor, digite um valor válido{mens.default_}')
            print()
        
        else:
            break

    return num

def Exerc113():
    ''' Valida entrada de dois números: um Inteiro e outro Real.
        Funções: Leiainteiro e Leiareal validam os inputs.
        Estes utilizam (try,except,else) para detectar exceções ou erros
    '''
    print()
    mens.print_title('#113 - Tratamento de Erro e Exceções')
    nint = leiaint()
    nreal = leiafloat()
    print('-'*40)
    print(f' O valor Inteiro digitado foi {mens.green_}{nint}{mens.default_} e o Real foi{mens.green_} {nreal}{mens.default_}.')
    print()
    mens.print_end()

def Exerc114():
    ''' #114: Testa o acesso ao site pudim: <http://www.pudim.com.br/>
    '''
    import requests

    print()
    mens.print_title(f'#114: Teste de acesso a sites: Requests validado por ({mens.green_}try, except{mens.default_})')
  
    site = 'http://www.pudim1.com.br/'
    try:
        response = requests.get(site)
        if response.status_code == 200:
            print(f'  O site {mens.yellow_}<{site}> {mens.default_}está {mens.green_}acessível{mens.default_}, apresenta status = {mens.green_}{response.status_code}{mens.default_}')
        
    except requests.ConnectionError as erro:
        mens.typewriter(f' {mens.red_}O site não está acessível no momento: {erro.__class__}{mens.default_}')
    
    finally:
        print()
        mens.print_end()
        print()

def Exerc114a():
    ''' Acesso a site via urllib'''
    import urllib
    import urllib.request as request1

    site = 'http://www.pudim.com.br'
    print()
    mens.imp_titulo('#114a: Acesso a site: Validado por (try, exception')
    try:
        response = request1.urlopen(site)
    except request1.URLError:
        print()
        print(f' O site{mens.red_} <{site}>{mens.default_} não está acessível no momento.\n')
    else:
        print(f' O acesso ao site <{site}> foi conseguido com sucesso!!\n Apresenta status: {response.status}\n')
        # print(response.read())
        print()


def Exerc115():
    ''' Criar cadastro de pessoas (nome, idade).
        Funcionalidade para cadastrar e visualizar o cadastro
        Construir um menu onde se possa escolher estas opções acima.
        Fazer validadação dos inputs.
        Criar um arquivo: cadastro.txt
    '''
    while True:
        print()
        menu_lista = [  'Listar pessoas cadastradas',
                        'Cadastrar novas pessoas',
                        'Alterar dados de pessoas',
                        'Apagar nome do cadastrado',
                        'Localizar uma pessoa',
                        'Ordenar o cadastro',
                        'Sair do programa'  ]
        titulo = 'MENU PRINCIPAL: CADASTRO'
        opc = mens.menu( titulo, menu_lista)

        if opc == 1:
            showcad('PESSOAS CADASTRADAS', readcad())   
            sleep(2)  
        elif opc == 2:
            insertcad() 
            sleep(2)
        elif opc == 3:
            changecad('ALTERA DADOS CADASTRADOS')
            sleep(2)
        elif opc == 4:
            delcad()
            sleep(2)
        elif opc == 5:
            findnome('LOCALIZAR PESSOAS')
            sleep(2)
        elif opc == 6:
            sortcad()
            mens.typewriter(' ... Classificando o cadastro ...', cor=mens.green_ )
            showcad(' CADASTRO CLASSIFICADO...', readcad())
            sleep(4)

        elif opc == 7:
            mens.imp_titulo(f'{mens.green_} Saindo do sistema... Até Logo!{mens.default_}')
            sleep(2)
            break
        else:
            print(f'{mens.red_} Erro: Escolha uma opção válida (1-9):{mens.default_}')
            sleep(2)


def main():

    # Exerc113()
    # Exerc114()
    # Exerc114a()
    Exerc115()

main()