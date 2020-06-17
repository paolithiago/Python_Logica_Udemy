"""fazer um programa que le um numero e verifica se e par ou impar, caso seja par armazenar em 
p, se for impar armazenar em i. Imprimir p e import"""
#Variaveis - como estamos imprimmindo as duas variaveis, idenpendente se passa no prcoessamento 
#pela condição(se entra no if ou no else) foi deslcarada variavel para imprimir os dois
p=0
i=0
#Entrada
Valor = int(input("Digite o valor a ser analisado"))
#Processamento
if ((Valor%2) == 0):
    p=Valor
else:
    i=Valor
print(p)
print(i)
        