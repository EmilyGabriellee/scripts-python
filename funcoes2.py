def calcula_temperatura (c):
    f = 9 * c / 5 + 32
    print("a temperatura de {}°C corresponde a {}°F".format(c, f))

temperatura = float(input("Quantos graus celsius está fazendo agora?"))
calcula_temperatura(temperatura)
