# função para fatorial


def fatorial(n, show=False):
    """
    → Calcula o fatorial de um número.
    :param n: Número a ser calculado.
    :param show: (opcional) Mostra o calculo por extenso.
    :return: Valor do fatorial de um número.
    → Criado por Estephano Bartenski. (27/07/20)
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            if c == 1:
                print(' = ', end='')
        f = f * c
    return f


# programa principal
print(fatorial(5, show=True))  # show true é para mostrar com o cálculo, além do resultado
print(fatorial(5))  # show False ficou como padrão
help(fatorial)