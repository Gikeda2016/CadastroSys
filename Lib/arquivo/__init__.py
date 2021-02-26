
from Lib import valida as val
from Lib import interface as mens
from time import sleep
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


def sortcad():
    ''' Classificar o cadastro(lista)'''
    cadastro = readcad()
    cadastro.sort()   # ordena a lista contendo as tuplas
    savecad(cadastro)


def insertcad():
    ''' Insere dados novos no cadastro.
    '''
    try:
        mens.imp_titulo('NOVO CADASTRO')
        nome = val.leiastring(' Nome: ')
        idade = val.leiainteiro(' Idade: ')

        arquivo = open('cadastro.txt', 'at')  # abre para adicionar
        cad = (nome, idade)
        linha = str(cad) + '\n'
        arquivo.write(linha)
        arquivo.close()

        print(f' Novo registro de {green_}{nome}{default_} foi adicionado.')
    except:
        print(f"{red_} ERRO: falha na inserção de registro.{default_}")

    finally:
        arquivo.close()


def changecad(mensag):
    ''' Altera dados de cadastro.
        :mensag - cabeçalho 
    '''
    while True:
        pessoas = findnome(mensag, True)
        listaopc = list(range(0, len(pessoas)))
        if len(pessoas) > 0:
            while True:
                num = val.leiainteiro(
                    f' Alterar o número{green_}{listaopc}{default_} ou [{green_}999{default_}-sair]: ')
                if num in range(0, len(pessoas)):
                    print('-' * 40)
                    print(f' Alterando {pessoas[num]}')
                    nome = val.leiastring(' Nome: ')
                    idade = val.leiainteiro(' Idade: ')

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
                    print(f'\n {red_}Por favor, digite um valor valido.{default_}')

        if str(input(f'\n Quer  alterar outro cadastro [{green_}S/N{default_}]: ')) in 'nN':
            break


def delcad():
    ''' Encontra e deleta nome '''
    while True:
        pessoas = findnome('RETIRAR NOME DO CADASTRO', True)
        if len(pessoas) > 0:
            listaopc = list(range(0, len(pessoas)))
            while True:
                num = val.leiainteiro(f'\n Apagar o número{green_} {listaopc} ou [999-sair]{default_}: ')
                if num in listaopc:
                    if str(input(f'\n Quer mesmo {green_}apagar{red_} {pessoas[num]}{default_}? [{green_}S/N{default_}]: ')) in 'nN':
                        break
                    if num in range(0, len(pessoas)):
                        cadastro = readcad()
                        cadastro.remove(pessoas[num])
                        savecad(cadastro)
                        print('-' * 40)
                        print(f' {red_}Apagado nome:{green_} {pessoas[num]}{default_}')
                        print()
                        break
                elif num == 999:
                    break
                else:
                    print(f'\n {red_};Escolha não válida, veja as opções.{default_}')

        if str(input(f'\n Quer  retirar outro nome[{green_}S/N{default_}]: ')) in 'nN':
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
            tam_id = (len(cadastro)-1)//10 + 1
            for i, pessoa in enumerate(cadastro):
                print(f' {green_}[{i:{tam_id}}]:{default_} {pessoa[0]:.<{tam_nome}}{pessoa[1]:>{tam_idade}} anos')
        else:
            print()
            print(f' {green_}... Ainda não há pessoas cadastradas.{default_}')

    except Exception as erro:
        print(f' Cadastro apresentou problemas...{erro.__class__}')


def findnome(mensag, retorna=False):
    ''' Encontra um ou mais nomes no cadastro
        por default não retorna, True: retorna achados (achei)
        por default lê o arquivo: cadastro.txt
    '''
    try:
        while True:
            cadastro = readcad()
            mens.imp_titulo(mensag)
            nome = val.leiastring(' Qual nome procura?: ').upper()
            achei = list()  # nome achados

            for pessoa in cadastro:
                if nome in pessoa[0].upper() or nome == '*':
                    achei.append(pessoa)

            if len(achei) > 0:
                showcad(f'Resultado da pesquisa nome: {nome}', achei)
            else:
                print(f'\n Infelizmente <{green_}{nome}{default_}> não consta no cadastro.')

            if str(input(f'\n Quer procurar outro nome [{green_}S/N{default_}]: ')) in 'nN':
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
        arquivo = open('cadastro.txt', 'rt')
        linhas = arquivo.readlines()
        arquivo.close()

        cadastro = list()
        for linha in linhas:
            pessoa = tuple(eval(linha))
            cadastro.append(pessoa)

    except FileNotFoundError:
        print(f' {red_}Cadastro inexistente, arquivo foi criado agora.{default_}')
        createcad('cadastro.txt')
        cadastro = list()


    except Exception as erro:
        pessoas = []
        print(
            f' {red_}ERRO: Falha na leitura do arquivo{default_} => {green_}{erro.__class__}{default_}')

    return cadastro


def createcad(arqnome):
    ''' cria arquivo txt
        :arqnome - nome do arquivo - ""cadastro.txt"
    '''
    try:
        arquivo = open(arqnome, 'wt+')  # abre arquivo para escrita texto e sobrescreve se já existir de mesmo nome
        arquivo.close()
    except:
        print(f' {red_}Arquivo cadastro.txt não criado!!{default_}')


def savecad(cadastro):
    ''' grava no arquivo: cadastro.txt
        pessoa = ('Maria', 32) tipo tuple().
    '''
    try:
        pessoas = list()
        for item in cadastro:
            pessoa = str(item) + '\n'
            pessoas.append(pessoa)
        arquivo = open('cadastro.txt', 'wt')
        arquivo.writelines(pessoas)
        arquivo.close()

    except:
        print(f'{red_} Falha na gravação no cadastro.{default_}')
