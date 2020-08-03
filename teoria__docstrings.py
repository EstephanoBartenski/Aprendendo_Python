def contador(i, f, p):
    """
    → Faz uma contagem e mostra na tela.
    :param i: início da contagem.
    :param f: final da contagem.
    :param p: passo da contagem.
    :return: sem retorno.
    → Função criada por Estephano Bartenski.
    """
    c = i
    while c <= f:
        print(f'{c} ', end=' ')
        c += p
    print('FIM!')


# programa principal
help(contador)