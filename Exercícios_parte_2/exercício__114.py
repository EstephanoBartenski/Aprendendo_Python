# site acessível?
from urllib import request, error

try:
    site = request.urlopen('https://www.twitch.tv/')
except error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site com sucesso.')