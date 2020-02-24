altura = int(input("Qual a largura da parede? "))
largura = int(input("qual a largura da prede? "))
area = altura * largura
print("Você vai precisar de {} baldes de tintas para pintar uma área de {} metros.".format(area/2, area))