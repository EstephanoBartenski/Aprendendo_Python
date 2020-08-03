# aqui vou deixar a solução do Guanabara
# repare como ele fez em duas linhas a soma dos pares kkkkk mas funcionou o meu, fodase
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = float(input(f'Digite um valor para [{l}, {c}]: '))
print('--' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:.2f} ]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('--' * 30)
print(f'A soma dos valores pares é {somapar:.2f}.')
for l in range(0, 3):
    somacol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacol:.2f}.')
for c in range(0, 3):
    if c ==0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior:.2f}.')