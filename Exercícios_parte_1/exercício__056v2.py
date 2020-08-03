# a media de idade do grupo
# o homem mais novo
# quantas mulheres com mais de 18 anos
# considere todos os casos de respostas (só mulheres, só homens)
totp = 5
toti = 0
contmm = 0
ihnovo = 0
for pessoa in range(1, totp +1):
    print('----- {}ª PESSOA -----'.format(pessoa))
    p = str(input('NOME: ')).strip()
    i = int(input('IDADE: '))
    s = str(input('SEXO [M/F]: ')).strip().lower()
    toti += + i
    if i >= 18 and s in 'Ff':
        contmm += 1
    else:
        contmm == 0
    if pessoa == 1 and s in 'Mm':
        ihnovo = i
        nhnovo = p
    if i <= ihnovo and s in 'Mm':
        ihnovo = i
        nhnovo = p
media = toti / totp
print('A média das idades das pessoas foi de {:.1f}.'.format(media))
if ihnovo != 0:
    print('O homem mais novo tem {} anos e se chama {}.'.format(ihnovo, nhnovo))
if contmm != 0:
    print('Das pessoas informadas, há {} mulheres maiores de idade.'.format(contmm))
else:
    print('Nenhuma mulher foi informada.')
