s = int(input('Digite a distãncia a ser percorrida: '))

if s <= 200: 
    p = 0.50
else: 
    p = 0.45
print(f'O valor a ser pago é {s * p}')