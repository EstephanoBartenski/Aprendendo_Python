# retorno de valores
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


# programa principal
valor = soma(8, 21, 2)
print(valor)
# ou
print(soma(8, 21, 2))
# isso torna possível:
r1 = soma(3, 6, 10)
r2 = soma(2, 4)
r3 = soma(21, 55)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')