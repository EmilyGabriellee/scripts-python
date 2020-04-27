distancia = float(input("qual a distancia da sua viagem?"))
print("voc~e sta prestes a a fazer uma viagem de {}km.".format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("e o preço da sua viagem sera R${:.2f}".format(preço))