import random
print('\033[1;33;40m=-=' * 10)
print('\033[1;35m         JOGO - JOKENPÔ')
print('\033[1;33;40m=-=\033[m' * 10)

jogador = str(input('pedra, papel ou tesoura?:  ')).lower().strip()
computador =['pedra', 'papel', 'tesoura']
escolha_do_pc = random.choice(computador)

if jogador == 'pedra' and escolha_do_pc== 'tesoura':
    print(f'\033[1;32mVOCÊ GANHOU! EU ESCOLHI {escolha_do_pc.upper()}\033[m')
elif jogador == 'tesoura' and escolha_do_pc == 'papel':
    print(f'\033[1;32mVOCÊ GANHOU! EU ESCOLHI {escolha_do_pc.upper()}\033[m')
elif jogador == 'papel' and escolha_do_pc == 'pedra':
    print(f'\033[1;32mVOCÊ GANHOU! EU ESCOLHI {escolha_do_pc.upper()}\033[m')
elif jogador == escolha_do_pc:
    print('\033[1;33mEMPATE! TENTE NOVAMENTE!')
else:
    print(f'\033[1;31mVOCÊ PERDEU!! EU ESCOLHI {escolha_do_pc.upper()} HAHAHAHA\033[m')