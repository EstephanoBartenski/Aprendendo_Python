# tabuada 3.0
cont = op = 0
num = int(input('Quer ver a tabuada de qual valor? '))
while num >= 0:
    print('-----------------')
    while True:
        cont += 1
        result = num * cont
        print(f'{num} x {cont} = {result}')
        if cont > 9:
            print('-----------------')
            cont = 0
            break
    num = int(input('Quer ver a tabuada de qual valor? '))
print('Programa Tabuada encerrado. Volte sempre!')

# outra forma (não esqueça que se você souber o limite de algo,
# tente usar o for, que provavelmente será mais prático
'''while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 10)
    for c in range(0,11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 10)
print('Programa Tabuada encerrado. Volte sempre!')'''
