from datetime import date
ano = int(input("Que ano quer analisar? digite 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print("o ano {} É BISSEXTO!".format(ano))
else:
    print("o ano {} nao é BISSEXTO!".format(ano))