# matriz em python
matriz = []
for c in range(0, 3):
    n = int(input(f'Digite um valor para [0, {c}]: '))
    matriz.append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para [1, {c}]: '))
    matriz.append(n)
for c in range(0, 3):
    n = int(input(f'Digite um valor para [2, {c}]: '))
    matriz.append(n)
print(f'[  {matriz[0]}  ][  {matriz[1]}  ][  {matriz[2]}  ]\n'
      f'[  {matriz[3]}  ][  {matriz[3]}  ][  {matriz[5]}  ]\n'
      f'[  {matriz[6]}  ][  {matriz[7]}  ][  {matriz[8]}  ]')

# outra forma, claramente melhor:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = intex0(input(f'Digite um valor para ({l}, {c}): '))
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print()