# analisando triângulos 2.0
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (a+b)>c and (a+c)>b and (b+c)>a:
    print('Podem formar um triângulo!')
    if a == b == c:
        print('Este triângulo será EQUILÁTERO!')
    elif a == b and a != c and b != c:
        print('Este triângulo será ISÓSCELES!')
    elif a != b and a != c and b != c:
        print('Este triângulo será ESCALENO!')
else:
    print('Estes segmentos não podem formar um triângulo!')



