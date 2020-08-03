def titulo(msg):
    print('-' * 30)
    print(f'        {msg}')
    print('-' * 30)


def lin():
    print('-' * 30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


def contador(* num):
    for v in num:
        print(f'{v}', end=' ')
    print('FIM!')


def contador2(* num):
    print(f'Recebi os valores {num} e são, ao todo, {len(num)} valores.')


def somavarios(* num):
    s = 0
    for n in num:
        s += n
    print(f'Somando os valores {num} temos {s}.')


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


# programa principal
titulo('OLÁ GANHAFOTO!')
soma(10, 30)
lin()
soma(a=10, b=30)
lin()
soma(b=30, a=10)
lin()
contador(1, 3, 6, 7, 8)
lin()
contador(99, 4888)
lin()
contador2(2, 6, 7, 8)
lin()
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
lin()
somavarios(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lin()