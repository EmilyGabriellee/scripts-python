def calculadora(n1, n2, operador):
    if operador == '+':
       print( n1 + n2)
    elif operador == '-':
       print( n1 - n2)
    elif operador == '*':
        print(n1 * n2)
    else :
       print( n1 / n2)

Emily = int(input("Digite um número: "))
Cintia= input("Digite o operador (+, -, *, /): ")
Wesley = int(input("Digite outro número: "))

calculadora(Emily, Wesley, Cintia)
