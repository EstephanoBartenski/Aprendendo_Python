# número por extenso
npot = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
     'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
     'dezenove', 'vinte')
neng = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
     'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
     'nineteen', 'twenty')
nesp = ('uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez',
     'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho',
     'diecinueve', 'veinte')
nita = ('une', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove', 'dieci',
     'undici', 'dodici', 'tredici', 'quattordici', 'quindici', 'sedici', 'diciassette', 'diciotto',
     'diciannove', 'venti')
nale = ('eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn',
     'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn',
     'neunzehn', 'zwanzig')

while True:
    num = 0
    num = int(input('Digite um número inteiro entre 1 e 20: '))
    while num < 1 or num > 20:
        num = int(input('Tente novamente. Digite um número inteiro entre 1 e 20: '))
    idioma = 6
    while idioma < 1 or idioma > 5:
        idioma = int(input('Escolha um idioma:\n'
                           '[ 1 ] PORTUGUÊS\n'
                           '[ 2 ] INGLÊS\n'
                           '[ 3 ] ESPANHOL\n'
                           '[ 4 ] ITALIANO\n'
                           '[ 5 ] ALEMÃO\n'
                           ''))
    if idioma == 1:
        print(f'Você digitou o número {npot[num-1]}.')
    if idioma == 2:
        print(f'You typed number {neng[num-1]}.')
    if idioma == 3:
        print(f'Ingressaste el número {nesp[num-1]}.')
    if idioma == 4:
        print(f'Hai inserito il numero {nita[num-1]}.')
    if idioma == 5:
        print(f'Vous avez entré le numéro {nale[num-1]}.')
    continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continua in 'N':
        print('PROGRAMA ENCERRADO! Volte sempre')
        break