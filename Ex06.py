#Programa que calcula o valor do salario final de acordo com horas
#e valor da hora
#Entrada
horas=int(input("Digite a quantidade de horas trabalhadas: "));
ValorSalario = float(input("Digite o valor do salario: "));

#processmaneto

TotSalario = horas*ValorSalario;

#Saida
#converte os valores para float onde o 0 e a variavel +:.2f, que sao dois digitos apos as casas
#decimais
print("O Valor total de salario e :{0:.2f}".format(TotSalario))