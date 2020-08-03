def leiadinheiro(msg):
    ok = False
    n = 0
    while not ok:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'ERRO! "{n}" é um preço inválido!')
        else:
            ok = True
    return float(n)


def leiaint(msg):
    """
    → Valida um número inteiro.
    :param msg: (opcional) Número a ser validado.
    :return: O valor numérico recebido transformado para inteiro.
    → Criado por Estephano Bartenski (28/07/20).
    """
    ok = False
    n = 0
    while True:
        n = str(input(msg)).strip()
        if n[0] in '-' or n.isnumeric():
            n = int(n)
            ok = True
        else:
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
        if ok:
            break
    return n


def leiaintv2(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiareal(msg):
    """
    → Valida um número real.
    :param msg: (opcional) Número a ser validado.
    :return: O valor numérico recebido transformado para float.
    → Criado por Estephano Bartenski (28/07/20).
    """
    ok = False
    n = 0
    while True:
        n = str(input(msg)).strip()
        if n[0] in '-' or n.isnumeric():
            n = float(n)
            ok = True
        else:
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
        if ok:
            break
    return n


def leiarealv2(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31m MENSAGEM \033[m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n