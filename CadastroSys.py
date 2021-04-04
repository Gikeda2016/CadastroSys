''' Erros e exceções (divisão por zero, variável não inicializada ...)
'''
from colorama import init
init()

from Lib.arquivo import *
from Lib import interface as mens
from time import sleep

def CadastroSys():
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
            sleep(4)  
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
        elif opc == 9:
            mens.imp_titulo(f'{mens.green_} Saindo do sistema... Até Logo!{mens.default_}')
            sleep(2)
            break
        else:
            print(f'{mens.red_} Erro: Escolha uma opção válida (1-9):{mens.default_}')
            sleep(2)


if __name__ == '__main__':
    
    CadastroSys()


