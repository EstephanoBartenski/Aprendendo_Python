# progressão artimética
print('='*30)
print('     10 TERMOS DE UMA PA       ')
print('='*30)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
for c in range(0, 10):
    c = a1 + c * r
    print(c, end=' ')
    print('->', end=' ')
print('ACABOU')

# refazendo
# an = a1 + (n - 1) * r
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n = 0
for n in range(1, 11):
    an = a1 + (n - 1) * r
    n += 1
    print('{} --> '.format(an), end='')
print('FIM', end='')
