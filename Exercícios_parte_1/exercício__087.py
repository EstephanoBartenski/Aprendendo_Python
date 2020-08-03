# mais matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = float(input(f'Digite um valor para [{l}, {c}]: '))
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print()
soma3col = matriz[0][2] + matriz[1][2] + matriz[2][2]
maior2li = max(matriz[1])
print('--' * 30)
print(f'A soma dos valores da terceira coluna é {soma3col:.2f}.')
print(f'O maior valor da segunda linha é {maior2li:.2f}.')
copia = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for c in range(0, 3):
    copia[c] = matriz[0][c]
for c in range(0, 3):
    copia[c + 3] = matriz[1][c]
for c in range(0, 3):
    copia[c + 6] = matriz[2][c]
somapares = 0
for c in range(0, len(copia)):
    if copia[c] % 2 == 0:
        somapares += copia[c]
print(f'A soma dos valores pares é {somapares:.2f}.')
print('--' * 30)
