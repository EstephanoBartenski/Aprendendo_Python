# validando entrada de dados em python
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
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if ok:
            break
    return n


# programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')