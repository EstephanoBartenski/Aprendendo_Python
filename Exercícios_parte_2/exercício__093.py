# cadastro de jogador de futebol
dados = dict()
gols = list()
dados['nome'] = str(input('Nome do(a) jogador(a): ')).strip().capitalize()
cont = 0
i = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for i in range(1, i + 1):
    gol = (int(input(f'     Quantos gols marcou {i}ª partida? ')))
    cont += gol
    gols.append(gol)
dados['gols'] = gols
dados['total'] = cont
print()
print('--' * 30)
print(dados)
print('--' * 30)
print()
print('--' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('--' * 30)
print()
print('--' * 30)
print(f'O jogador {dados["nome"]} jogou {i} partidas:')
for i in range(0, len(gols)):
    print(f'    >>> Na partida {i}, fez {gols[i]} gol(s).', end=' ')
    print()
print(f'Foi um total de {cont} gol(s).')
print('--' * 30)
