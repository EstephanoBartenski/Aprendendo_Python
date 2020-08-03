# a ideia aqui é cadastrar varios alunos e pedir uma lista com os aprovados, reprovados e em recuperação
print('--' * 17)
print('        CADASTRO DE NOTAS')
print('--' * 17)
aluno = dict()
cadastro = list()
while True:
    aluno['nome'] = str(input('Nome: ')).strip().capitalize()
    aluno['med'] = float(input('Média de {}: '.format(aluno['nome'])))
    print()
    print(f' - O nome é {aluno["nome"]}.\n'
          f' - A média é {aluno["med"]:.2f}.')
    if aluno['med'] >= 7:
        print(' - Situação: APROVADO!')
        aluno['situação'] = 'aprovado'
    elif 5 <= aluno['med'] < 7:
        print(' - Situação: RECUPERAÇÃO!')
        aluno['situação'] = 'recuperação'
    else:
        print(' - Situação: REPROVADO!')
        aluno['situação'] = 'reprovado'
    cadastro.append(aluno.copy())
    print()
    resp = str(input('Cadastrar mais uma nota? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print()
print(' -- FORMAS DE MOSTRAR -- ')
for i in range(0, len(cadastro)):
    print(cadastro[i])
print('--' * 40)
for i in cadastro:
    for v in i.values():
        print(v, end=' ')
    print()
print('--' * 40)
