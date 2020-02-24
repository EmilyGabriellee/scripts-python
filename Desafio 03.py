aluno = input ("Digite o nome do aluno(a): ")
print("====== N O T A S ======")
print("====== {} ======".format(aluno))
print("==MATERIAS== | ==NOTAS==")

np = int(input("Português    | Digite a nota:  "))
nm = int(input("Matemática   | Digite a nota:  "))
ni = int(input("Inglês       | Digite a nota:  "))

print("A média final das notas do(a) aluno(a) {} foi: {}.".format(aluno, (np + nm + ni) / 3))