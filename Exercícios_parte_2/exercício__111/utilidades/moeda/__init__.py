from ex097 import escreva


def moeda(n):
    v = f'R${n:.2f}'.replace('.', ',')
    return v


def resumo(n=0, a=0, d=0):
    v0 = moeda(n)
    v1 = dobro(n, True)
    v2 = metade(n, True)
    v3 = aumentar(n, a, True)
    v4 = diminuir(n, d, True)
    escreva('RESUMO DO VALOR')
    print(f'Preço analisado: \t{v0:>6}')
    print(f'Dobro do preço: \t{v1:>6}')
    print(f'Metade do preço: \t{v2:>6}')
    print(f'{a}% de aumento: \t{v3:>6}')
    print(f'{d}% de redução: \t{v4:>6}')
    print('-' * 29)


def aumentar(n=0, p=0, moeda=False):
    v = n * (1 + p / 100)
    if moeda:
        v = f'R${v:.2f}'.replace('.', ',')
    return v


def diminuir(n=0, p=10, moeda=False):
    v = n - (n * (p / 100))
    if moeda:
        v = f'R${v:.2f}'.replace('.', ',')
    return v


def dobro(n=0, moeda=False):
    v = n * 2
    if moeda:
        v = f'R${v:.2f}'.replace('.', ',')
    return v


def metade(n=0, moeda=False):
    v = n / 2
    if moeda:
        v = f'R${v:.2f}'.replace('.', ',')
    return v