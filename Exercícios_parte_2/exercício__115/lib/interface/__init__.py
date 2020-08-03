cores = {'limpa': '\033[m',
         'branco': '\033[1;30m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'ciano': '\033[1;36m',
         'cinza': '\033[1;37m'}



def linha(tam=42):
    return '-' * tam


def cabeçalho(msg):
    print(linha())
    print(f'\033[1;37m{msg.center(42)}\033[m')  # alinha a mensagem no meio de 42 caracteres
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[1;36m[ {cont} ]\033[m - \033[1;30m{item}\033[m')
        cont += 1
    print(linha())
    while True:
        try:
            n = int(input('\033[1;37mSelecionar Opção:\033[m '))
            n = abs(n)
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite uma opção válida.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            break
    opção = n
    return opção