#fazer um prgrama que receba a area do func e direcionar a pesquisa
#1 RH - 2 TI - 3 OP 

id = int(input("Digite seu ID :"))
while id !=0:
    func = int(input("Digite o numero da area"))
    if func == 1:
        print("RH")
    elif func==2:
        print("TI")
    elif func==3:
        print("OP")
    else:
        print("Outros")
    id = int(input("Digite seu ID :"))
print("Fim")
