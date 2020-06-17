vetor=[]
pares=[]
cont=0
#preenche o vetor com os valores de no que sao os numeros de 1 a 6 - range do for
for n in range (1,1000000):
    vetor.append(n)
    if n % 2 == 0:
        pares.append(n)      
for i in pares:
    #print("n - {0}".format(i))
    cont=cont+1
print("Quantidade de Numeros divisiveis por 2: {0}".format(cont))
