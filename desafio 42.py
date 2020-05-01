r1 = float(input("primeiro segimento: "))
r2 = float(input("segundo segimento: "))
r3= float(input("tercaeiro segimento: "))
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print("os segmentos acima podem formar um triangulo. ", end='')
    if r1 == r2 == r3:
        print("EQUILATERO!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISOSCELES")
else:
    print("os segimentos acima nao podem formar um triangulo. ")