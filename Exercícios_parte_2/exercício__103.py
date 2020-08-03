# ficha do jogador
def artilheiro(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# programa principal
nome = str(input('Nome do jogador: ')).strip().capitalize()
gols = str(input('Número de gols: '))
if gols.isnumeric(): # melhor que usar o if com .type
    gols = int(gols)
else:
    gols = 0
if nome == '':
    artilheiro(gols=gols)
else:
    artilheiro(nome, gols)

