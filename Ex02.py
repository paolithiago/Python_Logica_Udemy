"""Elaborar um program que receba um valor e verifique se o mesmo e maior que 0 caso sim, armaze
na-lo na variavel e e imprimir, senao armazenar em b e imprimir"""

#Entrada
Valor=int(input("Digite o valor a ser analisado:"));

#Processamento

if Valor >0:
    a=Valor
    print("O valor e positivo: {0}",format(a))
else:
    b=Valor
    print("O valor e negativo: {0}",format(b))
print(Valor)