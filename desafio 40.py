nota1 = float(input("primeira nota:"""))
nota2 = float(input("segunda  nota:"""))
media = (nota1 + nota2) / 2
print("tirando {:.1f}a media a media do aluno e {:.1f}".format(nota1, nota2, media))
if media >= 5 and media < 7:
    print("on aluno esta de recuperaçao.")
elif media < 5:
    print("o aluno esta reprovado.")
else:
    print("o aluno esta aprovado.")