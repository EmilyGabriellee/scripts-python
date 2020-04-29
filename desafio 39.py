from datetime import date
atual = date.today().year
nasc = int(input("qual foi o ano de nascimento: "))
idade = atual - nasc
print("quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
if idade == 18:
    print("voce tem que se alistar imediatamente!")
elif idade < 18:
    saldo = 18 - idade
    print(" faltam {} anos  para o alistamento".format(saldo))
    ano = atual + saldo
    print("seu alistamento vai ser em {}".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("voce ja deveria ter se alistado ha {} anos ".format(saldo))
    ano = atual -  saldo
    print("seu alistamento foi em {}".format(ano))