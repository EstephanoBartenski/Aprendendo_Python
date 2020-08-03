'''pessoal = [['Joana', 33], ['Marcelo', 45], ['Otávio', 50], ['Jorge', 12], ['Bárbara', 14]]
print(pessoal[1])
print(pessoal[1][1])
print(pessoal[1][0])

print()

turma = list()
turma.append(pessoal[:])
print(turma)
print(turma[0])
print(turma[0][4])
print(turma[0][4][1])'''''

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
print()
totmaior = totmenor = 0
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor +=1
print(f'Há {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade.')

