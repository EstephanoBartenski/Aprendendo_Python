# análise de dados do grupo
continuar = 'S'
sexo = ' '
pessoa18 = homens = mulheres20 = 0
while True:
    while continuar == 'S':
        print(' {}\n'
              ' CADASTRE UMA PESSOA\n'
              ' {}'.format('-' * 19, '-' * 19))
        idade = int(input('Idade: '))
        if idade >= 18:
            pessoa18 += 1
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        while sexo not in 'MF':
            sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres20 += 1
        continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N] ')).upper().strip()[0]
    break
print(f'\n'
      f'Total de pessoas com mais de 18 anos: {pessoa18}. \n'
          f'Ao todo temos {homens} homens cadastrados. \n'
          f'E temos {mulheres20} mulheres com menos de 20 anos.')