n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Pode formar triangulo.")
    elif  n1 == n2 == n3:
        print('É um triangulo Equilátero. ')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('É um triangulo isóceles')
    else:
        print('É um triangulo escaleno')
    
elif n1 > n2 + n3 and n2 > n1 + n3 and n3 > n1 + n2:
    print("Não pode formar triangulo.")
