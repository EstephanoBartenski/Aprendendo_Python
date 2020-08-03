# alistamento militar
from datetime import date
hoje = date.today().year
sexo = input('Qual o seu sexo (M ou F)?').strip()
if sexo == 'F' or sexo == 'f' or sexo == 'feminino' or sexo == 'Feminino' or sexo == 'FEMININO':
    print('No Brasil, o alistamento é obrigatório apenas para homens.\nLogo, você não precisa se alistar.')
else:
    ano = int(input('Ano de nascimento: '))
    idade = hoje-ano
    falta = 18-idade
    seráem = falta+hoje
    print('Quem nasceu em {} tem {} anos agora em {}.'.format(ano, idade, hoje))
    if idade == 18:
        print('Você precisa se alistar ainda este ano!')
    elif idade > 18:
        print('Você já fez o alistamento militar!')
    elif idade < 18:
        print('Ainda faltam {} anos para seu alistamento, que ocorrerá em {}'.format(falta, seráem))
