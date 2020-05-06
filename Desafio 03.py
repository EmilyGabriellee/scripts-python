aluno = input ("Digite o nome do aluno(a): ")
print("====== \033[1;33mN O T A S\033[m ======")
print("====== \033[1;36m{}\033[m ======".format(aluno))
print("==\033[1;31mMATERIAS\033[m== | ==\033[1;31mNOTAS\033[m==")

np = int(input("Português    | Digite a nota:  "))
nm = int(input("Matemática   | Digite a nota:  "))
ni = int(input("Inglês       | Digite a nota:  "))

print("A média final das notas do(a) aluno(a) \033[1;33m{}\033[m foi: \033[1;31m{}\033[m.".format(aluno, (np + nm + ni) / 3))