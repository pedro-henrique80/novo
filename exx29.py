v = int(input('Digite a velocidade do carro em km/h: '))

if v > 80: 
    print(f'Você foi multado! Sua multa é de: {(v - 80) * 7} reais.')
else: 
    print(f'Você está dentro dos limites!')