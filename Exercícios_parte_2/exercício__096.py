# função que calcula área
def cab():
    print('--' * 10)
    print('CONTROLE DE TERRENOS')
    print('--' * 10)


def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l} x {c} mede {a:.2f} m².')


# programa principal
cab()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
