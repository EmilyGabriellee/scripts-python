peso = float(input("qual o seu peso? "))
altura = float(input("qual o sua altura? "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("voce esta abaixo do peso normal")
elif 18.5 <= imc < 25:
    print("parabens voce esta na faixa de peso normal")
elif 25 <= imc < 30:
    print(" voce esta em sobrepeso ")
elif 30 <= imc < 40:
    print(" voce esta em obesisade ")
elif imc >= 40:
    print("voce esta na obesidade morbita, cuidado!")

