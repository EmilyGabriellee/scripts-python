salario = float(input("Qual o salario do funcionario? "))
if salario <= 1254:
    novo = salario * (salario * 15 / 100)
else:
    novo = salario * (salario * 10 / 100)
print("quem ganhava R${:.2f} passa a ganhar R${:.2f}!".format(salario, novo))