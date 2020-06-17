#Construir um sistema que receba a altura da pessoa e calcule o peso ideal
#Entrada
Altura = float(input("Digite sua altura:"));
#Processamento
CalculoPeso = (Altura*72.7)-58;
#Saida
print("O peso ideal de acordo com sua altura e: {0:.2f}".format(CalculoPeso));
