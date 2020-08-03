# índice de massa corporal
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
peso = float(input('Digite seu PESO em kg: '))
altura = float(input('Digite sua ALTURA em m: '))
imc = peso / (altura**2)
print('Seu IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('{}ABAIXO DO PESO{}'.format(cores['ciano'], cores['limpa']))
elif 18.5 <= imc <= 24.9:
    print('{}PESO NORMAL{}'.format(cores['ciano'], cores['limpa']))
elif 25 <= imc <= 29.9:
    print('{}SOBREPESO{}'.format(cores['ciano'], cores['limpa']))
elif 30 <= imc <= 34.9:
    print('{}OBESIDADE Grau 1{}'.format(cores['ciano'], cores['limpa']))
elif 35 <= imc <= 39.9:
    print('{}OBESIDADE Grau 2{}'.format(cores['ciano'], cores['limpa']))
elif imc >= 40:
    print('{}OBESIDADE Grau 3{}'.format(cores['ciano'], cores['limpa']))
