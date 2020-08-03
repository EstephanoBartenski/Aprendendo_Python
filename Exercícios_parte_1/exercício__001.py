# OLÁ, MUNDO!
# import emoji
# print(emoji.emojize('\033[1;34mOlá, Mundo! :earth_americas:\033[m', use_aliases=True))
# nome = input('Diga-me quem és')
# print(emoji.emojize('Olá, {}{}{} :see_no_evil:'.format('\033[4;34m', nome, '\033[m'), use_aliases=True))

nome = 'Estephano'
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
