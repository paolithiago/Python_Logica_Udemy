"""Ler a varivavel peso do peixe, verificar se ha excesso e se houver, gravar na 
variavel e e na variavel m o valor de multa que deve ser paga , caso contrario mostrar
variaveis como zero
cada multa e 4 reais por peso excedente
Como Fiz:
#Entrada de dados
pesopeixe = float(input("Digite o Peso do peixe:"))

#Processmaneto de dados
excesso = pesopeixe - 50
if (excesso >0 ):
    multa=excesso*4
else:
    multa=0
    excesso=0
print("O peso do peixe e {0}".format(pesopeixe))
print("O Valor do excesso e {0}".format(excesso))
print("O Valor da multa por excesso e {0:.1f}".format(multa))
Como Professor fez
 """
Peso=float(input("Insira o peso do peixe: "))
if Peso> 50:
    Multa=(Peso-50)*4
    Excesso = Peso-50
    print("A multa a ser paga e R$: {0:.1f}".format(Multa))
    print("O excesso do peixe e :{0:.1f} ".format(Excesso))
else:
    Multa=0
    Excesso=0
    print("A multa a ser paga e R$: {0:.1f}".format(Multa))
    print("O excesso do peixe e :{0:.1f} ".format(Excesso))


    