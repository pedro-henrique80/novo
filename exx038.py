x1 = int(input("Digite o primeiro número: "))
x2 = int(input("Digite o segundo número: "))

if x1 > x2:
    print(f"O maior valor é {x1}")
elif x2 > x1: 
    print(f"O maior valor é {x2}")
else:
    print("Os dois são iguais.")