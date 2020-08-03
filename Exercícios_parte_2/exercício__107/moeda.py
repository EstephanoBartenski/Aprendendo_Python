# módulo


def aumentar(n, p=10):
    v = n * (1 + p / 100)
    return v


def diminuir(n, p=10):
    v = n - (n * (p / 100))
    return v


def dobro(n):
    v = n * 2
    return v


def metade(n):
    v = n / 2
    return v