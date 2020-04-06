print("===================================")
print("Calculadora de primos")
while True:
    num = int(input('Digite um numero para verificaçao ou 0 para cancelar!:'))
    if num == 0:
        print('Encerrando programa...')
        break
    counter = 0
    i = int(num)
    for i in range(num, 0, -1):
        if num % i == 0:
            counter = counter + 1
            if counter > 2:
                break
    if counter > 2:
        print('O número não é Primo.')
    else:
        print('O número é Primo.')
    print('===================================')