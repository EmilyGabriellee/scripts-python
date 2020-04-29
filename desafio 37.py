num = int(input("digite um numero inteiro qualquer: "))
print('''escolha uma das bases para converter: 
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opçao = int(input("sua opiçoa: "))
if opçao == 1:
    print("{} convertido para binario e igual a {}".format(num, bin(num)[2:]))
elif opçao == 2:
    print("{} convertido para octal e igual a {}".format(num, oct(num)[2:]))
elif opçao == 3:
    print("{} convertido para hexadecimal e igual a {}".format(num, hex(num)[2:]))
else:
    print("opçao invalida, tente novamente")