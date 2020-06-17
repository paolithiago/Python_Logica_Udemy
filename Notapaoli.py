#Receber 6 notas de 1 aluno e fazer a o calculo da soma de notas se o total for maior que 25 aprovado 

notas = []
cont=0
cont2 =0
nf = 0
#entrada

Nome_Aluno = input("Digite o Nome do aluno:")
for n in range(1,6):
    nt = int(input("Digite a nota:"))
    notas.append(nt)
    cont =cont+1
for i in notas:
    cont2=cont2+1
    nf = nf+i
    print("Nota {0} - {1}".format(cont2,i))

print("Fim do Cadastro de Notas!!")
print("Quatidade de Notas: {0}".format(cont))
print("Nota Final = {0}".format(nf))      
if nf < 25:
    print("Reprovado")
else:
    print("Aprovado")
