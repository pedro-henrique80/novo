from math import hypot
n = float(input('digite o primeiro cateto: '))
n2 = float(input('digite o segundo cateto: '))
h = hypot(n, n2)
print('o valor da hipotenusa é igual a: {:.2f}!'.format(h))