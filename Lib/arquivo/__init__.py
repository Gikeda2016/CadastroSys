
from Lib import valida as val
from Lib import interface as mens
from time import sleep
from colorama import init
init()

''' Cores ANSI - ativadas por Colorama em init()'''
default_ =  '\33[m'  ## cor padrão
white_bold =  '\33[m'
green_ = '\33[0;32m' ## letra verde
green_bold = '\33[1;32m' ## letra verde bold
red_ = '\33[0;31m' ##  letra vermelha
red_bold = '\33[1;31m' ##  letra vermelha bold
yellow_ =  '\33[0;33m' ##  letra amarela
yellow_bold = '\33[1;33m' ##  letra amarela bold
blue_ = '\33[0;34m' ##  letra azul
blue_bold = '\33[1;34m' ##  letra azul bold
inversion_ ='\33[7;37;40m' ## padrão reverso -  fundo branco, letra preta
title_ = '\33[1;33m' ## padrão  -  fundo preto, letra branca

basedir = 'C:\\Users\\55119\\Documents\\MeusProjetos\\CadastroSys\\'  ## ajustar para cada reinstalação


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
        cad = (nome, idade)   # tuple do novo cadastro
        linha = str(cad) + '\n' 

        with open('cadastro.txt', 'at', encoding='utf-8') as arquivo:  # abre para adicionar
            arquivo.write(linha)

        print(f' Novo registro de {green_}{nome}{default_} foi adicionado.')
    except:
        print(f"{red_} ERRO: falha na inserção de registro.{default_}")


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

        print(f'\n Quer  alterar outro cadastro [{green_}S/N{default_}]: ', end='')
        if str(input()) in 'nN':
            break


def delcad():
    ''' Encontra e deleta nome '''

    while True:
        pessoas=[]
        pessoas = findnome('RETIRAR NOME DO CADASTRO', True)
        if len(pessoas) > 0:
            listaopc = list(range(0, len(pessoas)))
            while True:
                num = val.leiainteiro(f'\n Apagar o número{green_} {listaopc} ou [999-sair]{default_}: ')
                if num in listaopc:
                    print(f'\n Quer mesmo {green_}apagar{red_} {pessoas[num]}{default_}? [{green_}S/N{default_}]: ', end='')
                    if str(input()) in 'nN':
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

        print(f'\n Quer  retirar outro nome[{green_}S/N{default_}]: ', end='')
        if str(input()) in 'nN':
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
                print(f' {green_bold}[{i:{tam_id}}]:{white_bold} {pessoa[0]:.<{tam_nome}}{pessoa[1]:>{tam_idade}} anos{default_}')
        else:
            print()
            print(f' {green_}... Ainda não há pessoas cadastradas.{default_}')

    except Exception as erro:
        print(f' Cadastro apresentou problemas...{erro.__class__}')


def findnome(mensag, retorna=False):
    ''' Procura nomes no cadastro e os imprime, por default não retorna (False)
    '''
    try:
        while True:
            achei_nomes = []  # nome achados
            cadastro = readcad()
            mens.imp_titulo(mensag)
            nome = val.leiastring(' Qual nome procura?: ').upper()
            for pessoa in cadastro:
                if nome in pessoa[0].upper() or nome == '*':
                    achei_nomes.append(pessoa)

            if len(achei_nomes) > 0:
                showcad(f'Resultado da pesquisa nome: {nome}', achei_nomes)
            else:
                print(f'\n Infelizmente <{green_}{nome}{default_}> não consta no cadastro.')

            print(f'\n Quer procurar outro nome [{green_}S/N{default_}]: ', end='')
            if str(input()) in 'nN':
                break

        if retorna:
            return achei_nomes  ## lista de nomes encontrados

    except:
        print('ERRO: Falha na localização de pessoas')


def readcad():
    ''' Faz leitura do arquivo cadastro.txt
        Retirar a marca "\n" da linha e
        a converte em uma list de tuple [('Maria', 32), ('João', 42)]
     '''
    try:
        with open(basedir + 'cadastro.txt', 'rt', encoding ='utf-8') as arquivo:
            linhas = arquivo.readlines()
        cadastro = []
        for linha in linhas:
            pessoa = tuple(eval(linha))
            cadastro.append(pessoa)       
        return cadastro

    except FileNotFoundError:
        print(f' {red_}Cadastro inexistente, arquivo foi criado agora.{default_}')
        createcad('cadastro.txt')
        cadastro = list()
    except Exception as erro:
        pessoas = []
        print(
            f' {red_}ERRO: Falha na leitura do arquivo{default_} => {green_}{erro.__class__}{default_}'
            )



def createcad(arqnome):
    ''' cria arquivo txt
        :arqnome - nome do arquivo - ""cadastro.txt"
    '''
    try:
        arquivo = open(basedir + arqnome, 'wt+', encoding ='utf-8')  # cria um novo arquivo ou o sobrescreve se existir 
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
        
        with open(basedir + 'cadastro.txt', 'wt', encoding='utf-8') as arquivo:
            arquivo.writelines(pessoas)

    except:
        print(f'{red_} Falha na gravação no cadastro.{default_}')
