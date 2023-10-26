massa = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura: '))

imc = massa / (altura ** 2)

if imc < 18.5:
    print(f'Abaixo do peso: {imc:.2f}')
elif imc >= 18.5 and imc < 25:
    print(f'Peso ideial: {imc:.2f}')
elif imc >= 25 and imc < 30:
    print(f'Sobrepeso: {imc:.2f}')
elif imc >=30 and imc < 40:
    print(f'Obesidade: {imc:.2f}')
else:
    print(f'Obesidade mórbida. {imc:.2f}')