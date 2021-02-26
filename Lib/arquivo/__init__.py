
from Lib.valida import leiainteiro, leiastring
from Lib import interface as mens
from time import sleep
from colorama import init

init()


def sortcad():
    ''' Classificar o cadastro'''
    cadastro = readcad()
    cadastro.sort()
    savecad(cadastro)


def insertcad():
    ''' Insere dados novos no cadastro
    '''
    try:
        mens.imp_titulo('NOVO CADASTRO')
        nome = leiastring(' Nome: ')
        idade = leiainteiro(' Idade: ')

        arquivo = open('../../../Documents/MeusProjetos/CadastroSys/cadastro.txt', 'at')
        cad = (nome, idade)
        linha = str(cad) + '\n'
        # linhas.append(linha)
        # arquivo.writelines(linhas)
        arquivo.write(linha)
        arquivo.close()

        print(f' Novo registro de {mens.green_}{nome}{mens.default_} foi adicionado.')
    except:
        print(f"{mens.red_} ERRO: falha na inserção de registro.{mens.default_}")

    finally:
        arquivo.close()


def changecad(mensag):
    ''' Altera dados de cadastro
    '''
    while True:
        pessoas = findnome(mensag, True)
        listaopc = list(range(0, len(pessoas)))
        if len(pessoas) > 0:
            while True:
                num = leiainteiro(
                    f' Alterar o número{mens.green_}{listaopc}{mens.default_} ou [{mens.green_}999{mens.default_}-sair]: ')
                if num in range(0, len(pessoas)):
                    print('-' * 40)
                    print(f' Alterando {pessoas[num]}')
                    nome = leiastring(' Nome: ')
                    idade = leiainteiro(' Idade: ')

                    if len(nome) == 0 or nome == '':  ## nome vazio não altera
                        nome = pessoas[num][0]
                        print(nome)
                    if idade == 0 or idade > 120:  ## idade =0 ou maior que 120 não altera
                        idade = pessoas[num][1]

                    pessoa = (nome, idade)  ## monta a pessoa no padrão tupla do cadastro
                    cadastro = readcad()
                    ind = cadastro.index(pessoas[num])  ## localiza a pessoa no cadastro
                    cadastro[ind] = pessoa

                    savecad(cadastro)
                    print(f' Alterado cadastro de {pessoas[num]}')
                    print('-' * 40)
                    break

                elif num == 999:
                    break
                else:
                    print(f'\n {mens.red_}Por favor, digite um valor valido.{mens.default_}')

        if str(input(f'\n Quer  alterar outro cadastro [{mens.green_}S/N{mens.default_}]: ')) in 'nN':
            break


def delcad():
    ''' Encontra e deleta nome '''
    while True:
        pessoas = findnome('RETIRAR NOME DO CADASTRO', True)
        if len(pessoas) > 0:
            listaopc = list(range(0, len(pessoas)))
            while True:
                num = leiainteiro(f'\n Apagar o número{mens.green_} {listaopc} ou [999-sair]{mens.default_}: ')
                if str(input(
                        f'\n Quer mesmo {mens.green_}apagar{mens.red_} {pessoas[num]}{mens.default_}? [{mens.green_}S/N{mens.default_}]: ')) in 'nN':
                    break
                if num in range(0, len(pessoas)):
                    cadastro = readcad()
                    cadastro.remove(pessoas[num])
                    savecad(cadastro)
                    print('-' * 40)
                    print(f' {mens.red_}Apagado nome:{mens.green_} {pessoas[num]}{mens.default_}')
                    print()
                    break
                elif num == 999:
                    break
                else:
                    print(f'\n {mens.red_};Escolha não válida, veja as opções.{mens.default_}')

        if str(input(f'\n Quer  retirar outro nome[{mens.green_}S/N{mens.default_}]: ')) in 'nN':
            break


def showcad(mensag, cadastro):
    ''' Mostra o cadastro de pessoas
    '''
    try:
        mens.imp_titulo(mensag)
        if len(cadastro) > 0:
            tam_nome = 0
            tam_idade = 0
            for pessoa in cadastro:  ## ajuste de coluna para impressão
                if len(pessoa[0]) > tam_nome:
                    tam_nome = len(pessoa[0])
                if len(str(pessoa[1])) > tam_idade:
                    tam_idade = len(str(pessoa[1]))
            tam_nome += 5

            for i, pessoa in enumerate(cadastro):
                print(f' {mens.green_}[{i}]:{mens.default_} {pessoa[0]:.<{tam_nome}}{pessoa[1]:>{tam_idade}} anos')
        else:
            print()
            print(f' {mens.green_}... Ainda não há pessoas cadastradas.{mens.default_}')

    except:
        print(f' Cadastro apresentou problemas...')


def findnome(mensag, retorna=False):
    ''' Encontra um ou mais nomes no cadastro
        por default não retorna, True: retorna achados (achei)
        por default lê o arquivo: cadastro.txt
    '''
    try:
        while True:
            cadastro = readcad()
            mens.imp_titulo(mensag)
            nome = leiastring(' Qual nome procura?: ').upper()
            achei = list()  # nome achados

            for pessoa in cadastro:
                if nome in pessoa[0].upper() or nome == '*':
                    achei.append(pessoa)

            if len(achei) > 0:
                showcad(f'Resultado da pesquisa nome: {nome}', achei)
            else:
                print(f'\n Infelizmente <{mens.green_}{nome}{mens.default_}> não consta no cadastro.')

            if str(input(f'\n Quer procurar outro nome [{mens.green_}S/N{mens.default_}]: ')) in 'nN':
                break

        if retorna:
            return achei  ## lista de nomes encontrados

    except:
        print('ERRO: Falha na localização de pessoas')


def readcad():
    ''' Faz leitura do arquivo cadastro.txt
        Retirar a marca "\n" da linha e
        a converte em uma list de tuple [('Maria', 32), ('João', 42)]
     '''
    try:
        arquivo = open('../../../Documents/MeusProjetos/CadastroSys/cadastro.txt', 'rt')
        linhas = arquivo.readlines()
        arquivo.close()

        cadastro = list()
        for linha in linhas:
            pessoa = tuple(eval(linha))
            cadastro.append(pessoa)

    except FileNotFoundError:
        print(f' {mens.red_}Cadastro inexistente, arquivo foi criado agora.{mens.default_}')
        createcad('cadastro.txt')
        cadastro = list()


    except Exception as erro:
        pessoas = []
        print(
            f' {mens.red_}ERRO: Falha na leitura do arquivo{mens.default_} => {mens.green_}{erro.__class__}{mens.default_}')

    return cadastro


def createcad(arqnome):
    ''' cria arquivo txt '''
    try:
        arquivo = open(arqnome, 'wt+')
        # arquivo.writelines('')
        arquivo.close()
    except:
        print(f' {mens.red_}Arquivo cadastro.txt não criado!!{mens.default_}')


def savecad(cadastro):
    ''' grava no arquivo: cadastro.txt
        pessoa = ('Maria', 32) tipo tuple()
    '''
    try:
        pessoas = list()
        for item in cadastro:
            pessoa = str(item) + '\n'
            pessoas.append(pessoa)
        arquivo = open('../../../Documents/MeusProjetos/CadastroSys/cadastro.txt', 'wt')
        arquivo.writelines(pessoas)
        arquivo.close()

    except:
        print(f'{mens.red_} Falha na gravação no cadastro.{mens.default_}')
