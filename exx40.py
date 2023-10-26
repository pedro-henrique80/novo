nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
média = (nota_1 + nota_2) / 2

if média < 5.0:
    print('\033[1;31mREPROVADO!\033[m')
elif média >= 5.0 and média < 6.9:
    print('\033[1;33mRECUPERAÇÃO!\033[m')
else: 
    print('\033[1;32mAPROVADO!\033[m')
print(f'\033[1;35mSua nota foi {média}!\033[m')