import math

n1 = int(input("Digite um número:  "))

d1 = n1 * 2
d2 = n1 * 3
d3 = math.sqrt(n1)
print("o dobro de \033[1;33m{}\033[m é \033[1;31m{}\033[m, o triplo de \033[1;33m{}\033[m é \033[1;31m{}\033[m e a rsaiz quadrada de \033[1;33m{}\033[m é \033[1;31m{}\033[m!".format(n1, d1, n1, d2, n1, d3))