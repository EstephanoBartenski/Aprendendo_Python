# aprimorando os dicionários
jogadores = dict()
temp = dict()
gols = list()
time = list()
ind = 0
while True:
    resp = 'oi'
    gols.clear()
    temp.clear()
    temp['ind'] = ind
    ind += 1
    temp['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    temp['partidas'] = int(input(f'Quantas partidas {temp["nome"]} jogou? '))
    for i in range(1, temp['partidas'] + 1):
        gols.append(int(input(f' >>> Quantos gols na {i}ª partida? ')))
    temp['gols'] = gols[:]
    temp['totgols'] = sum(gols)
    jogadores['jogador'] = temp.copy()
    time.append(jogadores.copy())
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print()
print('--' * 45)
print(' (i) Nome           Partidas       Gols p/ partida     Total de gols')
print('--' * 45)
for c in range(0, len(time)):
    print(f'{time[c]["jogador"]["ind"]:^5}'
          f'{time[c]["jogador"]["nome"]:<15}'
          f'{time[c]["jogador"]["partidas"]:<15}'
          f'{str(time[c]["jogador"]["gols"]):<20}'
          f'{time[c]["jogador"]["totgols"]:<15}', end='')
    print()
print('--' * 45)
print()
while True:
    qual = int(input('Mostrar dados de qual jogador? '
                     '(escolha pelo índice) (99 p/ encerrar) '))
    if qual == 99:
        break
    while qual >= len(time) and qual != 99:
        print('ERRO! Não existe jogador com este código.')
        qual = int(input('Mostrar dados de qual jogador? '
                         '(escolha pelo índice) (99 p/ encerrar) '))
    if qual == 99:
        break
    print(f' >>> Levantamento do Jogador {time[qual]["jogador"]["nome"]}:')
    for i, v in enumerate(time[qual]["jogador"]["gols"]):
        print(f'     Na partida {i + 1} fez {v} gols.')
    print(f'Foi um total de {time[qual]["jogador"]["totgols"]} gols.')
