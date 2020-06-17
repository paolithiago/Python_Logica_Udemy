#entrada

indice=float(input("Digite o indice de poluicao: "))

#processamento

if (indice >= 0.3) and (indice < 0.4):
    print("grupo 1 suspender atividades")
elif (indice >= 0.4) and (indice < 0.5): 
        print("grupo 1 e grupo 2 suspender atividades")   
elif (indice >= 0.5): 
        print("Todos os grupos suspender atividades")


    