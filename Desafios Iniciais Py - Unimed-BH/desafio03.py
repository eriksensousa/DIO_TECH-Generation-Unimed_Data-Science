"""
ENTRADA:
O arquivo de entrada contém dois inteiros.
O primeiro é o tempo gasto na viagem em horas e o segundo é a velocidade média durante a mesma em km/h.

SAÍDA:
Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal.

Ex: 10 85 -> 70.833
"""

valores = input().split() 

#TODO:  Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.
resultado = int(valores[0]) / int(valores[1])

print(format(resultado, '.2f'))