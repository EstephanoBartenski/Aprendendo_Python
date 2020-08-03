# tuplas com times de futebol
cores = {'limpa': '\033[m',
         'branco': '\033[1;30m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'ciano': '\033[1;36m',
         'cinza': '\033[1;37m'}
classificação = ('Liverpool', 'M. City', 'Man. United', 'Chelsea', 'Leicester City', 'Wolves', 'Spurs',
                 'Sheffield United', 'Burnley', 'Arsenal', 'Everton', 'Southampton', 'Newcastle', 'Crystal Palace',
                 'West Ham', 'Brighton', 'Aston Villa', 'Watford', 'Bournemouth', 'Norwich')
print('{}\n'
      '             {}PREMIER LEAGUE 2019/2020{}\n'
      '{}\n'
      ''.format('--=--' * 10, cores['vermelho'], cores['limpa'], '--=--' * 10))
print('[ A ] Top 4\n'
      '[ B ] Bottom 3\n'
      '[ C ] Alphabetic order\n'
      '[ D ] World Champions\n'
      '[ E ] Everton\n'
      '[ F ] Classificação\n'
      '')
opção = ''
opção = str(input('ESCOLHA UMA OPÇÃO: ')).upper().strip()[0]

while opção not in 'ABCDEF':
    opção = str(input('ESCOLHA UMA OPÇÃO: ')).upper().strip()[0]
if opção in 'A':
    print('{}{}{}'.format(cores['azul'], classificação[0:4], cores['limpa']))
if opção in 'B':
    print('{}{}{}'.format(cores['amarelo'], classificação[-3:], cores['limpa']))
if opção in 'C':
    for time in sorted(classificação):
        print(time)
if opção in 'D':
    print('{}{}{}'.format(cores['vermelho'], classificação[0].upper(), cores['limpa']))
if opção in 'E':
    print('Everton está na {}ª posição lmao'.format((classificação.index('Everton')) + 1))
if opção in 'F':
    cont = 1
    for time in classificação:
        print(f'{cont}º {time}')
        cont += 1
