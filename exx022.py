nome = input('Digite seu nome: ')

primeiras_letras = nome.split()
print(f"seu nome maiúsculo é: {nome.upper()}")
print(f"Seu nome minúsculo é: {nome.lower()}")
print(f"A quantidade de letras no seu nome é: {len(nome) - nome.count(' ')}")
print(f"A quantidade de letras no seu primeiro nome é: {len(primeiras_letras[0])}")