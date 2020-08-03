# progressão aritmética 2.0 (10 primeiros termos) ex051 foi o usando o for
print('-=-=-=-=-=-=-=-=-\n'
      '  GERADOR DE PA\n'
      '-=-=-=-=-=-=-=-=-')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
an = a1
cont = 1
mais = 10
tot = 0
while mais != 0:
    tot += mais
    while cont <= tot:
        print('{} -> '.format(an), end='')
        cont += 1
        an += r
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM\n'
      'Progressão finalizada com {} termos ao todo.'.format(tot))
