velocidade = float(input("qual a velocidade do carro atualmente?"))
if velocidade > 80:
    print('MULTADO! você ULTRAPASSOU o limite que é de 80k/h')
    multa = (velocidade-80) * 7
    print("voce deve pagar uma multa de R${:.2f}".format(multa))
else:
    print("tenha um bom dia! dirija com segurança!")

