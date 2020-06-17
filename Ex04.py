""" receber a altura e sexo da pessoa e calcular o peso ideal
Para Homens - (72,7 *altura)-58
Para mulheres - (62,1*altura)-44,7  """
#Entrada
sexo=input("Informe Sexo -m/f: ")#JA E STRING
altura = float(input("Informe a altura: "))#CONVERTE STRING PARA FLOAT
    
#SEXO.LOWER E UMA FUNCAO PYTHON QUE CONVERTE PARA MINUSCULO ASSIM MESMO COM A ENTRADA EM MAISCULO
#CONVERTE PRIMEIRO PARA ANALISAR
#Processamento
if (sexo.lower() == "m"):
    pesoideal=((72.7*altura)-58)
elif (sexo.lower() == "f"):
    pesoideal=((62.1*altura)-44.7)
else:
    pesoideal=0
    print("Sexo nao reconhecido")
print("Peso Ideal {0:.1f}".format(pesoideal))
    