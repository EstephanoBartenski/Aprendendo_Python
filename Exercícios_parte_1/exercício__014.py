# conversor de temperaturas
c = float(input('Insira a temperatura em ºC:'))
f = c*(9/5)+32
k = c+273.15
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF e {}K'.format(c, f, k))
