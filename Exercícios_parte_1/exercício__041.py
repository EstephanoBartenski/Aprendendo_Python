# classificando atletas
from datetime import date
hoje = date.today().year
ano = int(input('Ano de nascimento: '))
idade = hoje-ano
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <=14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade == 20:
    print('Classificação: SÊNIOR')
elif idade > 20:
    print('Classificação: MASTER')
