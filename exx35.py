n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Pode formar triangulo.")
else:
    print("Não pode formar triangulo.")