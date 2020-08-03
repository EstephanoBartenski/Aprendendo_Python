# aquele clássico da média de notas
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
n1 = float(input('Digite a nota do primeiro bimestre: '))
n2 = float(input('Digite a nota do segundo bimestre: '))
n3 = float(input('Digite a nota do terceiro bimestre: '))
n4 = float(input('Digite a nota do quarto bimestre: '))
media = (n1+n2+n3+n4)/4
sem1 = (n1+n2)/2
sem2 = (n3+n4)/2
if media >= 7:
    print('Parabéns! Você foi {}APROVADO{}\n'
          'Sua média final foi {:.2f} nesta matéria!'.format(cores['verde'], cores['limpa'], media))
else:
    print('Sua média foi {:.2f} e você ficou para exame!'.format(media))
    quanto = 15-(sem1+sem2)
    print('Para passar com exame você precisará tirar no mínimo {:.2f}'.format(quanto))
    ne = float(input('Quanto você tirou no exame? '))
    nf = (ne+sem1+sem2)/3
    if nf >= 5:
        print('Você foi {}APROVADO{} com média final de {:.2f}'.format(cores['verde'], cores['limpa'], nf))
    else:
        print('Vish... Parece que você ficou de {}DEPENDÊNCIA{}.\n'
              'Sua nota final com exame foi de {:.2f}.\n'
              'Estude mais da próxima vez!'.format(cores['vermelho'], cores['limpa'], nf))
