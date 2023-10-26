d = int(input('digite a quantidade de dias alugados: '))
km = float(input('digite o valor em km percorridos: '))

f =  (d * 60) + (km * 0.15)
print('o preço que você irá pagar é {:.2f}'.format(f))