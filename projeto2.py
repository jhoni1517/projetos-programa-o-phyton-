nota_1= float(input("Digite a primeira nota: "))
nota_2= float(input("Digite a segunda nota: "))
nota_3= float(input("Digite a segunda nota: "))

total_notas= (nota_1+nota_2+nota_3)
print("A nota Total é:", total_notas)

resultado_final= (total_notas/3)

if resultado_final>6:
    print("Aluno aprovado!! ")

else:
    print("Aluno não atingiu a nota mínima! ")