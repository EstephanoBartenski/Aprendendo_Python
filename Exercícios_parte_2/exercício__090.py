# dicionários
print('--' * 17)
print('        CADASTRO DE NOTAS')
print('--' * 17)
aluno = dict()
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
print()
print(aluno)



# outra resolução:
'''aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['med'] = float(input(f'Média de {aluno["nome"]} '))
if aluno['med'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['med'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('--' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')'''