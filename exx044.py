preço_normal = float(input('Digite o preço normal dele: '))
condição1 = str(input('Sua forma de pagamento é à vista ou parcelado? ')).lower()
condição3 = int(input('Caso você queira parcelar, em quantas vezes quer dividir(caso não queria, apenas digite 1)? '))
condição2 = str(input('Dinheiro, Cartão ou Cheque? ')).lower()



if condição1 == 'à vista' and condição2 == 'dinheiro' or condição2 == 'cheque':
    print(f'O valor recebeu 10% de desconto e ficou {preço_normal - preço_normal * 0.10} reais')
elif condição1 == 'à vista' and condição2 == 'cartão':
    print(f'O valor recebeu 5% de desconto e ficou {preço_normal - preço_normal * 0.05} reais')
elif condição1 == 'parcelado' and condição3 >= 2 and condição3 < 3:
    print(f'O preço permanece o mesmo: {preço_normal}')
elif condição1 == 'parcelado' and condição3 >= 3:
    print(f'Hávera um juros de 20% e ficará {preço_normal + (preço_normal * 0.20)}')
else: 
    print('Repita, e coloque valores válidos.')

