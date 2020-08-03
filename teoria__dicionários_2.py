estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
print()
for e in brasil:
    for v in e.values():
        print(v, end=' ') #esse espaço aqui dentro separa as siglas
    print() #isso faz pular de linha pra cada iteração