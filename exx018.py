import math
n = float(input('digite o ângulo: '))
s= math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))

print('O ângulo de {} tem:\nSENO de {:.2f}\nCOSSENO de {:.2f}\nTANGENTE de {:.2f}'.format(n, s, c,t))
