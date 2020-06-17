"Fazer um progrmama que receba um numero inteiro e verifique se ele e par ou impar e se e positivo ou  negatvigto"

#Variaveis
inteiro=0
positivo=0
#Entrada
valor = int(input("Digite o valor a ser verificado:"))
#Processamento
if ((valor%2)==0):
    inteiro="Par"
else:
    inteiro="Impar"
if (valor>0):
    positivo="Positivo"
else:
    positivo="Negativo"
print("O Valor e : {0} e {1}".format(inteiro,positivo))
    


