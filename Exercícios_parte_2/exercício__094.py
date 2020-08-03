# unindo listas e dicionários
nomes = list()
idades = list()
mulheres = list()
cadastro = list()
temp = dict()
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nomes.append(nome)
    temp['nome'] = nome
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    temp['sexo'] = sexo
    if sexo in 'F':
        mulheres.append(nome)
    idade = int(input('Idade: '))
    idades.append(idade)
    temp['idade'] = idade
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cadastro.append(temp.copy())
    del temp['nome']
    del temp['sexo']
    del temp['idade']
    if resp in 'N':
        break
med = sum(idades) / len(idades)
maiores = list()
for c in range(0, len(cadastro)):
    if cadastro[c]['idade'] > med:
        maiores.append(cadastro[c])
print('--' * 30)
print(f'Ao todo foram cadastradas {len(nomes)} pessoas.')
print(f'A média de idade entre as cadastradas é de {med:.2f} anos.')
print(f'As mulheres cadastradas foram {mulheres}.')
if len(maiores) != 0:
    print(f'Lista das pessoas que estão com idade acimda da média do grupo:')
    print(f'     {maiores}')
else:
    print('Não há pessoas com peso acima da média do grupo.')
print(' <<< ENCERRADO >>> ')