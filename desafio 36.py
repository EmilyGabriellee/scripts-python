casa = float(input("qual o valor da casa?"))
salario = float(input("qual o salario do comprador?"))
anos = int(input("quantos anos de financiamento?"))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print("para pagar uma casa de R${:.2f} em {} anos ".format(casa, anos), end="")
print("a prestaçao sera de R${:.2f}".format(prestaçao))
if prestaçao <= minimo:
    print("EMPRESTIMO pode ser CONCEDIDO!")
else:
    print("EMPRESTIMO NEGADO")