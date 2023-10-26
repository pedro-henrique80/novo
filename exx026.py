nome = str(input('Digite uma frase: ')).upper().strip()

print(f"A frase possui {nome.count('A')} letras A")
print(f"A primeira letra A aparece na posição: {nome.find('A')}")
print(f"A ultima letra A aparece na posição: {nome.rfind('A')}")