# lista composta e análise de dados
# peso <= 70 é leve, peso >= 100 é pesada, entre 70 e 100 não é nada
lista = list()
dados = list()
maisp = list()
menosp = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso [Kg]: ')))
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Deseja cadastrar mais uma pessoa? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for c in lista:
    if c[1] <= 70:
        menosp.append(c[0])
    if c[1] >= 100:
        maisp.append(c[0])
nomes = list()
pesos = list()
for v in lista:
    nomes.append(v[0])
    pesos.append(v[1])
menor = min(pesos)
maior = max(pesos)
print('--' * 50)
print(f'Foram cadastradas {len(lista)} pessoas.')
if menosp != []:
    print(f'As pessoas com peso igual ou abaixo de 70 Kg foram {menosp}.')
if maisp != []:
    print(f'As pessoas com peso igual ou acima de 100 Kg foram {maisp}.')
menor = pesos.index(min(pesos))
maior = pesos.index(max(pesos))
print(f'O menor peso foi {min(pesos)} Kg, de {lista[menor][0]}.')
print(f'O maior peso foi {max(pesos)} Kg, de {lista[maior][0]}.')
print('--' * 50)

