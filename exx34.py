salário = float(input('digite seu salário: '))


if salário > 1250.00:
    x = (salário * 0.10) + salário
else: 
    x = (salário * 0.15) + salário

print(x)