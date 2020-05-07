print("{:=^40}".format(' \033[1;30mLOJAS MILY-CHAN\033[m '))
preço = float(input('qual o preço das compras? R$'))
print('''FORMA DE PAGAMENTO
[1] á vista dinheiro/cheque;
[2] á vista cartao;
[3] 2x no cartao;
[4] 3x ou mais no cartao.''')
opçao = int(input(':'))
if opçao == 1:
    total = preço - (preço * 10 / 100 )
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela =  total / 2
    print('sua compra sera parcelada em 2x de R${:.2f} \033[1;31mSEM JUROS\033[m'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('quantas parcelas? '))
    parcela = total / totparc
    print('sua compra sera parcelada em {}x de R${:.2f} \033[1;31mCOM JUROS\033[m'.format(totparc, parcela))
else:
    total = 0
    print('\033[1;31m OPÇAO INVALIDA DE PAGAMENTO, TENTE NOVAMENTE!!!\033[m')
print('sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))

