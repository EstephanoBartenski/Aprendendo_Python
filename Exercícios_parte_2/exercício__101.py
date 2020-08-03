# funções para votação


def voto(ano):
    #print('Descubra se seu voto é opcional ou obrigatório.')
    #ano = int(input('Em que ano você nasceu? '))
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        facult = (18 - idade) + date.today().year
        return f'Com {idade} anos você ainda NÃO ESTÁ HABILITADO a votar!\n' \
               f'Seu voto será facultativo quando completar 16 anos, ou seja, a partir de {facult}.'
    else:
        ler = str(input('Você é alfabetizado? [S/N] ')).strip().upper()[0]
        if ler in 'N':
            return 'Por ser analfabeto, seu voto é OPCIONAL!'
        gringo = str(input('Você é estrangeiro? [S/N] ')).strip().upper()[0]
        if gringo in 'S':
            return 'Por ser estrangeiro residente no país, você NÃO ESTÁ HABILTIADO a votar!'
        politicos = str(input('Está em pleno exercício dos seus direitos políticos? [S/N] ')).strip().upper()[0]
        if politicos in 'N':
            return 'Por não ter pleno exercícios dos seus direitos políticos, você NÃO ESTÁ HABILITADO a votar!'
        elif 16 <= idade < 18:
            return f'Com {idade} anos seu voto é OPCIONAL!'
        elif 18 <= idade < 70:
            return f'Com {idade} anos seu voto é OBRIGATÓRIO!'
        elif idade >= 70:
            return f'Com {idade} anos seu voto é OPCIONAL!'


# programa principal
ano = int(input(('Descubra se seu voto é opcional ou obrigatório.\n'
                'Em que ano você nasceu? ')))
print(voto(ano))