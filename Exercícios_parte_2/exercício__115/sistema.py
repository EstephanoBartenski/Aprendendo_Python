cores = {'limpa': '\033[m',
         'branco': '\033[1;30m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'ciano': '\033[1;36m',
         'cinza': '\033[1;37m'}
from ex115.lib.interface import *  # * é para importar tudo de lá
from ex115.lib.arquivo import *
from time import sleep

file = 'aula115.txt'
if not testfile(file):
    createfile(file)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa',
                 'Excluir uma pessoa do cadastro', 'Alterar dados', 'Sair do sistema'])
    if resp == 1:
        # opção de listar o conteúdo de um arquivo
        readfile(file)
    elif resp == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().capitalize()
        while True:
            try:
                n = int(input('\033[1;37mIdade: \033[m'))
                n = abs(n)  # função para módulo de um número
            except (ValueError, TypeError):
                print('\033[1;31mERRO! Digite uma idade válida.\033[m')
            except KeyboardInterrupt:
                print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            else:
                break
        idade = n
        cadastrar(file, nome, idade)
    elif resp == 3:
        cabeçalho('EXCLUIR DO CADASTRO')
        nome = str(input('Quem você deseja remover do cadastro: '))
        excluir(file, nome)
    elif resp == 4:
        cabeçalho('ALTERAR DADOS')
        quem = str(input('Alterar dados de qual pessoa? ')).strip()
        nome = str(input('Nome: ')).strip()
#        while True:
#            try:
#                n = int(input('\033[1;37mIdade: \033[m'))
#                n = abs(n)  # função para módulo de um número
#            except (ValueError, TypeError):
#                print('\033[1;31mERRO! Digite uma idade válida.\033[m')
#            except KeyboardInterrupt:
#                print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
#            else:
#                break
#        idade = n
        alterar(file, quem, nome)
    elif resp == 5:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida.\033[m')
    sleep(1)


