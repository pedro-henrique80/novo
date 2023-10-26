import random 
from time import sleep
x = [0, 1, 2, 3, 4, 5]
l = random.choice(x)

print(' O computador está pensando em um número... ')
f = int(input('Adivinhe qual número ele está pensando entre 0 e 5: '))
print('Analisando...')
sleep(2)
if f == l:
    print(f'você acertou! o valor realmente é {l}')
else:
    print(f'você errou, o valor era {l}')