# criando um menu de opções
from time import sleep
n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite mais um número: '))
print('     [ 1 ] somar\n'
      '     [ 2 ] multiplicar\n'
      '     [ 3 ] maior\n'
      '     [ 4 ] novos números\n'
      '     [ 5 ] sair do programa')
opção = int(input('>>>>> Qual é a sua opção? '))
while opção !=5:
    if opção > 5 or opção == 0:
        print('Opção inválida. Tente novamente!')
    if opção == 1:
        soma = n1+n2
        print('A soma de {:.2f} com {:.2f} resulta em {:.2f}.'.format(n1, n2, soma))
    elif opção == 2:
        multi = n1*n2
        print('A multiplicação de {:.2f} com {:.2f} resulta em {:.2f}.'.format(n1, n2, multi))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {:.2f} e {:.2f} é {:.2f}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    sleep(1)
    print('-==-'*8)
    print('     [ 1 ] somar\n'
          '     [ 2 ] multiplicar\n'
          '     [ 3 ] maior\n'
          '     [ 4 ] novos números\n'
          '     [ 5 ] sair do programa')
    opção = int(input('>>>>> Qual é a sua opção? '))
if opção == 5:
    print('Finalizando...')
    sleep(1)
    print('-==-'*8)
    print('Fim do programa. Volte sempre!')