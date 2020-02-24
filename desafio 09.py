print("====== T A B U A D A ====== ")
n1 = int(input ("Digite um número: "))
print("~~~~~~ A tabuada de {} é: ~~~~~~".format(n1))

for i in range(1, 11, +1):
    print("{} x {} = {}".format(n1, i, n1 * i))

print("=========================")