# catetos e hipotenusa
import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = math.sqrt(co**2+ca**2)
print('A hipotenusa deste triângulo retângulo irá medir {:.2f}'.format(h))

# há uma fórmula para a hipotenusa no math
print('A hipotenusa deste triângulo retângulo irá medir {:.2f}'.format(math.hypot(co, ca)))

