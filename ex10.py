#elaborar um programa que receba a indade de um nadador o na saida o classifique:
#entrada
idade=int(input("Digite a idade do Nadador: "))

#processamento

if (idade >= 5) and (idade <=7):
    print("Nadador da categoria infantil A")
elif (idade >= 8) and (idade <=11):
    print("Nadador da categoria infantil B")
elif (idade >= 12) and (idade <=13):
    print("Nadador da categoria Juvenil A")
elif (idade >= 14) and (idade <=17):
    print("Nadador da categoria Juvenil B")
elif (idade >= 18):
    print("Maior de 18 anos")
