"""
ENTRADA:
A entrada é composta por 3 inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100), que indicam, respectivamente,
a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.

SAÍDA:
Um valor real indicando o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais.

Ex: 100 2 2 -> 25.00
"""

entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

#TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:
resultado = distancia / (diametro1 + diametro2)

print(format(resultado, '.2f'))