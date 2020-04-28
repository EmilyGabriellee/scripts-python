a = int(input("primeiro valor:"))
b = int(input("segundo valor:"))
c = int(input("terceiro valor:"))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = b
print("o menor valor é {}.".format(menor))
print("o maior valor é {}.".format(maior))