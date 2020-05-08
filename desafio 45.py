from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('-='*18)
print('=- PEDRA -=- PAPEL -=- TESOURA -=')
print('-='*18)
print('''SUAS OPÇÕES SÃO :
[0]  PEDRA
[1]  PAPEL
[2]  TESOURA ''')
jogador = int(input('qual a sua jogada?'))
print('-='*18)
print("o computador escolheu {}".format(itens[computador]))
print("o jogador escolheu {}".format(itens[jogador]))
print('-='*18)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('\033[1;31mJOGADA INVALIDA!!!!!\033[m')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('\033[1;31mJOGADA INVALIDA!!!!!\033[m')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('\033[1;31mJOGADA INVALIDA!!!!!\033[m')
print('-=' * 18)
