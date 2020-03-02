#print("----métedo matemático----")
#co = float(input("Qual o coprimento do cateto oposto? "))
#ca = float(input("Qual o comprimento cateto adjacente? "))
#hi = (co ** 2 + ca ** 2) **(1/2)
#print("a hiponenusa vai medir {:.2f}!".format(hi))

import math
print("----Utilizando biblioteca----")
co = float(input("Qual o comprimento do cateto oposto?"))
ca = float(input("Qual o comprimento do cateto adjacente?"))
hi = math.hypot(co, ca)
print("A hipotenusa vai medir {:.2f}!".format(hi))