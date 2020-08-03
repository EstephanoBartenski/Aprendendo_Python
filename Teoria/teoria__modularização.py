def fatorial(n):
    """
    → Retona o fatorial de um número inteiro.
    :param n: O número ter o seu fatorial calculado.
    :return: O resultado do fatorial.
    → Criado por Estephano Bartenski (28/07/20).
    """
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')