from datetime import date
atual = date.today().year
nascimento = int(input("ano de nascimento? "))
idade = atual - nascimento
print("o atleta tem {} anos.".format(idade))
if idade <= 9:
    print("classificassao: MIRIM ")
elif idade  <= 14:
    print("classificaçao: INFANTIL ")
elif idade  <= 19:
    print("classificaçao: JUNIOR ")
elif idade <= 25:
    print("classificaçao: SENIOR")
else:
    print("classificaçao: MASTER")