def calculadora(n1, n2, operador):
    if operador == '+':
       print( n1 + n2)
    elif operador == '-':
       print( n1 - n2)
    elif operador == '*':
        print(n1 * n2)
    else:
       print( n1 / n2)


n1 = int(input("Digite um número: "))

while True:
    operador= input("Digite o operador válido (+, -, *, /): ")
    if operador == '+' or operador == '-' or operador == '*' or operador == '/':
        break

n2 = int(input("Digite outro número: "))

calculadora(n1, n2, operador)
