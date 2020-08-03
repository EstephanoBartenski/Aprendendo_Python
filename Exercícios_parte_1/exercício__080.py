# lista ordenada sem repetições
valores = list()
for c in range(0, 5):
    if c == 0:
        n = int(input('Digite um número inteiro: '))
        print('Adicionado ao final da lista...')
        valores.append(n)
    if 0 < c < 5:
        n = int(input('Digite um número inteiro: '))
        if n in valores:
            print('Ops, já temos este número!')
        else:
            if n > max(valores):
                print('Adicionado ao final da lista...')
                valores.append(n)
            elif n < min(valores):
                print('Adicionado ao começo da lista...')
                valores.insert(0, n)
            else:
                if n < valores[1]:
                    print('Adicionado na posição 1 da lista...')
                    valores.insert(1, n)
                elif n < valores[2]:
                    print('Adicionado na posição 2 da lista...')
                    valores.insert(2, n)
                elif n < valores[3]:
                    print('Adicionado na posição 3 da lista...')
                    valores.insert(3, n)
                elif n < valores[4]:
                    print('Adicionado na posição 4 da lista...')
                    valores.insert(4, n)
print(valores)
