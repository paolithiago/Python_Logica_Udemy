#Variaveis

#Entrada
num1=int(input("Digite o valor 1:"))
num2=int(input("Digite o valor 2:"))
num3=int(input("Digite o valor 3:"))
num4=int(input("Digite o valor 4:"))

#Processamento
q1=num1**2
q2=num2**2
q3=num3**2
q4=num4**2
if q3>=1000:
    print("Como q3 e maior igual a 1000 so imprime q3 -->{0}".format(q3))
else:
    print("N1 -->{0} E Q1-->{1}".format(num1,q1))
    print("N2 -->{0} E Q2-->{1}".format(num2,q2))
    print("N3 -->{0} E Q3-->{1}".format(num3,q3))
    print("N4 -->{0} E Q4-->{1}".format(num4,q4))
    
    