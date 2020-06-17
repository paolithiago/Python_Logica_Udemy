""" fazer algoritimo que leia duas variaveis, c e n , que sao o codigo e numero de 
horas tabalhadas de um operario, 
Calcular o salario sabendo que o mesmo ganha 10 reais por hora
quando o numero de hora exceder 50 calcular o valor excedente na variavel e. Caso contr
ario zerar a variavel e
A hora excedente vale 20 reais, no final imprimir salario e salario excedente
como fiz
"""
#Entrada de dados valore c codigo e n numero de horas trabalhadas
c=input("Digite o codigo do Funcionario:")
n=float(input("Digite as horas trabalhadas:"))
Salario = n*10
if n>50:
    e=(n-50)*20
    print("O salario do funcionario --> {0} e --> R${1:.1f}".format(c,Salario))
    print("O salario Extra do funcionario --> {0} e --> R${1:.1f}".format(c,e))
    print("O salario total com Extra do funcionario --> {0} e --> R${1:.1f}".format(c,Salario+e))
else:
    e=0
    print("O salario do funcionario {0} e -->R$ {1:.1f}".format(c,Salario))
    print("Funcionario nao fez horas excedentes!")
        
