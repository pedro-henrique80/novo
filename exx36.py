valor = float(input("\033[1;36mDigite o valor da casa: \033[m"))
salário = float(input("\033[1;35migite o valor do seu salário: \033[m"))
anos = int(input("\033[1;31mEm quantos anos será pago? \033[m"))
prestação = (valor / anos / 12)
print(f'Para pagar   uma casa de R${valor:.2f} em {anos} a prestação será de R${(prestação):.2f}.')
if prestação <= 0.30 * salário:
    print('EMPRÉSTIMO APROVADO! ')
else:
    print('EMPRÉSTIMO NEGADO! ')