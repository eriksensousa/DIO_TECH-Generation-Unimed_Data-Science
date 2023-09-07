"""
ENTRADA:
A entrada consiste de uma única linha que contém dois inteiros H e P (1 ≤ H, P ≤ 1000) indicando respectivamente
o número total de cachorros-quentes consumidos e o número total de participantes na competição.

SAÍDA:
Seu programa deve produzir uma única linha com um número racional representando o número médio de cachorros-quentes
consumidos pelos participantes. O resultado deve ser escrito como um número racional com exatamente dois dígitos após o ponto decimal,
arredondado se necessário.

Ex: 10 90 -> 0.11
"""

valores = input().split() 

#TODO:  Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.
resultado = int(valores[0]) / int(valores[1])

print(format(resultado, '.2f'))