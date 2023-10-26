idade = int(input('Digite sua idade: '))

if idade <= 9:
    print('Categoria Mirim.')
elif idade <= 14: 
    print('Categoria Infantil.')
elif idade <= 19:
    print('Categoria Junior.')
elif idade <= 20:
    print('Categoria Senior.')
else:
    print('Categoria Master.')