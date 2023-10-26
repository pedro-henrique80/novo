ano = int(input("Digite o ano q você nasceu: "))
idade = 2023 - ano #atualmente
if idade == 18:
    print('Está na hora de se alistar. ')
elif idade < 18:
    print(f'Faltam apenas {(18 - idade)} anos para você se alistar.')
else: 
    print(f'Já passou o prazo de alistamento! Já passaram-se {(idade - 18)} anos.')