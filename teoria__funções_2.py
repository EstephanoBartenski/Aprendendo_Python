# parâmetros opcionais
def soma(a=0, b=0, c=0):
    """
    → Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor.
    :param b: segundo valor.
    :param c: terceiro valor.
    :return: sem retorno.
    → Criado por Estephano Bartenski.
    """
    s = a + b + c
    print(f'A soma vale {s}.')



# programa principal
soma(8, 21, 2)
soma(2, 33)
soma(7)
soma()
soma(c=45, b=2)
print()

