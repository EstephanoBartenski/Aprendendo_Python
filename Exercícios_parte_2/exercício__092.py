# cadastro de trabalhador em Python
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip().capitalize()
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Nº da Carteira de Trabalho (0 se não tem): '))
if dados['CTPS'] == 0:
    del dados['CTPS']
    for k, v in dados.items():
        print(f' - {k} = {v}', end=' ')
        print()
    print('Não tem carteira de trabalho.')
else:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário mensal: R$ '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
    print()
    for k, v in dados.items():
        print(f' - {k} = {v}', end=' ')
        print()

